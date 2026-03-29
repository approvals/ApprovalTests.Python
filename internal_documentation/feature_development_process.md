## Feature Development Process

1. Create a micro feature document in `internal_documentation/micro_features/` describing the feature
2. Write a failing test
3. Implement the feature to make the test pass
4. Run `./build_and_test.sh` to verify everything passes
5. Approve the `.received.` files that are correct
6. Refactor as needed, re-running `./build_and_test.sh` after each change
