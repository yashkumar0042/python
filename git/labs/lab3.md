### Lab 3: Handling Conflicts

**Objective:** Experience and resolve merge conflicts.

1. **Step 1: Create Conflicting Changes in Two Branches**
   - Create a new branch (`conflict-branch`) from main.
   - Modify the same line in README.md in both feature-branch and conflict-branch.
   - Commit changes in conflict-branch and merge it back into main.

2. **Step 2: Resolve Conflicts**
   - Git will indicate a conflict. Manually edit the conflicted file, resolving differences.
   - Run the following commands:
     ```bash
     git add README.md
     git commit -m "Resolve conflicts"
     ```

**Question:**
- Why does Git require manual conflict resolution, and what is the purpose of conflict markers?

**Answer:**
- Git requires manual resolution to ensure that conflicting changes are reconciled correctly. Conflict markers (`<<<<<<<`, `=======`, and `>>>>>>>`) highlight the conflicting sections, allowing the developer to choose which changes to keep.

---

