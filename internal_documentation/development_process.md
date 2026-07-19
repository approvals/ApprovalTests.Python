# Development Process

STARTER_CHARACTER = 😎

For each step below, ask the human for confirmation before proceeding.

1. Create a micro feature document in `internal_documentation/micro_features/` describing the feature
2. Write a failing test
3. Implement the change to make the test pass
4. Run `./build_and_test.sh` to verify everything passes
5. Approve the `.received.` files that are correct. If the text is less than 10 line, prefer inline approvals.
6. Refactor as needed, re-running `./build_and_test.sh` after each change
7. Write user facing documentation. When you do this, read `internal_documentation\documentation_guidelines.md`
