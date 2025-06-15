# LuminaNotes

LuminaNotes is a workspace for experiments around generative music and creative coding.
It aggregates project notes alongside Python modules used for data processing and
model experimentation.

## Directory Structure

- `Lumina/` – Existing notes and documentation.
- `src/` – Python source modules.
  - `echoes/` – Utilities for loading and validating Morphology Map JSON files.
  - `omniintent/` – Placeholder for transformer-based model code.
- `tests/` – Pytest suites and related test assets.
- `data/` – Location for large bundles such as Echoes or Creative Packs.
- `.github/workflows/` – Continuous integration configuration.

Large binary assets are not stored in the repository. See `data/README.md`
for guidance on using Git LFS for large files.
