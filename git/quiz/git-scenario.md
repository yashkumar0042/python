
### Scenario 1: Resolving Merge Conflict

**Question:**
You're working on a feature branch, and when you try to merge it into the main branch, you encounter a merge conflict. How do you resolve the conflict?

**Answer:**
1. Use `git status` to identify conflicted files.
2. Open conflicted files, resolve conflicts manually.
3. Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
4. Use `git add <conflicted-file>` to stage the resolved file.
5. Complete the merge with `git merge --continue`.

### Scenario 2: Undoing the Last Commit

**Question:**
You accidentally committed and pushed changes to the main branch. How do you undo the last commit without affecting the working directory?

**Answer:**
1. Use `git reset --soft HEAD^` to undo the last commit while keeping changes staged.
2. Optionally, modify files as needed.
3. Commit the changes with a new message using `git commit -c ORIG_HEAD`.
4. Push the corrected commit.

### Scenario 3: Creating a Feature Branch

**Question:**
You need to work on a new feature. How do you create a new feature branch based on the latest main branch?

**Answer:**
1. Ensure you are on the main branch with `git checkout main`.
2. Update the main branch with `git pull origin main`.
3. Create a new feature branch with `git checkout -b feature-branch`.

### Scenario 4: Merging with a Specific Commit

**Question:**
You want to merge a specific commit from a feature branch into the main branch. How do you do this?

**Answer:**
1. Identify the commit hash using `git log`.
2. Switch to the main branch with `git checkout main`.
3. Cherry-pick the commit with `git cherry-pick <commit-hash>`.

### Scenario 5: Handling Large Files

**Question:**
Your repository contains large files that you want to remove from version control. How do you clean up the repository and prevent these files from being tracked?

**Answer:**
1. Add the large files or directories to the `.gitignore` file.
2. Use `git rm --cached <file>` to untrack the files.
3. Commit the changes and push them.
4. If files were already committed, use `git filter-branch` or `git filter-repo` to rewrite history.
