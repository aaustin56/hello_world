# hello_world

## Overview

The purpose of this project is to demonstrate how we can follow the multi-step process of collaborative software development using Git.

## References

Here is a list of references that you can keep handy for remember what commands are available for Git or the terminal.

Information on Git

https://git-scm.com/doc

Here's a quick list of commands:

```
# clone a repository from github to your local computer
git clone [repository_path]

# check the status of your local git repository
git status

# list existing branches
git branch

# create a new branch
git branch [branch_name]

# checkout an existing branch
git checkout [branch_name]

# checkout an existing branch, creating it if it does not exist
git checkout -b [branch_name]

# add an untracked file (for example a newly created one) to your branch
git add [path_to_file_name]

# commit all existing changes to your branch
git commit -a -m 'message'

# push all commits on your local branch to Github
git push https://[personal-access-token]@github.com/[github_user_name]/[path_to_repository]`

# display differences from your existing saved files and the last commit
git diff

# pull the latest from Github to your local git repository
git pull
```

A Git Cheatsheet

https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet


Information on linux terminal commands

https://community.linuxmint.com/tutorial/view/244


## A Complete Pull Request


The steps for all this include the following:

*1. (in the terminal) Clone the repo to your local computer.*

Make sure to navigate to the appropriate base directory where you want to store all your local (on your computer) code.

`git clone https://github.com/aaustin56/hello_world`

Cloning your repository will copy it to your local computer.  From there you can work on creating new branches, updating your code with commits, push those branch back to git, and eventually merging them.

2. (in the terminal) Create a new branch for your changes.

`git branch my-new-branch`

Two notes to mention:

Branch names generally are lower case with dashes '-' used as spaces between words.

Name your branch something descriptive.  For example:

	`updating-readme`
	`fixing-print-bug`
	'updating-logging`
	`adding-browse-products-feature`

3. (in your terminal) Checkout the new branch.

`git checkout my-new-branch`

Note: We can combine steps 2 and 3 into one command:

`git checkout -b my-new-branch`

Which will create a new branch if necessary and check it out.

4. (in your source code editor) Make changes to your code on this new branch.

This can include editing existing files as well as creating new files for new code, documention, etc.

If you have to create new files, be sure to add them with `git add`.

5. (in your terminal) Look at changes in our local branch.

`git diff`

Make sure the changes make sense.  You can also look at them in github which is easier on the eyes.

6. (in your terminal) Commit changes to local branch.

`git commit -a -m 'Updating documentation'`

Make sure to add a descriptive and useful message.

7. (in your terminal) Push changes on new branch to github

`git push https://[personal-access-token]@github.com/aaustin56/hello_world`

Note: Creating a personal access token can be done here:

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Also:

https://techglimpse.com/git-push-github-token-based-passwordless/

8. (in github) Create a new pull request (PR) on github.com

9. (in github) Wait for PR approval from other teammates.

Other developers may have comments on your PR.  Address them by either pushing back (argue with them!) or implement their suggested changes.

10. (in github) Merge PR after approval.  Delete branch no longer in use.

11. (in your terminal) Update all local main branches.


Note on rebase:

There is a situation where main gets updated via a PR merge, and now existing local branches of other developers are out of sync with what's in the Github main.

In this case, those developers should:

	1.) switch to main in local
	2.) pull latest
	3.) switch to their branch
	4.) `git rebase main`
		There may be merge conflicts which you'll have to resolve.