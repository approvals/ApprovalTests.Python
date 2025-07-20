# TDD Production Code Implementation Process

STARTER_CHARACTER = 🟢

**ALWAYS** ask the user one question at a time and wait for a response.

**ALWAYS** confirm file names and locations if unsure.

**NEVER** make changes to Test code in this process.

This process is for implementing production code for a new feature or bug fix.


## Steps
1. If needed, confirm the relevant test file and its location.
2. Repeat the following until all tests pass:
   - Run the tests.
   - Identify the first failing test.
   - Implement only the production code necessary to make that test pass.
   - Run the tests again.
   - After each successful run, ask the user if they would like to commit.
3. When all tests pass, recommend a final commit or review.

## Code Style
- Prefer code that is self-explanatory and easy to read over comments.
- Use functional helper methods instead of long methods.
- Prefer `org.lambda.query.Queryable` over Java streams.