Connecting Git with GitHub involves several steps, including setting up a GitHub account, configuring Git with your credentials, and creating a new repository on GitHub. Here are detailed steps for a new user:

### 1. Create a GitHub Account:

If you don't have a GitHub account, go to [GitHub](https://github.com/) and sign up for a new account. Follow the instructions to complete the registration process.

### 2. Install Git:

If Git is not installed on your computer, download and install it from the official Git website: [Git Downloads](https://git-scm.com/downloads)

### 3. Configure Git with Your GitHub Credentials:

Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux) and set your Git username and email. Use the same email address associated with your GitHub account.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### 4. Generate SSH Key (Optional, but Recommended):

Generating an SSH key allows you to securely authenticate with GitHub without entering your username and password every time. Skip this step if you prefer to use HTTPS for authentication.

```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

Follow the instructions and provide a passphrase if you want additional security.

### 5. Add SSH Key to SSH Agent (Optional, but Recommended):

If you generated an SSH key, add it to the SSH agent to manage your keys.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

### 6. Add SSH Key to GitHub Account:

Copy the SSH key to your clipboard.

```bash
cat ~/.ssh/id_rsa.pub
```

Go to your GitHub account, click on your profile picture, and select "Settings." Then, go to "SSH and GPG keys" and click "New SSH key." Paste the copied key into the "Key" field and add a descriptive title.

### 7. Create a New Repository on GitHub:

On the GitHub website, click the "+" button in the top right corner and select "New repository." Follow the instructions to create a new repository, and optionally, initialize it with a README file.

### 8. Clone the Repository to Your Local Machine:

Copy the repository URL from GitHub and clone it to your local machine.

```bash
git clone git@github.com:your-username/your-repository.git
```

Replace `your-username` with your GitHub username and `your-repository` with the repository name.

### 9. Make Changes Locally:

Navigate into the cloned repository and make changes to the files. Add new files, modify existing ones, etc.

```bash
cd your-repository
```

### 10. Commit Changes:

Commit your changes to the local repository.

```bash
git add .
git commit -m "Your commit message"
```

### 11. Push Changes to GitHub:

Push your changes to the GitHub repository.

```bash
git push origin main
```

Replace `main` with the name of your branch if it's different.

Congratulations! You have successfully connected Git with GitHub and created a new repository. You can now continue working with Git, making changes, committing, and pushing them to your GitHub repository.
