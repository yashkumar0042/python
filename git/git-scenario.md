
**1. **Scenario: You made changes in your local branch but want to discard them and get the latest changes from the remote branch.**
   - Solution:
     ```
     git fetch origin
     git reset --hard origin/your_branch
     ```

**2. **Scenario: You accidentally committed sensitive information. How do you remove the last commit without losing the changes?**
   - Solution:
     ```
     git reset HEAD^
     git stash
     # Manually remove sensitive info from working directory
     git stash apply
     ```

**3. **Scenario: You have multiple commits, and you want to combine them into a single commit.**
   - Solution:
     ```
     git rebase -i HEAD~n
     # In the interactive rebase, squash or fixup the commits as needed
     ```

**4. **Scenario: You want to create a new branch and switch to it in one command.**
   - Solution:
     ```
     git checkout -b new_branch
     ```

**5. **Scenario: You want to see the changes introduced by a specific commit.**
   - Solution:
     ```
     git show commit_hash
     ```

**6. **Scenario: You have a feature branch, and you want to merge it into the main branch, preserving a clear history.**
   - Solution:
     ```
     git checkout main
     git merge --no-ff feature_branch
     ```

**7. **Scenario: You want to undo the last commit but keep the changes in your working directory.**
   - Solution:
     ```
     git reset --soft HEAD^
     ```

**8. **Scenario: You have multiple branches, and you want to list them along with their last commit messages.**
   - Solution:
     ```
     git branch -v
     ```

**9. **Scenario: You want to discard changes in your working directory for a specific file.**
   - Solution:
     ```
     git checkout -- file_name
     ```

**10. **Scenario: You want to rename a local and remote branch.**
    - Solution:
      ```
      git branch -m new_branch_name
      git push origin :old_branch_name new_branch_name
      git push origin -u new_branch_name
      ```
