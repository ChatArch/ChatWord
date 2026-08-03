"""CLI entrypoint for chatword."""

from __future__ import annotations

import json
from pathlib import Path

import click
from chatstyle import (
    CommandField,
    CommandSchema,
    add_interactive_option,
    render_success,
    resolve_command_inputs,
)

from chatword import __version__


HELLO_SCHEMA = CommandSchema(
    name="hello",
    fields=(CommandField("name", prompt="name", required=True),),
)
INSPECT_SCHEMA = CommandSchema(
    name="inspect",
    fields=(CommandField("path", prompt="document path", required=True),),
)
EXTRACT_SCHEMA = CommandSchema(
    name="extract",
    fields=(CommandField("path", prompt="document path", required=True),),
)


def _resolve_document_path(
    schema: CommandSchema,
    path: Path | None,
    interactive: bool | None,
    usage: str,
) -> Path:
    values = resolve_command_inputs(
        schema=schema,
        provided={"path": path},
        interactive=interactive,
        usage=usage,
    )
    resolved = Path(values["path"]).expanduser()
    if not resolved.exists():
        raise click.ClickException(f"document not found: {resolved}")
    if not resolved.is_file():
        raise click.ClickException(f"document path is not a file: {resolved}")
    return resolved


@click.group()
@click.version_option(__version__, prog_name="chatword")
def main() -> None:
    """Task-oriented Word and PDF workflows for ChatArch."""


@main.command()
@click.argument("name", required=False)
@add_interactive_option
def hello(name: str | None, interactive: bool | None) -> None:
    """Print a greeting with ChatStyle-backed input resolution."""

    values = resolve_command_inputs(
        schema=HELLO_SCHEMA,
        provided={"name": name},
        interactive=interactive,
        usage="Usage: chatword hello [NAME]",
    )
    render_success(f"Hello, {values['name']}!")


@main.command("inspect")
@click.argument(
    "path",
    required=False,
    type=click.Path(dir_okay=False, path_type=Path),
)
@click.option("--json", "as_json", is_flag=True, help="Print machine-readable JSON.")
@add_interactive_option
def inspect_command(path: Path | None, as_json: bool, interactive: bool | None) -> None:
    """Inspect a Word or PDF file before deeper processing."""

    from chatword.document import ChatWordError, inspect_document

    resolved_path = _resolve_document_path(
        INSPECT_SCHEMA,
        path,
        interactive,
        "Usage: chatword inspect [PATH]",
    )
    try:
        info = inspect_document(resolved_path)
    except ChatWordError as exc:
        raise click.ClickException(str(exc)) from exc
    if as_json:
        click.echo(json.dumps(info.to_dict(), ensure_ascii=False, indent=2))
        return

    click.echo(f"path: {info.path}")
    click.echo(f"kind: {info.kind}")
    click.echo(f"suffix: {info.suffix or 'none'}")
    click.echo(f"size_bytes: {info.size_bytes}")
    click.echo(f"parser: {info.parser}")
    for key, value in info.details.items():
        click.echo(f"{key}: {value}")
    if info.warning:
        click.echo(f"warning: {info.warning}")


@main.command()
@click.argument(
    "path",
    required=False,
    type=click.Path(dir_okay=False, path_type=Path),
)
@click.option(
    "-o",
    "--output",
    type=click.Path(dir_okay=False, path_type=Path),
    help="Write extracted plain text to a file instead of stdout.",
)
@click.option("--force", is_flag=True, help="Allow replacing an existing output file.")
@add_interactive_option
def extract(
    path: Path | None,
    output: Path | None,
    force: bool,
    interactive: bool | None,
) -> None:
    """Extract plain text from a supported document."""

    from chatword.document import ChatWordError, extract_text

    resolved_path = _resolve_document_path(
        EXTRACT_SCHEMA,
        path,
        interactive,
        "Usage: chatword extract [PATH] [-o OUTPUT] [--force]",
    )
    if output is not None:
        output = output.expanduser()
        if output.resolve() == resolved_path.resolve():
            raise click.ClickException("output path must not be the input document")
        if output.exists() and not force:
            raise click.ClickException(f"output file already exists: {output}; use --force to replace it")

    try:
        text = extract_text(resolved_path)
    except ChatWordError as exc:
        raise click.ClickException(str(exc)) from exc

    if output is None:
        click.echo(text, nl=False)
        return

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(text, encoding="utf-8")
    render_success(f"Extracted text to {output}")


if __name__ == "__main__":
    main()
