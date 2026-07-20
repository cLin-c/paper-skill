param(
  [string]$Repo = "https://github.com/cLin-c/paper-skill",
  [string[]]$Targets,
  [switch]$DryRun
)

$ErrorActionPreference = 'Stop'
$Skill = "paper-skill"

if (-not $Targets -or $Targets.Count -eq 0) {
  $platforms = @('.claude', '.codex', '.openclaw', '.qwen', '.kimi', '.deepseek', '.comate', '.lingma')
  $Targets = @($platforms | Where-Object { Test-Path -LiteralPath "$env:USERPROFILE\$_" } | ForEach-Object { "$env:USERPROFILE\$_\skills\$Skill" })
  if ($Targets.Count -eq 0) { $Targets = @("$env:USERPROFILE\.codex\skills\$Skill") }
}

function Get-Version([string]$Path) {
  $file = Join-Path $Path "VERSION"
  if (Test-Path -LiteralPath $file) { return (Get-Content -Raw -Encoding UTF8 $file).Trim() }
  return "legacy"
}

function Test-PaperSkill([string]$Path) {
  $file = Join-Path $Path "SKILL.md"
  return (Test-Path -LiteralPath $file) -and (Select-String -LiteralPath $file -Pattern '^name:\s*paper-skill\s*$' -Quiet)
}

function Install-Target([string]$Target) {
  $label = $Target.Replace($env:USERPROFILE, "~")
  if ($DryRun) { Write-Host "DRY-RUN $label"; return "dry-run" }

  if (Test-Path -LiteralPath (Join-Path $Target ".git")) {
    if (-not (Test-PaperSkill $Target)) { throw "Refusing to update a Git directory that is not paper-skill: $Target" }
    $before = Get-Version $Target
    git -C $Target pull --ff-only -q
    if ($LASTEXITCODE -ne 0) { throw "git pull failed for $Target" }
    if (-not (Test-PaperSkill $Target)) { throw "paper-skill identity check failed after update: $Target" }
    Write-Host "updated  $label  $before -> $(Get-Version $Target)"
    return "updated"
  }

  $stamp = Get-Date -Format "yyyyMMdd-HHmmss-fff"
  $candidate = "$Target.installing-$stamp"
  $backup = $null
  New-Item -ItemType Directory -Force -Path (Split-Path $Target) | Out-Null

  try {
    git clone --depth=1 -q $Repo $candidate
    if ($LASTEXITCODE -ne 0 -or -not (Test-PaperSkill $candidate)) { throw "downloaded repository is not a valid paper-skill" }
    if (Test-Path -LiteralPath $Target) {
      $backup = "$Target.backup-$stamp"
      Move-Item -LiteralPath $Target -Destination $backup
      Write-Host "migrating $label (backup: $backup)"
    }
    Move-Item -LiteralPath $candidate -Destination $Target
    Write-Host "installed $label  version $(Get-Version $Target)"
    return $(if ($backup) { "migrated" } else { "installed" })
  } catch {
    if (Test-Path -LiteralPath $candidate) { Remove-Item -LiteralPath $candidate -Recurse -Force }
    if ($backup -and -not (Test-Path -LiteralPath $Target) -and (Test-Path -LiteralPath $backup)) { Move-Item -LiteralPath $backup -Destination $Target }
    throw
  }
}

Write-Host "paper-skill installer"
$counts = @{ installed = 0; updated = 0; migrated = 0; failed = 0; 'dry-run' = 0 }
foreach ($target in $Targets) {
  try { $counts[(Install-Target $target)]++ }
  catch { $counts.failed++; Write-Warning $_ }
}
Write-Host ("installed={0} updated={1} migrated={2} failed={3} dry-run={4}" -f $counts.installed, $counts.updated, $counts.migrated, $counts.failed, $counts.'dry-run')
if ($counts.failed -gt 0) { throw "$($counts.failed) target(s) failed" }
