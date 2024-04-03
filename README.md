# git
## git commands:
* git init > run it inside a project folder > initialization
* git status > show modification on files
* git add [filename] > 1. to add new files to track on git 2. to stage changes made to "filename" for the next commit. (steps: modification>stage>commit)
* git commit -m 'message' > to commit modification
* git log > show log of commits
* git diff HEAD > shows the differences between the working directory and the last commit (HEAD) in the current branch.
* git diff --staged > shows the difference between the working directory and the staged files
* git reset [filename] > to unstage the filename
* git checkout -- [filename] > recover filename to last version
## git branch
* git branch > show the branches
* git branch [newbranch] >  Create new branch from master
* git checkout [newbranch] > go to new branch
* git merge [newbranch] > merge new branch into master
* gir rm [filename] >  remove file from git and system
* git branch -d [newbranch] > remove new branch
## git remote
* git clone [gitlink.git] > clone the git > the name will be origin with branches
* git push origin master > upload
* git pull origin master > download
* git remote >  shows remotes
* git remote add [remotename] [repository link] > add new remote for pull and push with a name like origin
* git remote -v > shows remote names with their links for pull and push
* Conflict: changing a file (specially the same line) in the same repository through two people locally and then pushing it to the server > it will be rejected > it suggests what you should do > 1. git pull 2. git tries to automerge otherwise you should do it > push it
* 
