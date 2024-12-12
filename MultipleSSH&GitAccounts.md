# Setting Up Multiple Git and SSH Accounts for Personal and Work Use

This guide demonstrates how to configure multiple Git and SSH accounts (e.g., GitHub personal and Azure work) and troubleshoot common issues. 

Follow the steps below:

---

## 1. **Generate SSH Keys for Each Account**

Generate separate SSH keys for personal and work accounts.

### Personal GitHub Key
```bash
ssh-keygen -t rsa -b 4096 -C "your_personal_email@example.com" -f ~/.ssh/id_rsa_github_personal
```

## Work Azure Key

```bash
ssh-keygen -t rsa -b 4096 -C "your_work_email@example.com" -f ~/.ssh/id_rsa_work_azure

```

## 2. Add SSH Keys to SSH Agent

Add both keys to the SSH agent.

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa_github_personal
ssh-add ~/.ssh/id_rsa_work_azure
```

## 3. Add SSH Keys to Your Git Services

- Add Personal development SSH Key to GitHub

    - Copy the key for personal development: `cat ~/.ssh/id_rsa_github_personal.pub`
    - Go to GitHub > Settings > SSH and GPG Keys > New SSH Key, paste the key, and save.

- Add Work SSH Key to Azure DevOps

    - Copy the work key:  `cat ~/.ssh/id_rsa_work_azure.pub`

    - Go to Azure DevOps > User Settings > SSH Public Keys > Add, paste the key, and save.

## 4. Configure SSH ~/.ssh/config File

- Edit the SSH configuration file:  `nano ~/.ssh/config`

- Add the following entries:
```ssh
# Work: Azure Repos
Host azure-work
    HostName ssh.dev.azure.com
    User git
    IdentityFile ~/.ssh/id_rsa_work_azure

# Personal: GitHub
Host github-personal
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_personal_github
```

- Save and exit.

## 5. Test SSH Connections

Test each account's SSH connection:

**Personal GitHub**

`ssh -T github-personal`

Expected Output:

Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.

**Work Azure**

`ssh -T azure-work`

Expected Output:

remote: Shell access is not supported.

## 6. Clone Repositories Using SSH Aliases
Clone Personal Repository

- `git clone github-personal:username/repository.git`

Clone Work Repository

- `git clone azure-work:v3/organization/project/repository`

## 7. Troubleshooting
Check Remote Configuration

Ensure the remote URL uses the correct SSH alias:

`git remote -v`

The output should show have the following format:
```bash
> git remote -v
# Generic structure for Azure DevOps:
origin  azute-work:v3/organization/project/repository (fetch)
origin  azure-work:v3/organization/project/repository (push)
-------------------^ # Note the version v3 and organization path here
...

# Generic structure for GitHub:
origin  github-personal:username/repository.git (fetch)
origin  github-personal:username/repository.git (push)
```

If it does not, update the URL:

`git remote set-url origin <ssh-alias>:<repo-path>`

Add SSH Key to Agent if Not Loaded
```bash
ssh-add ~/.ssh/id_rsa_github_personal
ssh-add ~/.ssh/id_rsa_work_azure
```

- (optional) Debug with Verbose SSH

GIT_SSH_COMMAND="ssh -v" git pull

Look for lines mentioning identity file to confirm the correct key is being used.

## 8. Configure Git User Information Per Repository

Set Git user details for each repository to avoid conflicts:

- Personal Repository
```bash
git config user.name "Your Personal Name"
git config user.email "your_personal_email@example.com"
```

- Work Repository
```bash
git config user.name "Your Work Name"
git config user.email "your_work_email@example.com"
```

## 9. Summary of Commands

### Generate SSH Keys

For each account, generate separate SSH keys:
```bash
ssh-keygen -t rsa -b 4096 -C "<email>" -f ~/.ssh/id_rsa_<identifier>
```

### Add SSH Keys to Agent

Start the SSH agent and add the keys:
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa_<identifier>
```

2. Edit ~/.ssh/config
```bash
Host <alias>
    HostName <hostname>
    User git
    IdentityFile ~/.ssh/id_rsa_<identifier>
```

### Copy SSH Public Key

Retrieve the public key to add it to the respective service:
```bash
cat ~/.ssh/id_rsa_<identifier>.pub
```

### Edit SSH Config

Open the ~/.ssh/config file and add entries for each account:
```bash
Host <alias>
    HostName <hostname>
    User git
    IdentityFile ~/.ssh/id_rsa_<identifier>
```
### Test SSH Connection

Verify the connection with each alias:
```bash
ssh -T <alias>
```

### Clone Repositories

Use the SSH alias to clone repositories:
```bash
git clone <alias>:<repo-path>
```

### Update the Repo Remote URL
Check the remote configuration:
```bash
git remote -v

<!-- The output should look as follows: -->
# Generic structure for Azure DevOps:
origin  <ssh-alias>/organization/project/repository (fetch)
# E.g.,
origin  azute-work:v3/organization/project/repository (fetch)
origin  azure-work:v3/organization/project/repository (push)
...

# Generic structure for GitHub:
origin  <ssh-alias>:username/repository.git (fetch)
# E.g.,
origin  github-personal:username/repository.git (fetch)
origin  github-personal:username/repository.git (push)
```

If needed, update the remote URL:
```bash
git remote set-url origin <ssh-alias>:<repo-path>

# For Azure DevOps:
git remote set-url origin <ssh-alias>:v3/organization/project/repository
                         -------------^ # Note the version v3 and organization path here
# E.g.,
git remote set-url origin azure-work:v3/organization/project/repository

# For GitHub:
git remote set-url origin <ssh-alias>:username/repository.git
# E.g.,
git remote set-url origin github-personal:username/repository.git
```
### Configure Git User Information
Set Git user details for **EACH** repository:
```bash
git config user.name "Your Name"
git config user.email "your_email@example.com"
```