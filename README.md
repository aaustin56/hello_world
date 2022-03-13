# hello_world

The purpose of this project is to demonstrate how we can follow the multi-step process of collaborative software development.

The steps for all this include the following:

1. Clone the repo to your local computer.

`git clone https://github.com/aaustin56/hello_world`

Cloning your repository will copy it to your local computer.  From there you can work on creating new branches, updating your code with commits, push those branch back to git, and eventually merging them.

2. On local, create a new branch for your changes.

`git branch my-new-branch`

Two notes to mention:

Branch names generally are lower case with dashes '-' used as spaces between words.

Name your branch something descriptive.  For example:

	`updating-readme`
	`fixing-print-bug`
	'updating-logging`
	`adding-browse-products-feature`

3. Checkout the new branch.

`git checkout my-new-branch`

Note: We can combine steps 2 and 3 into one command:

`git checkout -b my-new-branch`

Which will create a new branch if necessary and check it out.

4. Make changes to your code on this new branch.

This can include editing existing files as well as creating new files for new code, documention, etc.

If you have to create new files, be sure to add them with `git add`.

5. Look at changes in our local branch.

`git diff`

Make sure the changes make sense.  You can also look at them in github which is easier on the eyes.

6. Commit changes to local branch.

`git commit -a -m 'Updating documentation'`

Make sure to add a descriptive and useful message.

7. Push changes on new branch to github

`git push https://<personal-access-token>@github.com/aaustin56/hello_world`

Note: Creating a personal access token can be done here:

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Also:

https://techglimpse.com/git-push-github-token-based-passwordless/

8. Create a new pull request (PR) on github.com

9. Wait for PR approval from other teammates.

Other developers may have comments on your PR.  Address them by either pushing back (argue with them!) or implement their suggested changes.

10. Merge PR after approval.  Delete branch no longer in use.

11. Update all local main branches.


Note on rebase:

There is a situation where main gets updated via a PR merge, and now existing local branches of other developers are out of sync with what's in the Github main.

In this case, those developers should:

	1.) switch to main in local
	2.) pull latest
	3.) switch to their branch
	4.) `git rebase`
		There may be merge conflicts which you'll have to resolve.