# Get today's date in YYYY-MM-DD format
$today = Get-Date -Format "yyyy-MM-dd"

# Read the current content of TODO.md
$content = Get-Content "TODO.md" -Raw

# Create new content with today's date at the top
$newContent = "$today`n- [ ]`n`n$content"

# Write the new content to TODO.md
Set-Content "TODO.md" -Value $newContent -NoNewline

Write-Host "Added $today to the top of TODO.md"
