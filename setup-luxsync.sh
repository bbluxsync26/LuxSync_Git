#!/bin/bash
set -euo pipefail

SCRIPT_PATH="${BASH_SOURCE[0]}"
if [[ "$SCRIPT_PATH" != /* ]]; then
  SCRIPT_PATH="$PWD/$SCRIPT_PATH"
fi
REPO_ROOT="$(cd -- "$(dirname -- "$SCRIPT_PATH")" && pwd)"

cat <<'EOF'
LuxSync repository bootstrap
----------------------------
This script is intentionally NON-DESTRUCTIVE.

The LuxSync repository on master is the source of truth. This script only ensures
that the expected directory structure exists. It does not create, replace, or
rewrite authoritative business, brand, content, prompt, or website documents.
EOF

# Expected repository structure. mkdir -p is safe for existing directories.
for dir in \
  docs \
  brand \
  brand/assets \
  content \
  prompts \
  prompts/website \
  website/public \
  website/src \
  website/pages \
  website/components \
  website/styles; do
  mkdir -p "$REPO_ROOT/$dir"
done

echo ""
echo "✅ LuxSync repository directories verified."
echo "No existing files were modified."
echo ""
echo "Authoritative content must be edited directly in the repository and reviewed through Git."
