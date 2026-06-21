# paper-skill universal installer — installs to all supported AI coding platforms
# Usage: irm https://raw.githubusercontent.com/cLin-c/paper-skill/main/install.ps1 | iex
$ErrorActionPreference = 'Stop'

$Repo  = "https://github.com/cLin-c/paper-skill"
$Skill = "paper-skill"

$Targets = @(
  "$env:USERPROFILE\.claude\skills\$Skill"
  "$env:USERPROFILE\.codex\skills\$Skill"
  "$env:USERPROFILE\.openclaw\skills\$Skill"
  "$env:USERPROFILE\.qwen\skills\$Skill"
  "$env:USERPROFILE\.kimi\skills\$Skill"
  "$env:USERPROFILE\.deepseek\skills\$Skill"
  "$env:USERPROFILE\.comate\skills\$Skill"
  "$env:USERPROFILE\.lingma\skills\$Skill"
)

$ok = 0; $upd = 0; $fail = 0

Write-Host "📦  paper-skill installer"
Write-Host ("━" * 50)

foreach ($Target in $Targets) {
  $Label = $Target.Replace($env:USERPROFILE, "~")
  if (Test-Path "$Target\.git") {
    Write-Host ("↻  {0,-48}" -f $Label) -NoNewline
    try {
      git -C $Target pull --ff-only -q 2>$null
      Write-Host " updated"
      $upd++
    } catch {
      Write-Host " (already up to date)"
      $upd++
    }
  } else {
    Write-Host ("✓  {0,-48}" -f $Label) -NoNewline
    try {
      New-Item -ItemType Directory -Force -Path (Split-Path $Target) | Out-Null
      git clone --depth=1 -q $Repo $Target 2>$null
      Write-Host " installed"
      $ok++
    } catch {
      Write-Host " FAILED"
      $fail++
    }
  }
}

Write-Host ("━" * 50)
Write-Host "✅  $ok installed, $upd updated, $fail failed"
Write-Host ""
Write-Host "Invoke in any supported platform:"
Write-Host "  /paper-skill"
