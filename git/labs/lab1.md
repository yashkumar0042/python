
### Lab 1: Initializing a Repository and Making Commits

**Objective:** Create a new Git repository, make changes, and commit them.

1. **Step 1: Create a New Repository**
   - Open a terminal and navigate to the directory where you want to create the repository.
   - Run the following commands:
     ```bash
     mkdir my-git-repo
     cd my-git-repo
     git init
     ```

2. **Step 2: Create a File and Make Initial Commit**
   - Create a new file (e.g., `README.md`) and add some content.
   - Run the following commands:
     ```bash
     echo "# My Git Repository" > README.md
     git add README.md
     git commit -m "Initial commit"
     ```

**Question:**
- Why is it essential to use the `git add` command before committing changes?

**Answer:**
- The `git add` command stages changes for the next commit. It tells Git which changes you want to include in the next commit. Without this step, the changes won't be part of the commit.

---

