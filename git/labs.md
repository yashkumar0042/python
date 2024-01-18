Certainly! Here are the 10 Git labs with more detailed instructions and examples:

### Lab 1: Setting Up Git
#### Objective:
Set up Git on your local machine.

1. **Instructions:**
   - Install Git on your computer.
     - Example for Linux: `sudo apt-get install git`
     - Example for macOS: `brew install git`
     - Example for Windows: Download and install from [Git website](https://git-scm.com/download/win)
   - Configure your username and email:
     - `git config --global user.name "Your Name"`
     - `git config --global user.email "your.email@example.com"`

### Lab 2: Creating a Repository
#### Objective:
Create a new Git repository.

2. **Instructions:**
   - Create a new directory.
     - Example: `mkdir my_project`
   - Initialize a Git repository in that directory:
     - `cd my_project`
     - `git init`
   - Create a file, add content, and commit it:
     - `touch myfile.txt`
     - `git add myfile.txt`
     - `git commit -m "Initial commit"`

### Lab 3: Cloning a Repository
#### Objective:
Clone an existing Git repository.

3. **Instructions:**
   - Find a repository on GitHub (e.g., `https://github.com/example/repo.git`).
   - Clone the repository to your local machine:
     - `git clone https://github.com/example/repo.git`

### Lab 4: Branching
#### Objective:
Understand and practice branching in Git.

4. **Instructions:**
   - Create a new branch:
     - `git branch feature_branch`
   - Switch to the new branch:
     - `git checkout feature_branch` (or `git switch feature_branch`)
   - Make changes, add, and commit:
     - `git add .`
     - `git commit -m "Add feature"`

### Lab 5: Merging
#### Objective:
Learn different ways of merging branches.

5. **Instructions:**
   - Merge branches:
     - Switch to the branch you want to merge into (e.g., `main`): `git checkout main`
     - `git merge feature_branch`
   - Resolve conflicts if needed.

### Lab 6: Remote Repositories
#### Objective:
Work with remote repositories.

6. **Instructions:**
   - Add a remote repository:
     - `git remote add origin https://github.com/example/repo.git`
   - Push changes to a remote repository:
     - `git push -u origin main`
   - Fetch changes from a remote repository:
     - `git fetch origin`

### Lab 7: Pull Requests
#### Objective:
Create and manage pull requests.

7. **Instructions:**
   - Fork a repository on GitHub.
   - Clone your fork to your local machine.
   - Create a branch, make changes, and push the branch.
   - Create a pull request on GitHub.

### Lab 8: Gitignore
#### Objective:
Utilize .gitignore to exclude files from version control.

8. **Instructions:**
   - Create a .gitignore file:
     - `touch .gitignore`
   - Edit .gitignore and add files/patterns to be ignored.

### Lab 9: Reverting Changes
#### Objective:
Practice reverting changes in Git.

9. **Instructions:**
   - Create a commit with changes.
   - Use `git revert` to undo the changes:
     - `git revert <commit_sha>`

### Lab 10: Tagging
#### Objective:
Tag specific points in your Git history.

10. **Instructions:**
    - Tag a specific commit:
      - `git tag -a v1.0 -m "Release v1.0" <commit_sha>`
    - Push tags to a remote repository:
      - `git push --tags`

These detailed instructions and examples should help users to perform Git activities effectively in a hands-on manner.
