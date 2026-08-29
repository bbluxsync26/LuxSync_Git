#!/usr/bin/env pwsh
$ErrorActionPreference = 'Stop'

$REPO_ROOT = Get-Location
Write-Host "Creating LuxSync repository structure in $REPO_ROOT..."

# Root folders
$dirs = @('docs', 'brand', 'content', 'prompts', 'website/public', 'website/src', 'website/pages', 'website/components', 'website/styles')
foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Path $dir -Force -ErrorAction SilentlyContinue | Out-Null
}

# README
$readmeContent = @"
# LuxSync

Where Luxury Lives Intelligently

## Purpose

LuxSync is a luxury smart-home automation and commerce company positioned at the intersection of premium branding and intelligent home technology.

This repository contains the strategy, brand assets, content, prompts, and website source code required to launch and grow the business.

## Repository Structure

docs     → Business and operational documentation
brand    → Visual identity and messaging
content  → Website and marketing copy
prompts  → AI prompt library
website  → Website source code

## Current Phase

Foundation & Launch Preparation

## Mission

To simplify luxury smart living through trusted curation, intelligent automation, and exceptional customer experiences.
"@
Set-Content -Path "README.md" -Value $readmeContent

# DOCS

$businessPlanContent = @"
# LuxSync Business Plan

## Business Overview

LuxSync is a luxury smart-home automation and commerce company.

## Value Proposition

We help customers create smarter, safer, and more elegant living environments through curated smart-home technology.

## Target Customers

- Short-term rental operators
- Seniors and caregivers
- Smart office managers
- Intentional parents
- Busy professionals

## Revenue Streams

- Product sales
- Automation bundles
- Subscription services

## Goals

- Launch storefront
- Establish supplier relationships
- Generate first sale
- Build customer trust
"@
Set-Content -Path "docs/business-plan.md" -Value $businessPlanContent

$launchPlanContent = @"
# Launch Plan

## Goal

Launch LuxSync within six days.

## Day 1

Infrastructure and storefront setup.

## Day 2

Supplier onboarding and catalog creation.

## Day 3

AI receptionist setup and testing.

## Day 4

Content creation and community outreach.

## Day 5

End-to-end testing.

## Day 6

Public launch.
"@
Set-Content -Path "docs/launch-plan.md" -Value $launchPlanContent

$financialModelContent = @"
# Financial Model

## Initial Targets

Startup Capital:
Less than `$500

Operating Overhead:
`$179.49/month

Gross Margin:
60.38%

## Month 1 Goals

Revenue:
`$8,564

Gross Profit:
`$5,171

Net Profit:
`$4,991.51

## Notes

Update this document as actual revenue data becomes available.
"@
Set-Content -Path "docs/financial-model.md" -Value $financialModelContent

# BRAND

$colorsContent = @"
# Plush Drift v2.1 Color System

## Primary Colors

Slate Navy
#0D1526

Dark Suede
#172036

Pale Driftwood
#D0BEB0

## Supporting Colors

Warm Taupe Mauve
#9E8B85

Antique Rose Taupe
#967878

Dusty Steel
#7B96B2

## Design Principle

Where warmth meets intelligence.

Where luxury feels like home.
"@
Set-Content -Path "brand/colors.md" -Value $colorsContent

$typographyContent = @"
# Typography

## Headlines

Font:
Manrope

Weights:
500
600

## Body Copy

Font:
Inter

Weights:
400
500

## UI Elements

Font:
Inter

Weight:
500

## Typography Goals

- Warm
- Comfortable
- Refined
- Human
- Modern
- Effortless

Avoid:

- Aggressive
- Corporate
- Technical
- Cold
"@
Set-Content -Path "brand/typography.md" -Value $typographyContent

$voiceContent = @"
# Voice & Tone

## Brand Voice

Intelligent Calm

## Personality

- Warm
- Confident
- Thoughtful
- Unhurried
- Professional

## We Sound Like

A trusted advisor.

## We Do Not Sound Like

- Pushy salespeople
- Tech enthusiasts showing off
- Corporate marketing jargon

## Example

Bad:

Buy now before supplies run out!

Good:

Thoughtfully selected solutions designed to make everyday living simpler and more enjoyable.
"@
Set-Content -Path "brand/voice-and-tone.md" -Value $voiceContent

# CONTENT

$homepageContent = @"
# Homepage

## Hero

Technology That Feels Like Home

Curated smart-home solutions, premium automation, and elevated living experiences designed to make life simpler.

## Sections

- Featured Solutions
- Why LuxSync
- How It Works
- Featured Products
- Email Signup

## CTA

Shop Collections
"@
Set-Content -Path "content/homepage.md" -Value $homepageContent

$aboutContent = @"
# About LuxSync

LuxSync was created to simplify smart-home technology without sacrificing elegance or quality.

Our mission is to help customers create homes that are safer, smarter, and more comfortable through trusted technology and thoughtful design.

We believe luxury is not complexity.

Luxury is confidence.
"@
Set-Content -Path "content/about.md" -Value $aboutContent

# PROMPTS

$contentWriterContent = @"
# Content Writer Prompt

You are a copywriter for LuxSync.

Guidelines:

- Sound warm and intelligent.
- Avoid hype.
- Avoid technical jargon when simple language works.
- Focus on customer benefits.
- Use the LuxSync voice:
  Intelligent Calm.

Output should feel premium, human, and trustworthy.
"@
Set-Content -Path "prompts/content-writer.md" -Value $contentWriterContent

$productDescContent = @"
# Product Description Prompt

Write a LuxSync product description.

Requirements:

- Highlight customer benefits.
- Emphasize simplicity.
- Emphasize compatibility.
- Keep language premium and approachable.
- Avoid exaggerated claims.

Format:

Headline

Overview

Key Benefits

Specifications

Call To Action
"@
Set-Content -Path "prompts/product-descriptions.md" -Value $productDescContent

$emailWriterContent = @"
# Email Writer Prompt

Write marketing emails for LuxSync.

Voice:

- Warm
- Sophisticated
- Relaxed
- Helpful

Structure:

Subject Line

Preview Text

Body

Call To Action

Never sound aggressive or sales-driven.
"@
Set-Content -Path "prompts/email-writer.md" -Value $emailWriterContent

# WEBSITE

$websiteReadmeContent = @"
# Website Application

This folder contains the LuxSync website source code.

## Objectives

- Fast performance
- Mobile-first design
- Accessibility
- Plush Drift design system
- SmartThings-focused messaging

## Brand Experience

Technology should feel invisible, intuitive, and dependable.
"@
Set-Content -Path "website/src/README.md" -Value $websiteReadmeContent

$homePageStructureContent = @"
# Home Page Structure

Hero

Featured Solutions

Why LuxSync

Product Collections

Email Signup

Footer
"@
Set-Content -Path "website/pages/home.md" -Value $homePageStructureContent

$designSystemContent = @"
# Design System

## Colors

Slate Navy:
#0D1526

Dark Suede:
#172036

Pale Driftwood:
#D0BEB0

Dusty Steel:
#7B96B2

## Typography

Headlines:
Manrope

Body:
Inter

## Design Principles

- Comfortable
- Modern
- Sophisticated
- Calm
- Human
"@
Set-Content -Path "website/styles/design-system.md" -Value $designSystemContent

Write-Host ""
Write-Host "✅ LuxSync repository structure created successfully."
Write-Host ""
Write-Host "Next steps:"
Write-Host "1. git init"
Write-Host "2. git add ."
Write-Host "3. git commit -m 'Initial LuxSync repository'"
Write-Host "4. Create GitHub repo"
Write-Host "5. git push"
