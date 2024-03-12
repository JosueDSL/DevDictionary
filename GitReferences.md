# Git References
Welcome to the basic git workflow:
![Basic Workflow](./media/Git/git%20workflow_fullwidth.svg)

## git init 
`git init` creates a new Git repository

## git status
`git status` inspects the contents of the working directory and staging area

## git add --all
`git add` adds files from the working directory to the staging area

## git diff 
`git diff` shows the difference between the working directory and the staging area

## git commit -m
`git commit` permanently stores file changes from the staging area in the repository

`git commit --amend` To avoid creating a new commit, you could create your changes, stage them with `git add` and then type the command `git commit --amend` to update your previous commit.

## git log
`git log` shows a list of all previous commits
`git log --oneline` shows the list of commits in one line format.
`git log --oneline --graph` Displays a visual representation of how the branches and commits were created

## git checkout HEAD filename
`git checkout HEAD filename` Discards changes in the working directory.
Shortcut: `git checkout -- filename`

## git reset HEAD filename
`git reset HEAD filename` Unstages file changes in the staging area.

## git reset commit_SHA
`git reset commit_SHA` Resets to a previous commit in your commit history.

## git push
Push your commits to the current branch

## git branch
You can use the command above to answer the question: “which branch am I on?” `git branch` will be the answer

### New branch
To create a new branch use:
```bash
git branch new_branch   
```
Then you would need to use: `git checkout branch_name` to switch to a new branch

## git checkout -b branch-name
It will create a new branch and immediatly switch to it. It's a shortcut for creating a new branch and checking it out in one step.

Make sure you are no longer in git log,

## Delete branch
The command
```bash
git branch -d branch_name
```
will delete the specified branch from your git project `-d`

If the features where never merged into master use `-D`

## Workflow for Git Collaborations
The workflow for Git collaborations typically follows this order:
0. Cloning the remote - One time Step

1. Fetch and merge changes from the remote
2. Create a branch to work on a new project feature
3. Develop the feature on your branch and commit your work
4. Fetch and merge from the remote again (in case new commits were made while you were working)
5. Push your branch up to the remote for review

Steps 1 and 4 are a safeguard against merge conflicts, which occur when two branches contain file changes that cannot be merged with the `git merge` command.

## git clone
Creates a local copy of a remote.

## git remote -v
List a Git project's remotes

## git fetch
Fetches work from the remote into the local copy.

## git merge origin/master: 
Merges origin/master into your local branch.

## git push origin <branch_name>: 
Pushes a local branch to the origin remote.
`git push origin <branch_name>`

## Pull Request Structure – What, Why, and How?

## git stash 
While working on a file, you find a small bug in a separate file from a previous commit that needs to be fixed before you continue.
```bash
$ git stash
```
Running the command above will store your work temporarily for later use in a hidden directory.

At this point, you can switch branches and do work elsewhere.

Once the bug is fixed, you want to retrieve the code you were working on previously, you can “pop” the work that was stored when you used git stash.
```bash
$ git stash pop
```
From here, you can continue your work and commit it when ready.

## git alias commands:
Below are a couple of examples:
```bash
$ git config --global alias.co "checkout"
$ git config --global alias.br "branch"
$ git config --global alias.glop "log --pretty=format:"%h %s" --graph"
```
Once the aliases are configured, next time you want to check out to another branch you could type the command:
`$ git co example_branch`
