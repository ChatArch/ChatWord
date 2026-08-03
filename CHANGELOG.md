# Changelog

## Unreleased

### Added

- Added optional Word/PDF/OCR dependency groups for common document workflows.
- Added `chatword inspect` and `chatword extract` commands for task-oriented document processing.
- Added document helper APIs for detecting, inspecting, and extracting text from Word/PDF files.
- Added CLI design documentation for current MVP commands and planned next tasks.

### Changed

- Added the shared `-i/-I` missing-input contract to document commands.
- Protected extraction outputs from accidental overwrite and normalized parser failures into ChatWord errors.
- Added real DOCX/PDF, encrypted PDF, and output-safety coverage to CI.

## 0.1.0 - 2026-06-23

### Added

- Initial ChatWord package release after PyPI name reservation.
- `chatword` CLI scaffold with a `hello` command.

## 0.0.1 - 2026-06-23

### Added

- Placeholder PyPI name reservation release.
