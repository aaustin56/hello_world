# hello_world

The purpose of this project is to demonstrate how we can follow the multi-step process of collaborative software development.

The steps for all this include the following:

1. Clone the repo to your local computer.

`git clone https://github.com/aaustin56/hello_world`

2. On local, create a new branch for your changes.

`git branch my-new-branch`

3. Checkout the new branch.

`git checkout my-new-branch`

4. Make changes to your code on this new branch.

This can include editing existing files as well as creating new files for new code, documention, etc.

5. Look at changes in our local branch.

`git diff`

6. Commit changes to local branch.

`git commit -a -m 'Updating documentation'`

7. Push changes on new branch to github

`git push https://<personal-access-token>@github.com/aaustin56/hello_world`

Note: Creating a personal access token can be done here:

https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Also:

https://techglimpse.com/git-push-github-token-based-passwordless/

8. Create a new pull request (PR) on github.com

9. Wait for PR approval from other teammates.

10. Merge PR after approval.  Delete branch no longer in use.

11. Update all local main branches.
