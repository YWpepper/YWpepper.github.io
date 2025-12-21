---
title: 'How_to_useGit'
lang: zh-CN
date: 2024-02-07
author: pepper
# permalink: /posts/2024/02/how_to_use_ubuntu/
toc: true
pinned: false
tags:
  - Server
  - Command
---


# Git note[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#git-note "Permanent link")

-   图解 [https://marklodato.github.io/visual-git-guide/index-zh-cn.html](https://marklodato.github.io/visual-git-guide/index-zh-cn.html) 利用图示讲解了 `checkout, reset, merge, cherry-pick, rebase` 等指令到底做了什么，可惜没有涉及到远程仓库的命令。Cheatsheet 性质的 👍
-   Git Pro ebook: [http://iissnan.com/progit/](http://iissnan.com/progit/) 写得非常详细，图示也很赞
    
    -   看了其中的远程分支和 [分支的rebase](http://iissnan.com/progit/html/zh/ch3_6.html) 章节，才算懂了 rebase 的使用。
-   来自廖雪峰的 [Git教程](https://www.liaoxuefeng.com/wiki/896043488029600)；
    
-   另外，官方还有个中文的文档，写得很细 [https://git-scm.com/book/zh/v2](https://git-scm.com/book/zh/v2)
-   廖雪峰老师推荐的一张 [Cheatsheet](https://gitee.com/liaoxuefeng/learn-java/raw/master/teach/git-cheatsheet.pdf)；
-   再推荐一篇进阶的文章 [你可能不知道的 Git](https://blog.daraw.cn/2019/12/21/you-dont-know-git/)；

[Oh Shit, Git!?!](https://ohshitgit.com/zh)

![](https://lightblues.github.io/techNotes/code/CS/media/git-note/16348994455801.jpg)

-   Workspace：工作区
-   Index / Stage：暂存区
-   Repository：仓库区（或本地仓库）
-   Remote：远程仓库

工作流程

1.  将远程仓库克隆为本地仓库 git clone ssh://git@git.sankuai.com/dapp/poi\_search\_rerank.git
2.  在本地创建和远程分支对应的分支 git checkout -b <本地分支名> origin/<远程分支名>，本地和远程分支的名称最好一致
3.  在本地分支完成任务后，可以试图用git push <远程主机名> <本地分支名>推送自己的修改
4.  如果推送失败，则表明远程分支比本地更新，需要先用git pull试图合并；
5.  如果pull失败并提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令git branch –set-upstream-to=<远程主机名>/<远程分支名> <本地分支名>创建链接
6.  如果合并有冲突，则解决冲突，并在本地提交（add => commit）
7.  没有冲突或者解决掉冲突后，再用git push <远程主机名> <本地分支名>推送就能成功
8.  提交到远程仓库以后，就可以发出 Pull Request 到staging分支，然后请求别人进行代码review，确认可以合并到staging
    1.  操作之前务必获取staging/master最新代码（pull 或者 fetch+merge）

## 常用语法[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_1 "Permanent link")

```markdown
######### Status, Add, Commit, Remove, Diff, Log, Checkout, Reset ##########

- 查看状态：
    ```bash
    git status
    ```

- 添加文件到暂存区：
    ```bash
    git add file1.txt file2.txt  # 添加指定文件
    git add -A                  # 添加当前目录下的所有修改
    git add .                   # 添加修改和新建文件
    git add -u                  # 添加修改和删除文件
    ```

- 提交更改：
    ```bash
    git commit -m "comment"  # 提交时的说明，必须要有
    ```

- 删除文件：
    ```bash
    git rm file.txt          # 从版本库中删除文件
    git rm -r filebook       # 删除文件夹
    ```

- 查看未提交的修改：
    ```bash
    git diff HEAD^
    git diff HEAD -- readme.txt  # 查看工作区和版本库最新版本的区别
    ```

- 查看提交历史：
    ```bash
    git log       # 提交历史
    git reflog    # 查看命令历史（包括回退修改等）
    ```

- 回滚到某个具体历史版本：
    ```bash
    git reset --hard 提交id
    ```

- 撤销更改：
    ```bash
    git checkout -- 文件名  # 退回到最近一次 add 或 commit 的状态
    git reset HEAD readme.txt  # 暂存区撤销
    ```

######### Remote ##########

- 查看远程仓库信息：
    ```bash
    git remote -v
    git remote show xxx
    ```

- 添加远程仓库：
    ```bash
    git remote add xxx git@server-name:path/repo-name.git
    ```

- 删除远程仓库：
    ```bash
    git remote rm xxx
    ```

######### Clone ##########

- 克隆远程仓库：
    ```bash
    git clone ssh://git@git.sankuai.com/dapp/poi_search_rerank.git
    git clone -b branch-name git@server-name:path/repo.git  # 克隆指定分支
    ```

######### Pull ##########

- 拉取远程分支：
    ```bash
    git pull <远程主机名> <远程分支名>:<本地分支名>
    git pull origin next:master
    ```

- 手动建立追踪关系：
    ```bash
    git branch --set-upstream-to=远程主机名/<远程分支名> <本地分支名>
    ```

- 使用 rebase 模式拉取：
    ```bash
    git pull --rebase <远程主机名> <远程分支名>:<本地分支名>
    ```

######### Push ##########

- 推送本地分支到远程：
    ```bash
    git push <远程主机名> <本地分支名>:<远程分支名>
    git push -u origin master  # 设置默认主机
    ```

######### Branch and Checkout ##########

- 分支操作：
    ```bash
    git branch          # 查看当前分支
    git branch -a       # 查看远程分支
    git branch <name>   # 创建分支
    git checkout <name> # 切换分支
    git checkout -b <name>  # 创建并切换到分支
    git branch -d <name>    # 删除分支
    git branch -D <name>    # 强制删除未合并的分支
    ```

######### Merge ##########

- 合并分支：
    ```bash
    git merge <branch-name>  # 合并分支
    git merge --no-ff -m "comment"  # 禁用 Fast forward 模式，生成新的 commit
    ```
```

## 具体应用[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_2 "Permanent link")

### 撤销修改[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_3 "Permanent link")

撤销修改的操作可以根据文件是否已被 `add` 到暂存区来选择不同的命令：

- 未 `add` 的文件：
    ```bash
    git restore <file>...
    ```

- 已 `add` 的文件：
    ```bash
    git restore --staged <file>...
    git restore <file>
    ```

### 代码回滚：git reset、git checkout 和 git revert[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#git-resetgit-checkoutgit-revert "Permanent link")

> **注意**：虽然以下内容使用了 `reset` 和 `checkout` 来恢复文件，但按照 Git 的指示，`restore` 是更加规范的选择。

#### `git reset`

`git reset` 用于撤销未被提交到远程的改动，即撤销本地的修改。它不仅会移动当前分支的 `HEAD`，还可以更改工作区（workspace）和暂存区（index）：

- `--soft`：修改 `HEAD`，不修改 `index` 和 `workspace`。
- `--mixed`：修改 `HEAD` 和 `index`，不修改 `workspace`。（默认行为）
- `--hard`：修改 `HEAD`、`index` 和 `workspace`。

示例：
```bash
# 修改 HEAD 和 index
git checkout hotfix
git reset HEAD~2

# reset 恢复文件
git reset HEAD filename  # 默认是 --mixed，修改 HEAD 和 index，不修改 workspace
```

#### `git checkout`

`git checkout` 作用于提交级别时，只是移动 `HEAD` 到不同的提交。如果有未暂存的文件，Git 会阻止操作并提示。

- 使用 `commit id` 作为参数可能会导致野指针。
- `git checkout -- file` 中的 `--` 很重要，没有 `--` 会变成“切换到另一个分支”的命令。

示例：
```bash
# 修改 workspace 去匹配某次 commit
git checkout HEAD

# 抹掉文件在 workspace 的修改（即使已 add 也行）
git checkout HEAD filename

# 若已 add，则恢复为 index 的结果；若未 add，则恢复为 HEAD 的结果
git checkout -- file
```

#### `git revert`

`git revert` 用于“反做”某一个版本，以达到撤销该版本修改的目的。它会生成一个新的提交，而不是直接修改历史记录。

例如：我们提交了三个版本（版本一、版本二、版本三），发现版本二有问题（如：存在 bug），想要撤销版本二的修改，但又不想影响版本三的提交。此时可以使用 `git revert` 来反做版本二，生成一个新的版本四。版本四会保留版本三的内容，但撤销版本二的修改。

示例：
```bash
git checkout hotfix
git revert HEAD^^
```

### 查看文件的修改记录[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_4 "Permanent link")

先查看在哪些提交中修改了这个文件。`--pretty=oneline` 使得 log 更加简洁，`--` 可省略：

```bash
git log --pretty=oneline -- 文件名
```

然后从 log 中找到要查看的那一次提交所对应的 id，用 `git show _id` 进行查看：

```bash
git show 356f6def9d -- 文件名
```

### 合并远程分支[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_5 "Permanent link")

有的时候我们需要跟别人合作进行开发，然后分别使用不同的 Git 分支。等项目完成时，需要进行代码合并，就需要知道如何合并远程分支。

假设你本地在使用的分支为 `a`（master 也是一样的），需要合并的远程分支为 `b`：

```bash
# 在本地新建一个与远程分支 b 相同的分支 b
git checkout -b b origin/b

# 将远程代码 pull 到本地
git pull origin b

# 切换回分支 a
git checkout a

# 合并分支 a 与分支 b
git merge b
```

### 删除文件恢复[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_6 "Permanent link")

如果删除了文件并且已经提交了，可以尝试以下操作恢复文件：

```bash
# 回退到上一次提交的状态
git reset HEAD^ 文件名

# 恢复文件到暂存区
git restore --staged <file>
```

### 取消文件跟踪[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_7 "Permanent link")

一些需要添加到 `.gitignore` 中的文件，如果之前已经建立了索引，需要取消跟踪：

```bash
# 单个文件
git rm --cached readme1.txt

# 所有文件（不删除本地文件）
git rm -r --cached .

# 所有文件（删除本地文件）
git rm -r --f .
```
> 以下内容来自廖雪峰教程

## 版本库[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_8 "Permanent link")

### 创建版本库[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_9 "Permanent link")

初始化一个 Git 仓库，使用以下命令：

```bash
git init
```

添加文件到 Git 仓库，分两步：

1. 使用命令 `git add <file>`，注意，可反复多次使用，添加多个文件；
2. 使用命令 `git commit -m <message>`，完成提交。

```bash
git add <file>
git commit -m "提交说明"
```

### 版本回退[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_10 "Permanent link")

- `HEAD` 指向的版本就是当前版本，因此，Git 允许我们在版本的历史之间穿梭，使用命令 `git reset --hard commit_id`。
- 穿梭前，用 `git log` 可以查看提交历史，以便确定要回退到哪个版本。
- 要重返未来，用 `git reflog` 查看命令历史，以便确定要回到未来的哪个版本。

```bash
# 查看提交历史
git log

# 回退到指定版本
git reset --hard commit_id

# 查看命令历史
git reflog
```

#### 版本命名[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_11 "Permanent link")

首先，Git必须知道当前版本是哪个版本，在Git中，用`HEAD`表示当前版本，也就是最新的提交`1094adb...`（注意我的提交ID和你的肯定不一样），上一个版本就是`HEAD^`，上上一个版本就是`HEAD^^`，当然往上100个版本写100个`^`比较容易数不过来，所以写成`HEAD~100`。

### 工作区和暂存区[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_12 "Permanent link")

暂存区是Git非常重要的概念，弄明白了暂存区，就弄明白了Git的很多操作到底干了什么。

### 管理修改[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_13 "Permanent link")

注意，`git diff readme.txt` 是与暂存区的文件比较；而 `git diff HEAD -- readme.txt` 则是与 HEAD 版本下的文件进行比较。因此，若在修改 readme.txt 后，已经 add 而尚未 commit ，则前者不会显示差异后者会显示出修改内容。

### 撤销修改 checkout –[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#checkout "Permanent link")

场景1：当你改乱了工作区某个文件的内容，想直接丢弃工作区的修改时，用命令 `git checkout -- file`。

场景2：当你不但改乱了工作区某个文件的内容，还添加到了暂存区时，想丢弃修改，分两步，第一步用命令 `git reset HEAD <file>`，就回到了场景1，第二步按场景1操作。

场景3：已经提交了不合适的修改到版本库时，想要撤销本次提交，参考[版本回退](https://www.liaoxuefeng.com/wiki/896043488029600/897013573512192)一节，不过前提是没有推送到远程库。

### 删除文件[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_14 "Permanent link")

命令 `git rm` 用于删除一个文件。如果一个文件已经被提交到版本库，那么你永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失**最近一次提交后你修改的内容**。

为了恢复删除的文件，：

场景 1：删除了文件，但没有 `git rm test.txt`，这时可以用 `git checkout -- test.txt` 找回；

场景 2：删除文件并且执行了 rm 操作，但没有 commit（这时候缓存区已经没有该文件了），则可以用 `git reset -- test.txt` 提取版本库中文件到缓存区，再使用 `git checkout -- test.txt` 从缓存区取回工作区；

场景 3：删除文件并且已经提交到版本库，可以用 `git reset HEAD^ -- test.txt` 提取该文件到缓存区；再使用 `git checkout -- test.txt` 提取回本地。

## 远程仓库[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_15 "Permanent link")

【总结一下】在 GitHub 上新建一个 repo，然后 1. clone 下来；2. 或者用类似 `git remote add origin git@github.com:michaelliao/learngit.git` 的命令。（这里的 origin 只是定义了远程仓库的名字）

### 案例：类似 GitHub 提示[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#github "Permanent link")

首先需要现在远程创建一个分支，比如地址为 `https://xxxxxxx/wangdong/helloworld.git`

`# 从本地新建一个分支，关联到 remote touch README.md git init git add README.md git commit -m "first commit" git branch -M main git remote add origin https://xxxxxxx/wangdong/helloworld.git git push -u origin main  # 本来就有了，直接关联 remote git remote add origin https://xxxxxxx/wangdong/helloworld.git git branch -M main git push -u origin main  # 若已有一个关联的 remote，则可取消后重新关联一个新的远程分支 git remote remove origin git remote add origin https://dev.33.cn/wangdong/alioss-file.git`

### 添加远程库[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_16 "Permanent link")

要关联一个远程库，使用命令`git remote add origin git@server-name:path/repo-name.git`；

关联后，使用命令`git push -u origin master`第一次推送master分支的所有内容；

此后，每次本地提交后，只要有必要，就可以使用命令`git push origin master`推送最新修改；

分布式版本系统的最大好处之一是在本地工作完全不需要考虑远程库的存在，也就是有没有联网都可以正常工作，而SVN在没有联网的时候是拒绝干活的！当有网络的时候，再把本地提交推送一下就完成了同步，真是太方便了！

### 从远程库克隆[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_17 "Permanent link")

要克隆一个仓库，首先必须知道仓库的地址，然后使用`git clone`命令克隆。

Git支持多种协议，包括`https`，但`ssh`协议速度最快。

## 分支管理[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_18 "Permanent link")

### 创建与合并[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_19 "Permanent link")

Git鼓励大量使用分支：

查看分支：`git branch`

创建分支：`git branch <name>`

切换分支：`git checkout <name>`或者`git switch <name>`

创建+切换分支：`git checkout -b <name>`或者`git switch -c <name>`

合并某分支到当前分支：`git merge <name>`

删除分支：`git branch -d <name>`

### 解决冲突[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_20 "Permanent link")

当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。

解决冲突就是把Git合并失败的文件手动编辑为我们希望的内容，再提交。

用`git log --graph`命令可以看到分支合并图。

### 分支管理策略[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_21 "Permanent link")

Git分支十分强大，在团队开发中应该充分应用。

合并分支时，加上`--no-ff`参数就可以用普通模式合并，合并后的历史有分支，能看出来曾经做过合并，而`fast forward`合并就看不出来曾经做过合并。

在实际开发中，我们应该按照几个基本原则进行分支管理：

-   首先，`master`分支应该是非常稳定的，也就是仅用来发布新版本，平时不能在上面干活；
-   那在哪干活呢？干活都在`dev`分支上，也就是说，`dev`分支是不稳定的，到某个时候，比如1.0版本发布时，再把`dev`分支合并到`master`上，在`master`分支发布1.0版本；
-   你和你的小伙伴们每个人都在`dev`分支上干活，每个人都有自己的分支，时不时地往`dev`分支上合并就可以了。

### Bug 分支[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#bug "Permanent link")

修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；

当手头工作没有完成时，先把工作现场`git stash`一下，然后去修复bug，修复后，再`git stash pop`，回到工作现场；

在master分支上修复的bug，想要合并到当前dev分支，可以用`git cherry-pick <commit>`命令，把bug提交的修改“复制”到当前分支，避免重复劳动。

### Feature 分支[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#feature "Permanent link")

开发一个新feature，最好新建一个分支；

如果要丢弃一个没有被合并过的分支，可以通过`git branch -D <name>`强行删除。

### 多人协作[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_22 "Permanent link")

-   查看远程库信息，使用`git remote -v`；
-   本地新建的分支如果不推送到远程，对其他人就是不可见的；
-   从本地推送分支，使用`git push origin branch-name`，如果推送失败，先用`git pull`抓取远程的新提交；
-   在本地创建和远程分支对应的分支，使用`git checkout -b branch-name origin/branch-name`，本地和远程分支的名称最好一致；
-   建立本地分支和远程分支的关联，使用`git branch --set-upstream branch-name origin/branch-name`；
-   从远程抓取分支，使用`git pull`，如果有冲突，要先处理冲突。

因此，多人协作的工作模式通常是这样：

1.  首先，可以试图用`git push origin <branch-name>`推送自己的修改；
2.  如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3.  如果合并有冲突，则解决冲突，并在本地提交；
4.  没有冲突或者解决掉冲突后，再用`git push origin <branch-name>`推送就能成功！

如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream-to <branch-name> origin/<branch-name>`。

## 标签管理[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_23 "Permanent link")

-   命令`git tag <tagname>`用于新建一个标签，默认为`HEAD`，也可以指定一个commit id；
-   命令`git tag -a <tagname> -m "blablabla..."`可以指定标签信息；
-   命令`git tag`可以查看所有标签。
    
-   命令`git push origin <tagname>`可以推送一个本地标签；
    
-   命令`git push origin --tags`可以推送全部未推送过的本地标签；
-   命令`git tag -d <tagname>`可以删除一个本地标签；
-   命令`git push origin :refs/tags/<tagname>`可以删除一个远程标签。

> 以下 from 美团

### git状态含义[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#git "Permanent link")

M 表示改动 A 表示添加 D 表示删除 R 表示重命名 C 表示拷贝 U 表示已更新到索引区但是未合并 ? 表示还没添加到git库中的文件 ! 表示已被忽略的文件 AU 我们添加了文件 UD 他们删除了文件 DD 双方都删除了文件 UU 双方都修改了文件

### 配置别名[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#_24 "Permanent link")

命令可以简写，用git st表示git status

`git config --global alias.co checkout git config --global alias.ci commit git config --global alias.br branch git config --global alias.last 'log -1' git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"`

当前用户的Git配置文件存放在 `～/.gitconfig` 文件中；当前仓库的配置文件在 `.git/config`

### 设置UI颜色[¶](https://lightblues.github.io/techNotes/code/CS/git-note/#ui "Permanent link")

`git config --global color.ui true`

---

