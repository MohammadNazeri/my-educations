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
## git tag
* git tag >  shows all tags
* git tag -a v2.0 -m 'message' > assign a tag to do version. 
* git push origin --tags > push all new tags to the server
* git checkout [tag] > Switch the working directory to the state of the repository at the time when the "v1.0" tag was created. This can be useful for reviewing code at a specific release version or for creating a new branch based on a tagged release.
## git key
* gpg --gen-key > generate key with giving name and email
* gpg --list-keys > shows all keys (public)
* gpg --list-secret-keys --keyid-format LONG > shows my private keys
* git config --global user.name > name
* git config --global user.signingkey > shows current private key (global means in all repositories in my computer)
* git config --global user.signingkey [new private key]
* git tag -s v2.1 -m 'message' > assign tag and sign
* git show v2.1 > shows the encrypted message
* git tag -v v2.1 > verify the encrypted message
* git commit -S -m 'message' >  commit and sign
## git debug
* git blame [filename] -L[line number] > shows history of line number > When a bug is found in a line you can track the modification and find out who changed it
* binary search commit:
1. git bisect start >  strat binary search commits
2. git bisect bad >  tells that now the situation is bad and there is bug
3. git bisect good [commit unique number] > tells that that commit is without bug > git log shows commit unique number
* After that git switches to a different commit and you should run and check the project > if there is a bug "git bisect bad" else "git bisect good" > finally will tell you where the bug is.
