#!/usr/bin/env pwsh
$ErrorActionPreference = 'Stop'

$REPO_ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "LuxSync repository bootstrap"
Write-Host "----------------------------"
Write-Host "This script is intentionally NON-DESTRUCTIVE."
Write-Host ""
Write-Host "The LuxSync repository on master is the source of truth. This script only ensures"
Write-Host "that the expected directory structure exists. It does not create, replace, or"
Write-Host "rewrite authoritative business, brand, content, prompt, or website documents."
Write-Host ""

$dirs = @(
    'docs',
    'brand',
    'brand/assets',
    'content',
    'prompts',
    'prompts/website',
    'website/public',
    'website/src',
    'website/pages',
    'website/components',
    'website/styles'
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Path (Join-Path $REPO_ROOT $dir) -Force -ErrorAction SilentlyContinue | Out-Null
}

Write-Host "✅ LuxSync repository directories verified."
Write-Host "No existing files were modified."
Write-Host ""
Write-Host "Authoritative content must be edited directly in the repository and reviewed through Git."
