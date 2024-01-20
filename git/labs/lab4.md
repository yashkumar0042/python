### Lab 4: Remote Repositories

**Objective:** Work with remote repositories.

1. **Step 1: Create a Remote Repository**
   - Create a new repository on GitHub or GitLab.
   - Follow the instructions to add the remote repository as a remote named `origin`.

2. **Step 2: Push Changes to Remote**
   - Push your local repository to the remote repository.
   - Run the following commands:
     ```bash
     git remote add origin <remote-repository-url>
     git branch -M main
     git push -u origin main
     ```

**Question:**
- What is the purpose of the `-u` option in the `git push` command?

**Answer:**
- The `-u` option sets up tracking between the local branch and the remote branch. After using `-u`, subsequent pushes and pulls can be done without specifying the remote and branch.

---

