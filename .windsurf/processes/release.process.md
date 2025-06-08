# Release Process

STARTER_CHARACTER = 🚀

1. Ensure all changes are committed and pushed.
2. Wait for CI to pass, which you can observe with `gh run list`.
3. Run `./.windsurf/scripts/group-commits-by-prefix.ps1` to review the changes since the last release and show the results to the user in a new temp file.
4. Get the version number from the last tag: `git describe --tags --abbrev=0`
5. Prompt the user whether the new release should update major, minor, or patch. Print out the new suggested version number and get confirmation.
6. Create a new draft release by running `gh release create <version> --draft --title "<title>" --notes "<notes>"`
7. Open the new draft release in the web browser.
8. Tell the user to add a release title and description.
9. Tell the user push the release button.
10. Wait for CI to run on the new release, which you can observe with `gh run list --workflow "Publish Python Package to PyPI" --created YYYY-MM-DD`.
