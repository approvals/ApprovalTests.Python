# Release Process

STARTER_CHARACTER = 🚀

1. Check the GitHub CLI login: `gh auth status`
   - If the token is invalid, offer the login from `internal_documentation/github_guidelines.md`.
1. Ensure all changes are committed and pushed.
1. Wait for CI to pass, which you can observe with `gh run list`.
1. Run `./.windsurf/scripts/group-commits-by-prefix.ps1` to review the changes since the last release and show the results to the user in a new temp file.
1. Get the version number from the last tag: `git describe --tags --abbrev=0`
1. Suggest to the user whether the new release should update major, minor, or patch. Print out the new suggested version number and get confirmation.
1. Create a new draft release by running `gh release create <version> --draft --title "<title>" --notes "<notes>"`
1. Open the new draft release in the web browser.
1. Tell the user to add a release title and description.
1. Tell the user to push the release button.
1. Wait for publish action to run on the new release, which you can observe with `gh run list --workflow "Publish Python Package to PyPI" --created YYYY-MM-DD`.
1. Run the "Test Current Release" GitHub workflow to verify the release.
