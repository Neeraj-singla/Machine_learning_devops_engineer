git pull
git checkout main
git checkout -b python_branch 
git branch
git checkout main
git checkout -b markdown_branch
git checkout main
git branch -d python_branch
git branch -d markdown_branch


Git commands used in this solution:

Create a new branch and move to it.
`git checkout -b 'branch_name'`
List the created branches available on your local.
`git branch`
Change between branches.
`git checkout branch_to_change_to`
Delete branches.
`git branch -d branch_name_to_delete`
Note: In order to delete a branch, you must first move off the branch you would like to delete.