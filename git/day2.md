# 5. Distributed Git
# I. Distributed Workflows

## Understanding Distributed Workflows
- Distributed version control allows for decentralized collaboration.
- Various workflows accommodate different project structures.

## Centralized Workflow
- Single shared repository.
- Contributors clone, make changes, and push to the central repository.

## Feature Branch Workflow
- Each feature or bug fix gets its own branch.
- Branches are merged into the main branch when ready.

## Forking Workflow
- Contributors fork the repository to their accounts.
- Pull requests are used to propose changes to the original repository.

# II. Contributing to a Project

## Forking a Repository
- Fork the repository on a platform like GitHub.
- Creates a copy under the contributor's account.

## Cloning and Branching
- Clone the forked repository to the local machine.
- Create a branch for the intended contribution.

## Making Changes
- Make and commit changes to the local branch.
- Regularly pull changes from the original repository to stay updated.

## Pushing Changes and Pull Requests
- Push changes to the forked repository.
- Create a pull request to propose changes to the original repository.

# III. Maintaining a Project

## Reviewing Pull Requests
- Project maintainers review and discuss proposed changes.
- Automated testing may be employed to ensure code quality.

## Merging Pull Requests
- Approved changes are merged into the main branch.
- Contributors may need to resolve conflicts during the merge.

## Versioning and Releases
- Use tags or branches to mark releases.
- Document changes in a release notes file.

# IV. Summary

## Key Takeaways
- Distributed workflows offer flexibility in collaboration.
- Contributors fork, clone, and branch to make changes.
- Pull requests facilitate collaboration and code review.
- Maintainers review, merge, and release new versions.
- Clear documentation and communication are essential for successful collaboration.

Certainly! Here are detailed PowerPoint notes on the GitHub topics:

---
# 6. GitHub
# I. Account Setup and Configuration

## Creating a GitHub Account
- Sign up on the GitHub website.
- Choose a username and configure account settings.

## Configuring Git on Local Machine
- Set global Git configurations: `git config --global user.name "Your Name"` and `git config --global user.email "your@email.com"`.
- Optionally, set other configurations like preferred text editor.

# II. Contributing to a Project

## Forking a Repository
- Fork a repository on GitHub to create a personal copy.
- Clone the forked repository to the local machine.

## Branching and Making Changes
- Create a branch for the intended contribution: `git checkout -b <branch-name>`.
- Make changes, commit them, and push to the forked repository.

## Creating a Pull Request
- Initiate a pull request on GitHub.
- Describe the changes made and request a review.

# III. Maintaining a Project

## Reviewing Pull Requests
- Project maintainers review proposed changes.
- Use comments and reviews to provide feedback.

## Merging Pull Requests
- Merge approved pull requests into the main branch.
- Resolve conflicts if necessary during the merge.

## Releases and Versioning
- Use GitHub releases to mark project milestones.
- Document changes in release notes.

# IV. Managing an Organization

## Creating an Organization
- Create an organization on GitHub for collaborative projects.
- Invite members to join the organization.

## Repository Permissions
- Set permissions for organization members based on roles.
- Control access to repositories.

# V. Scripting GitHub

## GitHub Actions
- Automate workflows with GitHub Actions.
- Define custom CI/CD processes in a YAML file.

## GitHub API
- Use the GitHub API for programmatic interaction.
- Automate repetitive tasks or gather repository information.

# VI. Summary

## Key Takeaways
- GitHub is a platform for version control and collaborative software development.
- Forking and branching are essential for contributing to projects.
- Pull requests facilitate code review and collaboration.
- Maintainers review, merge, and release changes.
- Organizations help manage collaborative projects.
- GitHub provides automation through GitHub Actions and an API.

---
# 7. Git Tools
# I. Revision Selection

## Git Log
- `git log`: Displays commit history.
- Options like `--oneline`, `--graph`, and `--since` provide different views.

## Git Show
- `git show <commit>`: Displays details of a specific commit.
- Useful for reviewing changes introduced in a commit.

# II. Interactive Staging

## Git Add -p
- `git add -p`: Interactively stage changes.
- Allows selecting specific changes within a file.

# III. Stashing and Cleaning

## Git Stash
- `git stash`: Temporarily saves changes.
- Useful for switching branches without committing.

## Git Clean
- `git clean`: Removes untracked files from the working directory.
- Use with caution to avoid unintentional data loss.

# IV. Signing Your Work

## Git Commit -S
- `git commit -S`: Sign commits using GPG.
- Adds a cryptographic signature to each commit.

# V. Searching

## Git Grep
- `git grep <pattern>`: Searches for a pattern in the repository.
- Options like `--line-number` and `--count` provide additional information.

# VI. Rewriting History

## Git Rebase
- `git rebase <branch>`: Rewrites commit history.
- Squash, edit, or reorder commits interactively.

# VII. Reset Demystified

## Git Reset
- `git reset <commit>`: Unstages changes or moves the branch pointer.
- Options like `--soft`, `--mixed`, and `--hard` control the reset behavior.

# VIII. Advanced Merging

## Git Merge Strategies
- `git merge -s <strategy>`: Utilize different merge strategies.
- Strategies include `recursive`, `octopus`, and `ours`.

# IX. Rerere

## Git Rerere
- `git rerere`: Reuse recorded resolution of conflicted merges.
- Automates conflict resolution based on past resolutions.

# X. Debugging with Git

## Git Bisect
- `git bisect`: Binary search for bugs.
- Identify the commit that introduced a bug.

# XI. Submodules

## Git Submodules
- `git submodule`: Embed external repositories within a repository.
- Useful for managing dependencies.

# XII. Bundling

## Git Bundle
- `git bundle`: Package a repository as a single file.
- Transfer Git data without direct network access.

# XIII. Replace

## Git Replace
- `git replace`: Replace an object with another one.
- Useful for correcting mistakes in the commit history.

# XIV. Credential Storage

## Git Credential Storage
- Configure credential storage for authentication.
- Options include caching, credential managers, and helpers.

# XV. Summary

## Key Takeaways
- Revision selection tools like `git log` and `git show` provide insights into commit history.
- Interactive staging (`git add -p`) allows for granular control over changes.
- Stashing and cleaning tools help manage work in progress.
- Signing commits adds a layer of authentication using GPG.
- Searching with `git grep` enables pattern matching.
- Rewriting history with `git rebase` allows for a cleaner commit history.
- Advanced merging strategies and rerere automate conflict resolution.
- Debugging tools like `git bisect` help identify the source of bugs.
- Submodules manage dependencies, and bundling facilitates data transfer.
- `git replace` corrects mistakes, and credential storage enhances authentication.

---
# 8. Customizing Git
# I. Git Configuration

## Global Configuration
- `git config --global`: Set global configurations.
- Includes user details, default text editor, and color settings.

## Repository Configuration
- `git config`: Set configurations specific to a repository.
- Includes repository-specific user details and custom aliases.

# II. Git Attributes

## Git Attributes Overview
- Define attributes for files in a repository.
- Control line endings, language, and merge strategies.

## .gitattributes File
- Specify attributes in a `.gitattributes` file.
- Applied to files based on patterns and rules.

# III. Git Hooks

## Git Hooks Introduction
- Scripts triggered by specific Git events.
- Located in the `.git/hooks` directory.

## Common Git Hooks
- `pre-commit`: Run before each commit.
- `post-commit`: Run after a commit is made.

# IV. An Example Git-Enforced Policy

## Commit Message Policy
- Enforce a commit message format.
- Use a `pre-commit` hook to check and enforce the policy.

## Implementation Steps
1. Create a `pre-commit` hook script.
2. Define the policy checks in the script.
3. Configure the repository to use the hook.

# V. Summary

## Key Takeaways
- Git configuration is customizable globally and per repository.
- Git attributes allow fine-tuning file behaviors.
- Git hooks enable automation of custom scripts at specific events.
- Examples like commit message policies can be enforced using Git hooks.
- Customization enhances consistency and workflow efficiency in Git.
