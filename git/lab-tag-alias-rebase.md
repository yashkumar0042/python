
### 1. Git Tagging:

#### Question:
1. Create a Git repository named "LabRepo."
2. Initialize the repository with some files and make a few commits.
3. Create a lightweight tag called "v1.0" on the latest commit.
4. Create an annotated tag called "release-v1.1" with a brief description.
5. List all tags in the repository.

#### Answer:
```bash
# Step 1: Create and initialize the repository
git init LabRepo
cd LabRepo

# Step 2: Add files and make commits
touch file1.txt
git add file1.txt
git commit -m "Initial commit"

# Add more files and make additional commits as needed

# Step 3: Create a lightweight tag "v1.0"
git tag v1.0

# Step 4: Create an annotated tag "release-v1.1"
git tag -a release-v1.1 -m "Release version 1.1"

# Step 5: List all tags
git tag
```

### 2. Git Alias:

#### Question:
1. Configure a Git alias named "l" that prints a concise log of the commit history.
2. Test the alias by running `git l` in your repository.
3. Create an alias "s" for "status" and an alias "b" for "branch."
4. Verify that the aliases work as expected.

#### Answer:
```bash
# Step 1: Configure alias "l" for log
git config --global alias.l "log --oneline --graph --all"

# Step 2: Test the "l" alias
git l

# Step 3: Create aliases "s" for "status" and "b" for "branch"
git config --global alias.s "status"
git config --global alias.b "branch"

# Step 4: Verify aliases
git s
git b
```

### 3. Git Rebase:

#### Question:
1. Create a Git repository with two branches, "feature" and "main."
2. Make changes in both branches, commit them, and ensure there are conflicts.
3. Use `git rebase` to reapply the "feature" branch changes onto "main."
4. Resolve any conflicts during the rebase.
5. Verify that the commit history is now a linear progression on the "main" branch.

#### Answer:
```bash
# Step 1: Create repository and branches
git init RebaseLab
cd RebaseLab
git checkout -b feature

# Make changes and commit in the "feature" branch

git checkout -b main

# Make changes and commit in the "main" branch

# Step 2: Create conflicts
# Modify the same file in both branches, then commit in each branch

# Step 3: Rebase "feature" onto "main"
git checkout feature
git rebase main

# Step 4: Resolve conflicts during rebase

# Step 5: Verify linear commit history on "main"
git checkout main
git log --oneline
```
