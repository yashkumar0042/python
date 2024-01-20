### Lab 2: Branching and Merging

**Objective:** Create and merge branches.

1. **Step 1: Create a New Branch**
   - Run the following commands:
     ```bash
     git branch feature-branch
     git checkout feature-branch
     ```

2. **Step 2: Make Changes in the New Branch**
   - Make changes to the README.md file.
   - Run the following commands:
     ```bash
     echo "This is a new feature." >> README.md
     git add README.md
     git commit -m "Add feature"
     ```

3. **Step 3: Merge Changes into Main Branch**
   - Run the following commands:
     ```bash
     git checkout main
     git merge feature-branch
     ```

**Question:**
- Why do we create a new branch for a new feature instead of directly making changes in the main branch?

**Answer:**
- Creating a new branch allows developers to work on new features or bug fixes without affecting the main branch. It provides isolation and enables changes to be reviewed and tested independently before merging into the main branch.

---

