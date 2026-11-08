<!--
Every commit in this PR reaches main and decides the release version.
Each one must be a conventional commit, and the strongest type wins:
  feat: ...   -> minor release        fix: ...    -> patch release
  feat!: ...  -> breaking change      docs/ci/chore/test/refactor: ... -> no release
Clean up vague commits ("update config") before merging: they show up in the changelog.
-->

## Summary

<!-- What does this change and why? Link related issues with "Closes #123". -->

## Requirements

<!-- IDs from docs/requirements.xlsx that this PR addresses, e.g. IMU-DRV-005, IMU-DRV-006. Write "None" if no requirement applies (docs, CI, tooling). -->

## How was this tested?

- [ ] Unit tests (`uv run pytest`)
- [ ] On hardware <!-- board, sensor model, wiring/bus, e.g. "Raspberry Pi 5 + ICM-20948 over I2C" -->
- [ ] Not applicable <!-- docs, CI or tooling only -->

## Checklist

- [ ] Tests added or updated for new behavior
- [ ] `docs/requirements.xlsx` updated (status, tests) for the requirements listed above
- [ ] README or docs updated if usage changed
- [ ] Breaking changes use `!` in the commit type and are described below

## Breaking changes

<!-- Delete this section if there are none. Otherwise describe what breaks and how to migrate. -->
