# hello_world

## Overview

The purpose of this project is to demonstrate how we can follow the multi-step process of collaborative software development using Git.


## What is Git?

Git is a version control system that allows multiple developers to work on a single code base.  More detailed descriptions and documentation can be found here:

[Git Source Control Management](https://git-scm.com/)

## What is Github?

Github is a cloud-based code store where users can store their code and work together to collaborate on creating software.

If you can read this, you're probably already here!

## Your Environment

When you begin to code, you basically always want to have three things running where you'll be working:

**1.) Local Editor / Integrated Development Environment**

> This is where you will be editing code that exists on your computer.  Code can be written and edited in any editor, but special, programmer-specific editors are called Integrated Development Environments (IDE).
>
> Use your favorite editor on your computer to edit code for your projects.
>
> A popular general-purpose editor is SublimeText.
>
> [SublimeText download site](https://www.sublimetext.com/download)
>
> If you're coding in Python, the Pycharm IDE is very popular.
>
> [Pycharm download site](https://www.jetbrains.com/pycharm/download/)
>
> If you're coding in Java, the Eclipse IDE is very popular.
>
> [Eclipse download site](https://www.eclipse.org/downloads/)
>
> For now we will use SublimeText because using Pycharm and Eclipse is very complicated for our examples, but later we may use them.

**2.) Terminal**

>The terminal is a text-based command prompt where you can input commands which are executed by your computer.
>
>A quick introduction to using the terminal can be found here:
>
>[Terminal Tutorial](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
>
>You will be working extensively with the Terminal.  In Linux you can find it in your applications menu (press the windows key) and type in `terminal`.
>
>The terminal is where you will execute `git` commands which do the work of managing your software you're writing between your local computer and Github.

**3.) Github**

>This is the online interface where our shared repository is stored.
>
>Here we do things like manage pull requests, do code reviews, merge code, manage repos etc.  This is the place where all individual developers' code meets to a common standard.

## A Complete Pull Request

The steps for all this include the following:

**1. (in the terminal) Clone the repo to your local computer.**

Make sure to navigate to the appropriate base directory where you want to store all your local (on your computer) code.

`git clone https://github.com/aaustin56/hello_world`

Cloning your repository will copy it to your local computer.  From there you can work on creating new branches, updating your code with commits, push those branch back to git, and eventually merging them.

**2. (in the terminal) Create a new branch for your changes.**

`git branch my-new-branch`

Two notes to mention:

Branch names generally are lower case with dashes '-' used as spaces between words.

Name your branch something descriptive.  For example:

	`updating-readme`
	`fixing-print-bug`
	'updating-logging`
	`adding-browse-products-feature`

**3. (in your terminal) Checkout the new branch.**

`git checkout my-new-branch`

Note: We can combine steps 2 and 3 into one command:

`git checkout -b my-new-branch`

Which will create a new branch if necessary and check it out.

**4. (in your source code editor) Make changes to your code on this new branch.**

This can include editing existing files as well as creating new files for new code, documention, etc.

If you have to create new files, be sure to add them with `git add`.

**5. (in your terminal) Look at changes in our local branch.**

`git diff`

Make sure the changes make sense.  You can also look at them in github which is easier on the eyes.

**6. (in your terminal) Commit changes to local branch.**

`git commit -a -m 'Updating documentation'`

Make sure to add a descriptive and useful message.

**7. (in your terminal) Push changes on new branch to github**

`git push https://[personal-access-token]@github.com/aaustin56/hello_world`

Note: Creating a personal access token can be done here:

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Also:

https://techglimpse.com/git-push-github-token-based-passwordless/

**8. (in github) Create a new pull request (PR) on github.com**

Visit github.com and create a new pull request.

If you've recently pushed a new branch to github there should be a green button near the top of the code-view's file listings for creating a new pull request.

Otherwise you can find it by clicking on the `Pull requests` tab.

Be sure to assign reviewers who will be required to approve your pull request.

Fill out a nice detailed description explaining what you hope to accomplish with your pull request.

**9. (in github) Wait for PR approval from other teammates.**

Other developers may have comments on your PR.  Address them by either pushing back (argue with them!) or implement their suggested changes.

**10. (in github) Merge PR after approval.  Delete branch no longer in use.**

Now that your PR has been approved, either merge it yourself or have the reviewer merge it.  Generally it's good practice to have the PR writer merge it in case they have any last-minute ticky-tack changes they want to make to the PR before merging.

**11. (in your terminal) Update all local main branches.**

Back at your terminal, `git checkout main` to switch to your main branch, and `git pull` to update from Github's now updated `main` branch to your local `main` branch.

Congratulations!  Now you've gone through the entire pull request process and merged code into an existing repository in Github!

Note on rebase:

There is a situation where main gets updated via a PR merge, and now existing local branches of other developers are out of sync with what's in the Github main.

In this case, those developers should:

	1.) switch to main in local
	2.) pull latest
	3.) switch to their branch
	4.) `git rebase main`
		There may be merge conflicts which you'll have to resolve.

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
