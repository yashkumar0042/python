---

# Understanding Git Basics

## Introduction
- **Version Control**: System for tracking changes in source code over time.
- **Git**: Distributed version control system.
- **Core Concepts**:
  - **Repository**: Storage for project files and version history.
  - **Commit**: Snapshot of changes at a specific point.
  - **Branch**: Independent line of development.

# Cloning a Repository and Performing Basic Operations

## Cloning
- `git clone <repository URL>`: Downloads a repository to the local machine.

## Basic Operations
- `git init`: Initializes a new Git repository.
- `git add <file>`: Stages changes for commit.
- `git commit -m "Commit message"`: Records changes in the repository.

# Fetching and Pulling Content

## Fetch
- `git fetch`: Retrieves changes from a remote repository.
  - Example: `git fetch origin`

## Pull
- `git pull origin <branch>`: Fetches and integrates changes from a remote branch.
  - Example: `git pull origin main`

# Pushing Code

- `git push origin <branch>`: Pushes changes to a remote repository.
  - Example: `git push origin feature-branch`

# Git Branching

## Creating a Branch
- `git branch <branch-name>`: Creates a new branch.
  - Example: `git branch feature-branch`
- `git checkout <branch-name>`: Switches to the new branch.
  - Example: `git checkout feature-branch`

## Merging
- `git merge <branch>`: Integrates changes from one branch into another.
  - Example: `git merge feature-branch`

# Git Merging

- `git merge <branch>`: Combines changes from different branches.
  - Example: `git merge feature-branch`

# Git Stash

- `git stash`: Temporarily saves changes for later use.
  - Example: `git stash`

# Git Add Interactive

- `git add -i`: Interactively stages changes.
  - Example: `git add -i`

# Git Rebase

- `git rebase <branch>`: Rewrites commit history by moving or combining commits.
  - Example: `git rebase main`

# Working With Multiple Repositories

- `git remote add <name> <repository URL>`: Links a local repository to a remote.
  - Example: `git remote add origin https://github.com/user/repo.git`

# Pull Requests

- Feature in platforms like GitHub to propose and discuss changes.
  - Create a branch, make changes, and create a pull request on GitHub.

# Git Log

- `git log`: Displays commit history.
- Options: `--oneline`, `--graph`, `--since`.
  - Example: `git log --oneline`

# Git Hooks

- Custom scripts triggered by Git events.
- Examples: `pre-commit`, `post-commit`.
  - Example of a `pre-commit` hook:
    ```bash
    #!/bin/bash
    echo "Running pre-commit checks..."
    # Add custom checks here
    ```
