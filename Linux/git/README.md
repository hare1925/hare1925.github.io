# git笔记

## git记住密码

###  git永久记住密码  
git config --global credential.helper store  
会在用户主目录的`,gitconfig` 文件中生成下面的配置。  

```
[credential]
    helpwe = store
```

如果没有`--global` ,则在当前目录下的`.git/config` 文件中添加。  
当然，你也可以直接复制上面生成的配置到配置文件中。  

--------

### 临时记住密码
默认记住15分钟：  
`git config -global credential.helper cache`  

下面是自定义配置记住1小时：  

`git config credential.helper 'cache -temeout=3600'`  

### SSH记住密码

可以从一个已有的SSH KEY 来记住密码，会在用户主目录下的 `known_hosts` 生成配置。  

**把ssh key添加到ssh-agent**  

```
$ eval $(ssh-agent -s)
$ ssh-add ~/.ssh/id_rsa
```

如添加过程：  

```
$ eval $(ssh-agent -s)
Agent pid 54188

$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /c/User/Administrator/.ssh/id_rsa:
Identity added: /c/User/Administrator/.ssh/id_rsa (/c/Users/Administrator/.ssh/id_rsa)
```

这个很蛋疼，对当前设置有效，重新启动电脑就没了。

