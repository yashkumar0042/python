### Lab: Distributed Git and GitHub

**Objective:** Learn and practice basic Git and GitHub workflows in a distributed environment.

#### Lab Setup:

1. **Create a GitHub Account:**
   - If you don't have a GitHub account, sign up at [GitHub](https://github.com/).

2. **Install Git:**
   - Install Git on your local machine from [git-scm.com](https://git-scm.com/).

#### Lab 1: Cloning a Repository

**Steps:**

1. **Clone a Repository:**
   - Fork a public repository on GitHub (e.g., a sample repository with a README).
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/your-username/repository.git
     ```

**Question:**
- What is the purpose of forking a repository on GitHub before cloning?

**Answer:**
- Forking creates a personal copy of a repository under your GitHub account. It allows you to freely experiment with changes without affecting the original repository.

---

#### Lab 2: Branching and Making Changes

**Steps:**

1. **Create a New Branch:**
   - Create a new branch for a new feature or bug fix:
     ```bash
     git checkout -b feature-branch
     ```

2. **Make Changes and Commit:**
   - Make changes to a file, add and commit the changes:
     ```bash
     echo "New feature content" >> myfile.txt
     git add myfile.txt
     git commit -m "Add new feature"
     ```

**Question:**
- Why is it advisable to create a new branch for each new feature or bug fix?

**Answer:**
- Creating a new branch isolates changes, allowing for independent development and easy integration through pull requests.

---

#### Lab 3: Pushing Changes to GitHub

**Steps:**

1. **Push Changes to Remote:**
   - Push the changes to your forked repository on GitHub:
     ```bash
     git push origin feature-branch
     ```

**Question:**
- What is the purpose of the `git push` command, and what does `origin` refer to in this context?

**Answer:**
- `git push` is used to upload local branch commits to a remote repository. `origin` is the default name given to the remote repository where you cloned or forked the project.

---

#### Lab 4: Pull Requests and Collaboration

**Steps:**

1. **Create a Pull Request:**
   - Visit your forked repository on GitHub and create a pull request for your feature branch.

2. **Review and Merge:**
   - Request a review, and after approval, merge the pull request.

**Question:**
- What role does a pull request play in the collaborative Git workflow?

**Answer:**
- A pull request is a way to propose changes to a repository and initiate discussion and review before merging changes into the main branch.

---

#### Lab 5: Handling Conflicts

**Steps:**

1. **Create a Conflict:**
   - Make changes to the same line in a file both locally and on GitHub.

2. **Pull Changes and Resolve Conflict:**
   - Attempt to pull changes and resolve conflicts:
     ```bash
     git pull origin main
     ```

**Question:**
- Why does a conflict occur, and how do you resolve it?

**Answer:**
- A conflict occurs when changes made locally and remotely affect the same lines. To resolve, manually edit the conflicted file, choose which changes to keep, and commit the resolution.

---

#### Lab 6: Collaboration with Multiple Contributors

**Steps:**

1. **Invite Collaborators:**
   - Invite another GitHub user as a collaborator on your repository.

2. **Collaborate on a Branch:**
   - Create a branch collaboratively, make changes, and push.

**Question:**
- How does collaborating with multiple contributors in a Git repository enhance teamwork?

**Answer:**
- Collaboration allows team members to work concurrently on different features or bug fixes, fostering parallel development and faster progress.

---

### Conclusion:

By completing these labs, you should have a good understanding of distributed Git workflows, collaboration using GitHub, handling branches, and resolving conflicts. Experiment further with Git and GitHub to reinforce these concepts.
