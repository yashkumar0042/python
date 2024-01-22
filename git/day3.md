# Understanding Git Basics

## Introduction
**Version Control:** It is a collaborative system that manages changes to source code over time. It enables tracking modifications, coordinating work among multiple contributors, and maintaining a historical record of project development.

**Git:** A distributed version control system that allows multiple developers to work on a project simultaneously. It tracks changes in a decentralized manner, providing flexibility and efficiency in collaboration.

## Core Concepts

**Repository:** A repository is a central storage location for project files and their complete version history. It serves as a collaborative space where developers can contribute and access the latest codebase.

**Commit:** A commit is a snapshot of the project at a specific point in time. It represents a set of changes made to the code, allowing developers to track and manage the development progress.

**Branch:** A branch is an independent line of development that diverges from the main codebase. It enables developers to work on features or bug fixes separately, promoting parallel development.

## Cloning a Repository and Performing Basic Operations

### Cloning
- `git clone <repository URL>`: Cloning is the process of copying a repository from a remote source to a local machine. It establishes a connection between the local and remote repositories for collaborative development.

### Basic Operations
- `git init`: Initializes a new Git repository in the current directory, creating the necessary data structures for version control.
- `git add <file>`: Adds changes to the staging area, preparing them for the next commit.
- `git commit -m "Commit message"`: Records changes in the repository with a descriptive commit message.

## Fetching and Pulling Content

### Fetch
- `git fetch`: Retrieves changes from a remote repository without merging them into the local branch. It updates the local repository with the latest changes.

### Pull
- `git pull origin <branch>`: Fetches changes from a remote branch and automatically integrates them into the local branch. It combines the fetch and merge operations.

## Pushing Code

- `git push origin <branch>`: Pushes local changes to a remote repository, making them accessible to other collaborators. It updates the remote repository with the latest changes.

## Git Branching

### Creating a Branch
- `git branch <branch-name>`: Creates a new branch with the specified name, allowing developers to work on separate features or fixes.
- `git checkout <branch-name>`: Switches to the newly created branch for further development.

### Merging
- `git merge <branch>`: Integrates changes from one branch into another. It combines the changes made in the specified branch into the current working branch.

## Git Merging

- `git merge <branch>`: Combines changes from different branches, bringing them together into a unified codebase.

## Git Stash

- `git stash`: Temporarily saves changes that are not ready for commit. It allows developers to switch branches without committing incomplete work.

## Git Add Interactive

- `git add -i`: Interactively stages changes, providing a user interface to choose which changes to include in the next commit.

## Git Rebase

- `git rebase <branch>`: Rewrites commit history by moving or combining commits. It helps create a linear and cleaner history.

## Working With Multiple Repositories

- `git remote add <name> <repository URL>`: Links a local repository to a remote repository, allowing collaboration between different copies of the codebase.

## Pull Requests

A feature in platforms like GitHub, pull requests allow developers to propose changes, discuss modifications, and merge code into the main branch.

## Git Log

- `git log`: Displays the commit history of the repository, providing details such as commit messages, authors, and timestamps.
  - Options: `--oneline`, `--graph`, `--since`.

## Git Hooks

Custom scripts triggered by Git events. Examples include pre-commit and post-commit hooks.

Example of a pre-commit hook:
```bash
#!/bin/bash
echo "Running pre-commit checks..."
# Add custom checks here
```

A post-commit hook is a custom script that runs automatically after a commit has been made in a Git repository. It can be used to perform additional actions or tasks based on the successful completion of a commit. Here's an example of a post-commit hook:

```bash
#!/bin/bash
# post-commit hook example

echo "Executing post-commit hook..."

# Notify developers or team members about the commit
# This could be done via email, messaging, or any other communication method
echo "Commit successfully made. Notify relevant team members."

# Trigger an automated build or deployment process
# This example assumes the presence of a build script or deployment process
./build_script.sh

# Additional actions or notifications based on your project's requirements

echo "Post-commit hook executed successfully."
```

In this example, the post-commit hook performs the following actions:

1. Prints a message indicating that the post-commit hook is being executed.
2. Notifies relevant team members about the successful commit.
3. Triggers an automated build or deployment process by calling a hypothetical `build_script.sh`.
4. Provides a placeholder for additional actions or notifications specific to the project.

Keep in mind that the specific actions performed in a post-commit hook can vary based on the project's needs. Hooks provide a way to customize and automate processes to enhance the development workflow.
