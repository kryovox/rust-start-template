#!/usr/bin/env bash
set -Eeuo pipefail

if [[ $# -ne 2 || ! $1 =~ ^academy-[0-9]{2}-(cpp|rust)01-[a-f0-9]{8}$ || ! $2 =~ ^[A-Za-z0-9-]+/[A-Za-z0-9._-]+$ ]]; then
  echo "Usage: bash academy-lab/scripts/start-work.sh BRANCH OWNER/REPO" >&2
  exit 1
fi
branch=$1
expected_repo=${2,,}
cd "$(git rev-parse --show-toplevel)"
if [[ -n $(git status --porcelain) ]]; then
  echo "Save or commit your current work before switching branches." >&2
  exit 1
fi
origin=$(git remote get-url origin)
case "$origin" in
  https://github.com/*) actual_repo=${origin#https://github.com/} ;;
  git@github.com:*) actual_repo=${origin#git@github.com:} ;;
  ssh://git@github.com/*) actual_repo=${origin#ssh://git@github.com/} ;;
  *) echo "Expected a GitHub origin." >&2; exit 1 ;;
esac
actual_repo=${actual_repo%.git}
actual_repo=${actual_repo,,}
if [[ "$actual_repo" != "$expected_repo" || "$actual_repo" == 'kryovox/cpp-start-template' || "$actual_repo" == 'kryovox/rust-start-template' ]]; then
  echo "Open your assigned personal repository; the instructor template is protected." >&2
  exit 1
fi

git check-ref-format --branch "$branch" >/dev/null
git fetch origin refs/heads/main:refs/remotes/origin/main

remote_exists=0
if git ls-remote --exit-code --heads origin "refs/heads/$branch" >/dev/null; then
  remote_exists=1
else
  rc=$?
  if [[ $rc -ne 2 ]]; then echo 'Could not inspect the remote branch.' >&2; exit "$rc"; fi
fi
if [[ $remote_exists -eq 1 ]]; then
  git fetch origin "refs/heads/$branch:refs/remotes/origin/$branch"
fi
if git show-ref --verify --quiet "refs/heads/$branch"; then
  git switch "$branch"
elif [[ $remote_exists -eq 1 ]]; then
  git switch --track -c "$branch" "origin/$branch"
else
  git switch -c "$branch" origin/main
fi
if [[ $remote_exists -eq 1 ]]; then
  git branch --set-upstream-to="origin/$branch" "$branch"
  echo "Resumed existing work. Local history is preserved."
else
  git push --set-upstream origin "$branch"
  echo "Created separate work branch."
fi
echo "Current branch: $(git branch --show-current)"

