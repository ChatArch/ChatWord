import json

import pytest
from click.testing import CliRunner

from chatword.cli import main
from chatword.document import ChatWordError, detect_document_kind, inspect_document


def _write_docx(path):
    from docx import Document  # type: ignore[reportMissingImports]

    document = Document()
    document.add_paragraph("ChatWord sample")
    document.save(path)


def _write_pdf(path, encrypted=False):
    from pypdf import PdfWriter  # type: ignore[reportMissingImports]

    writer = PdfWriter()
    writer.add_blank_page(width=72, height=72)
    if encrypted:
        writer.encrypt("secret")
    with path.open("wb") as file:
        writer.write(file)


def test_hello_command_accepts_explicit_name():
    result = CliRunner().invoke(main, ["hello", "ChatArch"])

    assert result.exit_code == 0
    assert "Hello, ChatArch!" in result.output


def test_detect_document_kind_from_suffix():
    assert detect_document_kind("brief.docx") == "docx"
    assert detect_document_kind("scan.pdf") == "pdf"
    assert detect_document_kind("legacy.doc") == "doc"
    assert detect_document_kind("notes.txt") == "unknown"


def test_inspect_command_reports_basic_unknown_file(tmp_path):
    sample = tmp_path / "notes.txt"
    sample.write_text("hello", encoding="utf-8")

    result = CliRunner().invoke(main, ["inspect", str(sample)])

    assert result.exit_code == 0
    assert "kind: unknown" in result.output
    assert "warning: Unsupported document type." in result.output


def test_inspect_command_can_emit_json(tmp_path):
    sample = tmp_path / "notes.txt"
    sample.write_text("hello", encoding="utf-8")

    result = CliRunner().invoke(main, ["inspect", "--json", str(sample)])

    assert result.exit_code == 0
    assert '"kind": "unknown"' in result.output
    assert '"size_bytes": 5' in result.output


def test_extract_command_rejects_unknown_file(tmp_path):
    sample = tmp_path / "notes.txt"
    sample.write_text("hello", encoding="utf-8")

    result = CliRunner().invoke(main, ["extract", str(sample)])

    assert result.exit_code != 0
    assert "Unsupported document type" in result.output


def test_inspect_and_extract_docx(tmp_path):
    sample = tmp_path / "sample.docx"
    output = tmp_path / "sample.txt"
    _write_docx(sample)

    inspected = CliRunner().invoke(main, ["inspect", "--json", str(sample)])
    extracted = CliRunner().invoke(main, ["extract", str(sample), "-o", str(output)])

    assert inspected.exit_code == 0
    payload = json.loads(inspected.output)
    assert payload["kind"] == "docx"
    assert payload["parser"] == "python-docx"
    assert payload["details"]["paragraphs"] == 1
    assert extracted.exit_code == 0
    assert output.read_text(encoding="utf-8") == "ChatWord sample\n"


def test_extract_protects_input_and_existing_output(tmp_path):
    sample = tmp_path / "sample.docx"
    output = tmp_path / "sample.txt"
    _write_docx(sample)
    source_bytes = sample.read_bytes()
    output.write_text("keep\n", encoding="utf-8")

    same_path = CliRunner().invoke(main, ["extract", str(sample), "-o", str(sample)])
    existing = CliRunner().invoke(main, ["extract", str(sample), "-o", str(output)])
    forced = CliRunner().invoke(main, ["extract", str(sample), "-o", str(output), "--force"])

    assert same_path.exit_code != 0
    assert "must not be the input" in same_path.output
    assert sample.read_bytes() == source_bytes
    assert existing.exit_code != 0
    assert "already exists" in existing.output
    assert forced.exit_code == 0
    assert output.read_text(encoding="utf-8") == "ChatWord sample\n"


def test_pdf_inspection_and_encrypted_error_contract(tmp_path):
    sample = tmp_path / "sample.pdf"
    encrypted = tmp_path / "encrypted.pdf"
    _write_pdf(sample)
    _write_pdf(encrypted, encrypted=True)

    inspected = CliRunner().invoke(main, ["inspect", "--json", str(sample)])
    encrypted_info = CliRunner().invoke(main, ["inspect", str(encrypted)])
    encrypted_extract = CliRunner().invoke(main, ["extract", str(encrypted)])

    assert inspected.exit_code == 0
    assert json.loads(inspected.output)["details"]["pages"] == 1
    assert encrypted_info.exit_code == 0
    assert "encrypted: True" in encrypted_info.output
    assert "requires a password" in encrypted_info.output
    assert encrypted_extract.exit_code != 0
    assert "Encrypted PDF content requires a password" in encrypted_extract.output


def test_public_api_wraps_missing_file_and_cli_supports_noninteractive_mode(tmp_path):
    missing = tmp_path / "missing.docx"

    with pytest.raises(ChatWordError, match="Document not found"):
        inspect_document(missing)

    result = CliRunner().invoke(main, ["inspect", "-I"])
    assert result.exit_code != 0
    assert "Missing required value: path" in result.output
