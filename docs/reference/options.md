# Options

All `verify()` methods take an optional `options` parameter to configure reporters, scrubbers, file extensions, etc. See the [Options diagram](https://raw.githack.com/approvals/ApprovalTests.Python/main/docs/images/options_diagram.html) for more details.

## Inline Approvals

### Known Issues

- Pycharm automatically removes trailing whitespace, which can cause the approval file to be different from the actual output.
  - To disable this behavior go to:
  - File -> Settings -> Editor -> General -> On Save -> [ ] Remove trailing spaces
