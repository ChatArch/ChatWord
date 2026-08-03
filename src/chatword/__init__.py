"""ChatWord package."""

from chatword.document import (
    ChatWordError,
    DocumentInfo,
    DocumentParseError,
    MissingDependencyError,
    UnsupportedDocumentError,
    detect_document_kind,
    extract_text,
    inspect_document,
)

__version__ = "0.1.0"

__all__ = [
    "ChatWordError",
    "DocumentInfo",
    "DocumentParseError",
    "MissingDependencyError",
    "UnsupportedDocumentError",
    "__version__",
    "detect_document_kind",
    "extract_text",
    "inspect_document",
]
