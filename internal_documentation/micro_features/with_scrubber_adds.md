# `with_scrubber` Adds by Default

Issue: https://github.com/approvals/ApprovalTests.Python/issues/276

## Purpose
People find `with_scrubber` and `add_scrubber` confusing. They don't realize that `with_scrubber` overwrites any existing scrubber, and that they need `add_scrubber` to chain scrubbers instead.

## Behavior
1. `Options.with_scrubber(scrubber)` adds the scrubber to any existing scrubbers, the same way `add_scrubber` does today.
2. `Options.with_scrubber(scrubber, replace=True)` replaces any existing scrubbers (today's behavior).
3. `replace` is keyword-only and defaults to `False`.
4. `add_scrubber` keeps working and behaves the same as `with_scrubber`.

## Usage Example
```python
options = Options().with_scrubber(scrub_dates).with_scrubber(scrub_guids)
# both scrubbers run

options = options.with_scrubber(scrub_names, replace=True)
# only scrub_names runs
```

## Compatibility
This changes behavior for anyone who calls `with_scrubber` twice and relies on the second call replacing the first. They need to add `replace=True`.
