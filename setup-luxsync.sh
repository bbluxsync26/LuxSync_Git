#!/bin/bash
set -euo pipefail

SCRIPT_PATH="${BASH_SOURCE[0]}"
if [[ "$SCRIPT_PATH" != /* ]]; then
  SCRIPT_PATH="$PWD/$SCRIPT_PATH"
fi
REPO_ROOT="$(cd -- "$(dirname -- "$SCRIPT_PATH")" && pwd)"

echo "Creating LuxSync repository structure in $REPO_ROOT..."

# Root folders
for dir in docs brand content prompts website/public website/src website/pages website/components website/styles; do
  mkdir -p "$REPO_ROOT/$dir"
done

# README
cat > "$REPO_ROOT/README.md" <<'EOF'
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
EOF

# DOCS

cat > "$REPO_ROOT/docs/business-plan.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/docs/launch-plan.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/docs/financial-model.md" <<'EOF'
# Financial Model

## Initial Targets

Startup Capital:
Less than $500

Operating Overhead:
$179.49/month

Gross Margin:
60.38%

## Month 1 Goals

Revenue:
$8,564

Gross Profit:
$5,171

Net Profit:
$4,991.51

## Notes

Update this document as actual revenue data becomes available.
EOF

# BRAND

cat > "$REPO_ROOT/brand/colors.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/brand/typography.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/brand/voice-and-tone.md" <<'EOF'
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
EOF

# CONTENT

cat > "$REPO_ROOT/content/homepage.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/content/about.md" <<'EOF'
# About LuxSync

LuxSync was created to simplify smart-home technology without sacrificing elegance or quality.

Our mission is to help customers create homes that are safer, smarter, and more comfortable through trusted technology and thoughtful design.

We believe luxury is not complexity.

Luxury is confidence.
EOF

# PROMPTS

cat > "$REPO_ROOT/prompts/content-writer.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/prompts/product-descriptions.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/prompts/email-writer.md" <<'EOF'
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
EOF

# WEBSITE

cat > "$REPO_ROOT/website/src/README.md" <<'EOF'
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
EOF

cat > "$REPO_ROOT/website/pages/home.md" <<'EOF'
# Home Page Structure

Hero

Featured Solutions

Why LuxSync

Product Collections

Email Signup

Footer
EOF

cat > "$REPO_ROOT/website/styles/design-system.md" <<'EOF'
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
EOF

echo ""
echo "✅ LuxSync repository structure created successfully."
echo ""
echo "Next steps:"
echo "1. git init"
echo "2. git add ."
echo "3. git commit -m 'Initial LuxSync repository'"
echo "4. Create GitHub repo"
echo "5. git push"
