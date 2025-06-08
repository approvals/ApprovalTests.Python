git fetch --tags

$latestTag = git describe --tags --abbrev=0

git log "$latestTag..HEAD" --format="%h %s" | Group-Object { $_.Substring(7,4) } | ForEach-Object { "`n# $($_.Name)"; $_.Group }

