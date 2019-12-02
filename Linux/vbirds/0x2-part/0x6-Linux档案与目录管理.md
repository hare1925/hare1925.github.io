# Linux文件与目录管理

## 1、目录与路径

绝对/相对路径的写法并不相同，需要特别注意。此外，当你下达指令时，该指令时透过什么工鞥来取得的？这与PATH这个变数有关。下面来学习喽！  

### 1.1、相对路径与绝对路径

在开始学习切换目录之前，必须要先了解一下所谓的【路径(PATH)】，又去的是：什么是【相对路径】于【绝对路径】，再次强调一下。  

- **绝对路径**：路径的写法【一定由根目录/写起】，例如：/usr/hare/这个目录。  
- **相对路径**：路径的写法【不是由/写起】，例如由 /usr/share/doc 要到 /usr/share/man 底下时，可以写成：【cd ../man】这就是相对路径的写法！相对路径意指【相对于目前工作目录的路径】！  

-----

- 相对路径的用途  

那么相对路径与绝对路径由什么了不起呀？真了不起呢！假设你需要装一个软件，这个软件共需要三个目录，分别是 etc, bin, man 这三个目录，然而由于不同的人喜欢安装在不同的目录之下，假设安装的路径是 /usr/local/packages/etc, /usr/local/packages/bin以及/usr/local/packages/man,不过乙却喜欢安装在 /home/packages/etc, /home/packages/bin, /home/packages/man这三个目录中，请问如果需要用到绝对路径的话，那是否很麻烦呢？是的！如此一来每个目录下的东西就很难对应的起来！这个时候相对路径的写法就显得特别重要了！  

此外，如果你跟鸟哥一样，喜欢将路径的名字写的很长，好让自己知道那个目录是在干什么的，那么用相对路径会很方便的。  


- 绝对路径用途  

但是对于档名的正确性来说，【绝对路径的正确度要比较好】。一般来说，鸟哥建议，如果在写程序（shell scripts）来管理系统的条件下，务必使用绝对路径的写法。怎么说呢？因为绝对路径的写法虽然比较麻烦，但是可以肯定这个写法绝对不会有问题。如果使用相对路径在程序当中，则可能由于你执行的工作环境不同，导致一些问题的发生。这个问题在工作排程（at， cron，第十五章）当中尤其重要！  

### 1.2、目录的相关操作

我们之前提到过cd命令，那目录还可以进行哪些指令呢？例如：建立目录，删除目录，之类的，还有，得要先知道，就是有哪些比较特殊的目录？一下这些得特别记住：  

```
.         代表此層目錄
..        代表上一層目錄
-         代表前一個工作目錄
~         代表『目前使用者身份』所在的家目錄
~account  代表 account 這個使用者的家目錄(account是個帳號名稱)
```

**需要注意的是**：在所有目录底下都会存在的两个目录，分别是【.】和【..】分别代表此层与上层目录的意思。  

**根目录的上一层与根目录自己是同一个目录**。  

了解一下几个常见的处理目录的指令吧：  

- cd ： 变换目录  
- pwd ： 显示目前的目录  
- mkdir ： 建立一个新的目录  
- rmdir ： 删除一个空的目录  

-----

- cd（change directory，改变目录）  

我们知道 dmtsai 这个使用者的家目录是 /home/dmtsai/,而 root 家目录则是 /root/,假设我们以 root身份在linux系统中，那么简单的说明一下这几个特殊的目录的意义是：  

```
[dmtsai@study ~]$ su -  # 先切換身份成為 root 看看！
[root@study ~]# cd [相對路徑或絕對路徑]
# 最重要的就是目錄的絕對路徑與相對路徑，還有一些特殊目錄的符號囉！
[root@study ~]# cd ~dmtsai
# 代表去到 dmtsai 這個使用者的家目錄，亦即 /home/dmtsai
[root@study dmtsai]# cd ~
# 表示回到自己的家目錄，亦即是 /root 這個目錄
[root@study ~]# cd
# 沒有加上任何路徑，也還是代表回到自己家目錄的意思喔！
[root@study ~]# cd ..
# 表示去到目前的上層目錄，亦即是 /root 的上層目錄的意思；
[root@study /]# cd -
# 表示回到剛剛的那個目錄，也就是 /root 囉～
[root@study ~]# cd /var/spool/mail
# 這個就是絕對路徑的寫法！直接指定要去的完整路徑名稱！
[root@study mail]# cd ../postfix
# 這個是相對路徑的寫法，我們由/var/spool/mail 去到/var/spool/postfix 就這樣寫！
```

cd 是Change directory的缩写，这个用来变换工作目录的指令，注意，目录名称与cd指令之间存在一个空格。  
登入linux后，每个账号都会在自己账号的家目录中，那回到上一层目录可以用【cd ..】，利用相对路径的写法必须要确认你目前的路径才能正确的渠道想要的目录。  
其实，我们的提示符即【root@study ~】#当中，就已经有指出目前的目录了，刚登入时会在自己的家目录，而家目录还有一个代码，那就是【~】符号！  
使用【cd ~】可以回到家目录，如果只输入cd那代表的就是回到自己家的意思。  
【cd -】代表着回到上一次所在的工作目录。  

- linux一般都会预设指令列模式（bash shell）具有档案不起功能，常常需要按【tab】键来补齐目录完整，这可是一个好习惯，可以很好的避免打错字。  

-----

- pwd（显示目前所在的目录）  

```
[root@study ~]# pwd [-P]
選項與參數：
-P  ：顯示出確實的路徑，而非使用連結 (link) 路徑。

範例：單純顯示出目前的工作目錄：
[root@study ~]# pwd
/root   <== 顯示出目錄啦～

範例：顯示出實際的工作目錄，而非連結檔本身的目錄名而已
[root@study ~]# cd /var/mail   <==注意，/var/mail是一個連結檔
[root@study mail]# pwd
/var/mail         <==列出目前的工作目錄
[root@study mail]# pwd -P
/var/spool/mail   <==怎麼回事？有沒有加 -P 差很多～
[root@study mail]# ls -ld /var/mail
lrwxrwxrwx. 1 root root 10 May  4 17:51 /var/mail -> spool/mail
# 看到這裡應該知道為啥了吧？因為 /var/mail 是連結檔，連結到 /var/spool/mail
# 所以，加上 pwd -P 的選項後，會不以連結檔的資料顯示，而是顯示正確的完整路徑啊！
```

pwd是print working directory的缩写，也就是显示目前所在的目录的指令。  
因为很多的套件所使用的目录名称都相同，例如 /usr/local/etc和/etc,这两个，在普通linux仅列出最后面一个目录而已，这个时候可能就需要用到pwd来看看自己到底在哪个目录了，以免搞混了。  

- 还有个【-P】的选项，它可以让我们取得正确的目录名称，而不是以链接档的路径来显示的。  


-----

- mkdir（建立新目录）  

```
[root@study ~]# mkdir [-mp] 目錄名稱
選項與參數：
-m ：設定檔案的權限喔！直接設定，不需要看預設權限 (umask) 的臉色～
-p ：幫助你直接將所需要的目錄(包含上層目錄)遞迴建立起來！

範例：請到/tmp底下嘗試建立數個新目錄看看：
[root@study ~]# cd /tmp
[root@study tmp]# mkdir test    <==建立一名為 test 的新目錄
[root@study tmp]# mkdir test1/test2/test3/test4
mkdir: cannot create directory ‘test1/test2/test3/test4’: No such file or directory
# 話說，系統告訴我們，沒可能建立這個目錄啊！就是沒有目錄才要建立的！見鬼嘛？
[root@study tmp]# mkdir -p test1/test2/test3/test4
# 原來是要建 test4 上層沒先建 test3 之故！加了這個 -p 的選項，可以自行幫你建立多層目錄！

範例：建立權限為rwx--x--x的目錄
[root@study tmp]# mkdir -m 711 test2
[root@study tmp]# ls -ld test*
drwxr-xr-x. 2 root   root  6 Jun  4 19:03 test
drwxr-xr-x. 3 root   root 18 Jun  4 19:04 test1
drwx--x--x. 2 root   root  6 Jun  4 19:05 test2
# 仔細看上面的權限部分，如果沒有加上 -m 來強制設定屬性，系統會使用預設屬性。
# 那麼你的預設屬性為何？這要透過底下介紹的 umask 才能瞭解喔！ ^_^
```

如果想要建立新的目录的化，那么就使用mkdir（make directory）吧！不过，在预设的情况下，你需要的目录得一层一层的建立才行！  
不过，现在有个更简单有效的方法！那就是加上`-p`这个选项哦！这个会递归穿件，并且，如果该目录本来就已经存在时，系统也不会显示错误信息哦！（不过鸟哥不建议使用-p因为如果打错字，目录就会乱七八糟的。  
另外，还有个地方必须要现有概念，那就是【预设权限】的地方。我们可以利用 -m 来强制给予一个新的目录相关的权限，例如上表当中，我们给予了 -m 711来给予新的目录 drwx--x--x 的权限。不过，如果没有给予 -m 选项时，那么预设的新建目录权限又是什么呢？这个和umask有关，我们在本章后头会介绍的。  

--------

- rmdir(删除【空】的目录)  

```
[root@study ~]# rmdir [-p] 目錄名稱
選項與參數：
-p ：連同『上層』『空的』目錄也一起刪除

範例：將於mkdir範例中建立的目錄(/tmp底下)刪除掉！
[root@study tmp]# ls -ld test*   <==看看有多少目錄存在？
drwxr-xr-x. 2 root   root  6 Jun  4 19:03 test
drwxr-xr-x. 3 root   root 18 Jun  4 19:04 test1
drwx--x--x. 2 root   root  6 Jun  4 19:05 test2
[root@study tmp]# rmdir test   <==可直接刪除掉，沒問題
[root@study tmp]# rmdir test1  <==因為尚有內容，所以無法刪除！
rmdir: failed to remove ‘test1’: Directory not empty
[root@study tmp]# rmdir -p test1/test2/test3/test4
[root@study tmp]# ls -ld test*    <==您看看，底下的輸出中test與test1不見了！
drwx--x--x. 2 root   root  6 Jun  4 19:05 test2
# 瞧！利用 -p 這個選項，立刻就可以將 test1/test2/test3/test4 一次刪除～
# 不過要注意的是，這個 rmdir 僅能『刪除空的目錄』喔！
```

如果有想要深处的目录，就使用 rmdir 吧！  
注意，目录需要一层一层的产出才行！而且被删除的目录里面必定不能存在其他的目录或档案！这意识所谓的空目录（empty directory)的意思啊！  
如果要将所有目录下的东西都删除掉！这个时候就必须要使用【rm -r】来进行递归删除了，不过还是使用rmdir比较不危险，也可以尝试使用 -p 的选项加入，来删除上层的目录哦！

### 1.3、关于执行文件路径的变量：$PATH

经过前面FHS的学习，我们可以知道查阅档案属性的指令ls完整大难名为： /bin/ls（这是绝对路径），那为什么我可以在任何地方执行 /bin/ls 这个指令呢？  
为什么我在任何目录下输入 ls 就一定可以显示出一些信息而不会说找不到该 /bin/ls 指令呢？  
这是因为环境变量 PATH 的帮助所致。  

**当我们在执行一个指令的时候，例如 ls这个命令，系统会依照PATH的设定去每个PATH定义的目录下搜寻档名为 ls 的可执行文档，如果PATH定义的目录中含有多个档名为ls的可执行档，那么先搜索到的同名指令先被执行。**  

现在，可以下达【echo $PATH】来看看到底有那些目录被定义出来了？ echo有【显示、打印】的意思，而PATH前面加的 $ 表示后面节的是变数，所以会显示出目前的PATH  

```
範例：先用root的身份列出搜尋的路徑為何？
[root@study ~]# echo $PATH
/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/root/bin

範例：用dmtsai的身份列出搜尋的路徑為何？
[root@study ~]# exit    # 由之前的 su - 離開，變回原本的帳號！或再取得一個終端機皆可！
[dmtsai@study ~]$ echo $PATH
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/dmtsai/.local/bin:/home/dmtsai/bin
# 記不記得我們前一章說過，目前 /bin 是連結到 /usr/bin 當中的喔！
```

PATH 一定是大写，这个变数的内容是由一堆目录所组成的，每个目录中间用冒号(:)来间隔，每个目录是有【顺序】之分的。仔细看以下上面的输出，你可以发现但无论是 root 还是 hare 都有 /bin 或 /usr/bin 这个目录在PATH变数内，所以当然能够在任何地方执行ls来找到 /bin/ls 执行档喽，因为 /bin 在centOS 7 当中，就是链接到 /usr/bin 去的，所以这两个目录内容会一模一样。  

- 假设用root将ls由/bin/ls移动称为/root/ls  
    - 1. 输入ls是否还可以执行。  
    - 2. 若不能，该如何执行ls这个指令？  
    - 3. 若要直接输入ls即可执行，又该如何进行？  

1. 将ls移动后，无论在那个目录输入ls都无法执行，也就是不能直接输入ls来执行，因为 /root 这个目录并不在PATH指定的目录中，所以，计时你在 /root 目录下，也不能够搜寻到ls这个指令。  
2. 因为ls的确存在于 /root 底下，并不是被删除了，所以可以通过**绝对路径** 或者**相对路径** 直接指定这个执行档档名，两种方法：1.`/root/ls`2.`./ls`  
3. 如果想要让root在任何目录都可以执行/root地下的ls，那么就将/root加入PATH当中即可。加入方法：  
    - `PATH="${PATH}:/root"`  
另外，除了 $PATH ，如果想要更明确定义出变数的名称，可以使用大括号 ${PATH} 来处理变数的呼叫。  
**注意这个实验做完了需要把ls放回去，不然系统可能会挂的**  

- 如果有两个 ls 指令在不同的目录中，那么下达 ls 的时候，哪个会被执行？  
    - 就是 ${PATH} 里面哪个目录先被查询，则那个目录下的指令就会被先执行了。  

- 为什么 ${PATH} 目录不加入本目录(.)?
    - 如果加入本目录，的确能够在指令所在目录执行指令。但是因为你的工作目录并非国定（常常会cd）因此能够执行的指令会有变动（因为每个目录地下的可执行档案不相同），这对使用者来说并不是好事。  
    - 如果有坏人使用者在 /tmp 地下做了一个指令，因为 /tmp 大家都能写入的环境，所以当然可以这样做。加入该指令可能会窃取使用者的一些资料，如果你还使用root的身份来执行这个指令，是不是很糟糕？如果这个指令的名称又是经常用到的 ls 时，那【中镖】的记录就更高了。  

所以，为了安全起见，并不建议将【.】加入PATH的搜索目录中。  

--------

由上我们可以得知几件事情：  

- 不同身份使用者预设的PATH不同，预设能够随意执行的指令也不同(如root与hare);  
- PATH是可以修改的;
- 使用绝对路径或相对路径直接指定某个指令的档名来执行，会比搜寻PATH来的正确；  
- 指令应该要放置到正确的目录下，执行才会比较方便；  
- 本目录(.)最好不要放到PATH当中。  

## 2、文件与目录管理

了解了路径，在了解一下档案的基本管理。  
档案的基本管理不外乎：属性、拷贝、删除档案 及 移动档案或目录 等等。  

### 2.1、文件与目录的查看：ls

```
[root@study ~]# ls [-aAdfFhilnrRSt] 檔名或目錄名稱..
[root@study ~]# ls [--color={never,auto,always}] 檔名或目錄名稱..
[root@study ~]# ls [--full-time] 檔名或目錄名稱..
選項與參數：
-a  ：全部的檔案，連同隱藏檔( 開頭為 . 的檔案) 一起列出來(常用)
-A  ：全部的檔案，連同隱藏檔，但不包括 . 與 .. 這兩個目錄
-d  ：僅列出目錄本身，而不是列出目錄內的檔案資料(常用)
-f  ：直接列出結果，而不進行排序 (ls 預設會以檔名排序！)
-F  ：根據檔案、目錄等資訊，給予附加資料結構，例如：
      *:代表可執行檔； /:代表目錄； =:代表 socket 檔案； |:代表 FIFO 檔案；
-h  ：將檔案容量以人類較易讀的方式(例如 GB, KB 等等)列出來；
-i  ：列出 inode 號碼，inode 的意義下一章將會介紹；
-l  ：長資料串列出，包含檔案的屬性與權限等等資料；(常用)
-n  ：列出 UID 與 GID 而非使用者與群組的名稱 (UID與GID會在帳號管理提到！)
-r  ：將排序結果反向輸出，例如：原本檔名由小到大，反向則為由大到小；
-R  ：連同子目錄內容一起列出來，等於該目錄下的所有檔案都會顯示出來；
-S  ：以檔案容量大小排序，而不是用檔名排序；
-t  ：依時間排序，而不是用檔名。
--color=never  ：不要依據檔案特性給予顏色顯示；
--color=always ：顯示顏色
--color=auto   ：讓系統自行依據設定來判斷是否給予顏色
--full-time    ：以完整時間模式 (包含年、月、日、時、分) 輸出
--time={atime,ctime} ：輸出 access 時間或改變權限屬性時間 (ctime) 
                       而非內容變更時間 (modification time)
```

在linux系统当中，这个ls指令可能是最常被执行的把！因为我们随时都要知道档案或者是目录的相关资讯啊。  
不过，当我们Linux的档案记录的资讯太多，ls没有需要全部列出来，所以，当你只有下达ls时，预设显示的只有：**非吟唱档的档名、以档名进行排序及档名代表的颜色显示**  
如果想要加入其他显示资讯时，可以加入上头提到的那些有用的选项，例如： -l 显示长串资料内容； -a 显示隐藏档案等  

```
範例一：將家目錄下的所有檔案列出來(含屬性與隱藏檔)
[root@study ~]# ls -al ~
total 56
dr-xr-x---.  5 root root 4096 Jun  4 19:49 .
dr-xr-xr-x. 17 root root 4096 May  4 17:56 ..
-rw-------.  1 root root 1816 May  4 17:57 anaconda-ks.cfg
-rw-------.  1 root root 6798 Jun  4 19:53 .bash_history
-rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
-rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
-rw-rw-rw-.  1 root root  176 Dec 29  2013 .bashrc
-rw-r--r--.  1 root root  176 Jun  3 00:04 .bashrc_test
drwx------.  4 root root   29 May  6 00:14 .cache
drwxr-xr-x.  3 root root   17 May  6 00:14 .config
# 這個時候你會看到以 . 為開頭的幾個檔案，以及目錄檔 (.) (..) .config 等等，
# 不過，目錄檔檔名都是以深藍色顯示，有點不容易看清楚就是了。

範例二：承上題，不顯示顏色，但在檔名末顯示出該檔名代表的類型(type)
[root@study ~]# ls -alF --color=never  ~
total 56
dr-xr-x---.  5 root root 4096 Jun  4 19:49 ./
dr-xr-xr-x. 17 root root 4096 May  4 17:56 ../
-rw-------.  1 root root 1816 May  4 17:57 anaconda-ks.cfg
-rw-------.  1 root root 6798 Jun  4 19:53 .bash_history
-rw-r--r--.  1 root root   18 Dec 29  2013 .bash_logout
-rw-r--r--.  1 root root  176 Dec 29  2013 .bash_profile
-rw-rw-rw-.  1 root root  176 Dec 29  2013 .bashrc
-rw-r--r--.  1 root root  176 Jun  3 00:04 .bashrc_test
drwx------.  4 root root   29 May  6 00:14 .cache/
drwxr-xr-x.  3 root root   17 May  6 00:14 .config/
# 注意看到顯示結果的第一行，嘿嘿～知道為何我們會下達類似 ./command 
# 之類的指令了吧？因為 ./ 代表的是『目前目錄下』的意思啊！至於什麼是 FIFO/Socket ？
# 請參考前一章節的介紹啊！另外，那個.bashrc 時間僅寫2013，能否知道詳細時間？

範例三：完整的呈現檔案的修改時間 (modification time)
[root@study ~]# ls -al --full-time  ~
total 56
dr-xr-x---.  5 root root 4096 2015-06-04 19:49:54.520684829 +0800 .
dr-xr-xr-x. 17 root root 4096 2015-05-04 17:56:38.888000000 +0800 ..
-rw-------.  1 root root 1816 2015-05-04 17:57:02.326000000 +0800 anaconda-ks.cfg
-rw-------.  1 root root 6798 2015-06-04 19:53:41.451684829 +0800 .bash_history
-rw-r--r--.  1 root root   18 2013-12-29 10:26:31.000000000 +0800 .bash_logout
-rw-r--r--.  1 root root  176 2013-12-29 10:26:31.000000000 +0800 .bash_profile
-rw-rw-rw-.  1 root root  176 2013-12-29 10:26:31.000000000 +0800 .bashrc
-rw-r--r--.  1 root root  176 2015-06-03 00:04:16.916684829 +0800 .bashrc_test
drwx------.  4 root root   29 2015-05-06 00:14:56.960764950 +0800 .cache
drwxr-xr-x.  3 root root   17 2015-05-06 00:14:56.975764950 +0800 .config
# 請仔細看，上面的『時間』欄位變了喔！變成較為完整的格式。
# 一般來說， ls -al 僅列出目前短格式的時間，有時不會列出年份，
# 藉由 --full-time 可以查閱到比較正確的完整時間格式啊！
```

其实 ls 的用法还有很多，包括**查阅档案所在 i-node 号码的 ls -i 选项，以及用来进行档案排序的 -S 选项** ,还有用来查阅不同时间的动作的 --time=atime 等选项。  
这些选项的存在都是因为linux档案系统记录了很多有用的资讯的缘故。那么linux的档案系统中，这些与权限、属性有关的资料放在哪里呢？放在 i-node 里面。（下一章深入讲解)  
无论如何， ls 最常被使用到的功能还是那个 -l 的选项，为此，很多 distribution 在预设的情况中，已经将ll（L的小写）设定为 ls -l 的意思了！  
这个功能是 Bash shell 的alias 功能呢，也就是说我们可以直接输入 ll 就等于输入 ls -l 了。  

### 2.2、复制、删除与移动：cp、rm、mv

- 复制档案，使用cp（copy）这个指令，这个指令除了单纯的复制之外，还可以建立链接档（就是捷径喽),比如两个档案的新旧而予以更新，以及赋值整个目录等等的功能。  
- 移动目录与档案，使用mv(move)这个指令，也可以直接拿来做更名（rename）  
- 删除文档与目录就是 rm(remove)这个指令喽。  

--------

### cp(扶着档案或目录)

```

[root@study ~]# cp [-adfilprsu] 來源檔(source) 目標檔(destination)
[root@study ~]# cp [options] source1 source2 source3 .... directory
選項與參數：
-a  ：相當於 -dr --preserve=all 的意思，至於 dr 請參考下列說明；(常用)
-d  ：若來源檔為連結檔的屬性(link file)，則複製連結檔屬性而非檔案本身；
-f  ：為強制(force)的意思，若目標檔案已經存在且無法開啟，則移除後再嘗試一次；
-i  ：若目標檔(destination)已經存在時，在覆蓋時會先詢問動作的進行(常用)
-l  ：進行硬式連結(hard link)的連結檔建立，而非複製檔案本身；
-p  ：連同檔案的屬性(權限、用戶、時間)一起複製過去，而非使用預設屬性(備份常用)；
-r  ：遞迴持續複製，用於目錄的複製行為；(常用)
-s  ：複製成為符號連結檔 (symbolic link)，亦即『捷徑』檔案；
-u  ：destination 比 source 舊才更新 destination，或 destination 不存在的情況下才複製。
--preserve=all ：除了 -p 的權限相關參數外，還加入 SELinux 的屬性, links, xattr 等也複製了。
最後需要注意的，如果來源檔有兩個以上，則最後一個目的檔一定要是『目錄』才行！
```

赋值(cp)这个指令是非常重要的，不同身份者执行这个指令会有不同的结果产生，尤其是那个 -a， -p的选项，对于不同身份来说，差异则非常的大！   

```
範例一：用root身份，將家目錄下的 .bashrc 複製到 /tmp 下，並更名為 bashrc
[root@study ~]# cp ~/.bashrc /tmp/bashrc
[root@study ~]# cp -i ~/.bashrc /tmp/bashrc
cp: overwrite `/tmp/bashrc'? n  <==n不覆蓋，y為覆蓋
# 重複作兩次動作，由於 /tmp 底下已經存在 bashrc 了，加上 -i 選項後，
# 則在覆蓋前會詢問使用者是否確定！可以按下 n 或者 y 來二次確認呢！

範例二：變換目錄到/tmp，並將/var/log/wtmp複製到/tmp且觀察屬性：
[root@study ~]# cd /tmp
[root@study tmp]# cp /var/log/wtmp . <==想要複製到目前的目錄，最後的 . 不要忘
[root@study tmp]# ls -l /var/log/wtmp wtmp
-rw-rw-r--. 1 root utmp 28416 Jun 11 18:56 /var/log/wtmp
-rw-r--r--. 1 root root 28416 Jun 11 19:01 wtmp
# 注意上面的特殊字體，在不加任何選項的情況下，檔案的某些屬性/權限會改變；
# 這是個很重要的特性！要注意喔！還有，連檔案建立的時間也不一樣了！
# 那如果你想要將檔案的所有特性都一起複製過來該怎辦？可以加上 -a 喔！如下所示：

[root@study tmp]# cp -a /var/log/wtmp wtmp_2
[root@study tmp]# ls -l /var/log/wtmp wtmp_2
-rw-rw-r--. 1 root utmp 28416 Jun 11 18:56 /var/log/wtmp
-rw-rw-r--. 1 root utmp 28416 Jun 11 18:56 wtmp_2
# 瞭了吧！整個資料特性完全一模一樣ㄟ！真是不賴～這就是 -a 的特性！
```

这个cp的功能很多，由于我们经常会复制一些资料，所以也会常用这个指令。  
一般来说我们去复制别人的资料（当然，该档案必须要有read的权限才行）时，总是希望复制到的资料最后是我们自己的，所以：  
在预设条件中，cp的来源档与目的档的权限是不同的，目的档的拥有者通常回事指令操作这本身。  

由于有了这个特性，因此当我们在进行备份的时候，某些需要特别注意的特殊权限档案，例如密码档(/etc/shadow)以及一些设定档，就不能直接以cp来复制，而必须要加上 -a 或 -p 等等可以完整复制档案权限的选项才行！  
另外，如果你想要复制档案给其他的使用者，也必须要注意到档案的权限（包含读、写、执行以及档案拥有者等等），否则，其他人还是无法针对你给予的档案进行修订的动作哦！注意注意！  

```

範例三：複製 /etc/ 這個目錄下的所有內容到 /tmp 底下
[root@study tmp]# cp /etc/ /tmp
cp: omitting directory `/etc'   <== 如果是目錄則不能直接複製，要加上 -r 的選項
[root@study tmp]# cp -r /etc/ /tmp
# 還是要再次的強調喔！ -r 是可以複製目錄，但是，檔案與目錄的權限可能會被改變
# 所以，也可以利用『 cp -a /etc /tmp 』來下達指令喔！尤其是在備份的情況下！

範例四：將範例一複製的 bashrc 建立一個連結檔 (symbolic link)
[root@study tmp]# ls -l bashrc
-rw-r--r--. 1 root root 176 Jun 11 19:01 bashrc  <==先觀察一下檔案情況
[root@study tmp]# cp -s bashrc bashrc_slink
[root@study tmp]# cp -l bashrc bashrc_hlink
[root@study tmp]# ls -l bashrc*
-rw-r--r--. 2 root root 176 Jun 11 19:01 bashrc         <==與原始檔案不太一樣了！
-rw-r--r--. 2 root root 176 Jun 11 19:01 bashrc_hlink
lrwxrwxrwx. 1 root root   6 Jun 11 19:06 bashrc_slink -> bashrc
```

这里的范例四很有意思：  
使用 -l 和 -s 都会建立所谓的连接档(link file),但是这两种连接档有不一样的情况。  
- -l 是所谓的实体连接(hard link),我们也称硬链接。  
- -s 是所谓的符号连接(symbolic link),我们也称软链接。  
简单来说软链接就是一个【捷径】，所以会看到档名右边会有个指向(->)的符号。  
至于硬链接则与原档案的属性权限完全一模一样，与尚未进行连结前的差异则是第二个link数由1变成2了。由于涉及到 i-node 相关知识，需要等到档案系统(filesystem)的时候在学习。  

```

範例五：若 ~/.bashrc 比 /tmp/bashrc 新才複製過來
[root@study tmp]# cp -u ~/.bashrc /tmp/bashrc
# 這個 -u 的特性，是在目標檔案與來源檔案有差異時，才會複製的。
# 所以，比較常被用於『備份』的工作當中喔！ ^_^

範例六：將範例四造成的 bashrc_slink 複製成為 bashrc_slink_1 與bashrc_slink_2
[root@study tmp]# cp bashrc_slink bashrc_slink_1
[root@study tmp]# cp -d bashrc_slink bashrc_slink_2
[root@study tmp]# ls -l bashrc bashrc_slink*
-rw-r--r--. 2 root root 176 Jun 11 19:01 bashrc
lrwxrwxrwx. 1 root root   6 Jun 11 19:06 bashrc_slink -> bashrc
-rw-r--r--. 1 root root 176 Jun 11 19:09 bashrc_slink_1            <==與原始檔案相同
lrwxrwxrwx. 1 root root   6 Jun 11 19:10 bashrc_slink_2 -> bashrc  <==是連結檔！
# 這個例子也是很有趣喔！原本複製的是連結檔，但是卻將連結檔的實際檔案複製過來了
# 也就是說，如果沒有加上任何選項時，cp複製的是原始檔案，而非連結檔的屬性！
# 若要複製連結檔的屬性，就得要使用 -d 的選項了！如 bashrc_slink_2 所示。

範例七：將家目錄的 .bashrc 及 .bash_history 複製到 /tmp 底下
[root@study tmp]# cp ~/.bashrc ~/.bash_history /tmp
# 可以將多個資料一次複製到同一個目錄去！最後面一定是目錄！
```

```
例題：
你能否使用 dmtsai 的身份，完整的複製/var/log/wtmp檔案到/tmp底下，並更名為dmtsai_wtmp呢？
答：
實際做看看的結果如下：
[dmtsai@study ~]$ cp -a /var/log/wtmp /tmp/dmtsai_wtmp
[dmtsai@study ~]$ ls -l /var/log/wtmp /tmp/dmtsai_wtmp
-rw-rw-r--. 1 dmtsai dmtsai 28416  6月 11 18:56 /tmp/dmtsai_wtmp
-rw-rw-r--. 1 root   utmp   28416  6月 11 18:56 /var/log/wtmp
由於 dmtsai 的身份並不能隨意修改檔案的擁有者與群組，因此雖然能夠複製wtmp的相關權限與時間等屬性， 但是與擁有者、群組相關的，原本 dmtsai 身份無法進行的動作，即使加上 -a 選項，也是無法達成完整複製權限的！
```

总之，由于cp有种种的大难属性与权限的特性，所以，在赋值时，必须要清楚的了解到：  

- 是否需要完整的保留原来档案的资讯？  
- 来源档案是否为连结档(symbolic link file)?  
- 来源档是否为特殊的档案，例如 FIFO， socket等？  
- 来源档是否为目录？  

--------

#### rm （移除档案或目录）

```
[root@study ~]# rm [-fir] 檔案或目錄
選項與參數：
-f  ：就是 force 的意思，忽略不存在的檔案，不會出現警告訊息；
-i  ：互動模式，在刪除前會詢問使用者是否動作
-r  ：遞迴刪除啊！最常用在目錄的刪除了！這是非常危險的選項！！！

範例一：將剛剛在 cp 的範例中建立的 bashrc 刪除掉！
[root@study ~]# cd /tmp
[root@study tmp]# rm -i bashrc
rm: remove regular file `bashrc'? y
# 如果加上 -i 的選項就會主動詢問喔，避免你刪除到錯誤的檔名！

範例二：透過萬用字元*的幫忙，將/tmp底下開頭為bashrc的檔名通通刪除：
[root@study tmp]# rm -i bashrc*
# 注意那個星號，代表的是 0 到無窮多個任意字元喔！很好用的東西！

範例三：將 cp 範例中所建立的 /tmp/etc/ 這個目錄刪除掉！
[root@study tmp]# rmdir /tmp/etc
rmdir: failed to remove '/tmp/etc': Directory not empty   <== 刪不掉啊！因為這不是空的目錄！
[root@study tmp]# rm -r /tmp/etc
rm: descend into directory `/tmp/etc'? y
rm: remove regular file `/tmp/etc/fstab'? y
rm: remove regular empty file `/tmp/etc/crypttab'? ^C  <== 按下 [ctrl]+c 中斷
.....(中間省略).....
# 因為身份是 root ，預設已經加入了 -i 的選項，所以你要一直按 y 才會刪除！
# 如果不想要繼續按 y ，可以按下『 [ctrl]-c 』來結束 rm 的工作。
# 這是一種保護的動作，如果確定要刪除掉此目錄而不要詢問，可以這樣做：
[root@study tmp]# \rm -r /tmp/etc
# 在指令前加上反斜線，可以忽略掉 alias 的指定選項喔！至於 alias 我們在bash再談！
# 拜託！這個範例很可怕！你不要刪錯了！刪除 /etc 系統是會掛掉的！

範例四：刪除一個帶有 - 開頭的檔案
[root@study tmp]# touch ./-aaa-  <==touch這個指令可以建立空檔案！
[root@study tmp]# ls -l 
-rw-r--r--. 1 root   root       0 Jun 11 19:22 -aaa-  <==檔案大小為0，所以是空檔案
[root@study tmp]# rm -aaa-
rm: invalid option -- 'a'                    <== 因為 "-" 是選項嘛！所以系統誤判了！
Try 'rm ./-aaa-' to remove the file `-aaa-'. <== 新的 bash 有給建議的
Try 'rm --help' for more information.
[root@study tmp]# rm ./-aaa-
```

这是移除的指令(remove),要注意的是：  
通常在linux系统下，为了怕档案被root误杀，所以很多distributions都已经预设加入 -i 这个选项了！  
而如果想要连目录下的东西都一起杀掉的话，那就要使用 -r 这个选项了！**不过在使用 【rm -r】这个指令之前，请千万注意了，因为该目录或档案【肯定】会被root杀掉** 因为系统不会再次询问你是否要砍掉哦！所以那是个超级严重的指令下达，如果你确定该目录不要了，那么用这个递归杀掉是个不错的方式！  

另外，范例四也是很有趣的例子，之前就说过，档名最好不要使用“-”号开头，因为后面接的是选项，因此，单纯的使用【rm -aaa-】系统的指令就会误判了。那如果使用后面会谈到的正则表达式时，还是会出现问题的。  
所以，只能避过首字符用“-”的方法了。就是加上本身目录【./】即可  
如果 man rm 的话，其实还有一种方法，那就是【rm -- -aaa-】也可以啊！  

--------

#### mv (移动档案与目录，或更名)

```
[root@study ~]# mv [-fiu] source destination
[root@study ~]# mv [options] source1 source2 source3 .... directory
選項與參數：
-f  ：force 強制的意思，如果目標檔案已經存在，不會詢問而直接覆蓋；
-i  ：若目標檔案 (destination) 已經存在時，就會詢問是否覆蓋！
-u  ：若目標檔案已經存在，且 source 比較新，才會更新 (update)

範例一：複製一檔案，建立一目錄，將檔案移動到目錄中
[root@study ~]# cd /tmp
[root@study tmp]# cp ~/.bashrc bashrc
[root@study tmp]# mkdir mvtest
[root@study tmp]# mv bashrc mvtest
# 將某個檔案移動到某個目錄去，就是這樣做！

範例二：將剛剛的目錄名稱更名為 mvtest2
[root@study tmp]# mv mvtest mvtest2 <== 這樣就更名了！簡單～
# 其實在 Linux 底下還有個有趣的指令，名稱為 rename ，
# 該指令專職進行多個檔名的同時更名，並非針對單一檔名變更，與mv不同。請man rename。

範例三：再建立兩個檔案，再全部移動到 /tmp/mvtest2 當中
[root@study tmp]# cp ~/.bashrc bashrc1
[root@study tmp]# cp ~/.bashrc bashrc2
[root@study tmp]# mv bashrc1 bashrc2 mvtest2
# 注意到這邊，如果有多個來源檔案或目錄，則最後一個目標檔一定是『目錄！』
# 意思是說，將所有的資料移動到該目錄的意思！
```

这是搬移(move)的意思！当你需要移动档案或目录的时候，就可以使用这个指令了！  
同时你也可以使用 -u（update）来测试新旧档案，看看是否需要搬移！  
另外一个用途就是【变更档名】，我们可以很轻易的使用mv来变更一个档案的档名呢！  
不过，在linux才有的指令当中，有个 rename ，可以用来更改大量的档名。  
可以使用 man rename 来查阅以下，也是挺有趣的指令哦！  

### 2.3、获取路径的文件名与目录名称pwd

- 每个档案的完整档名包含：前面的目录与最终的档名。  
而每个档名的长度都可以达到255个字节，那么你怎么知道那个是档名？那个是目录名？就是用斜线(/)来分辨啊。  
取得档名或者是目录名称，一般的用途应该是在写程序的时候用来判断只用的，这部分的指令可以在 shell scripts 里头再学习。  

先学习 【basename】 和 【dirname】 的用途！  

```
[root@study ~]# basename /etc/sysconfig/network
network         <== 很簡單！就取得最後的檔名～
[root@study ~]# dirname /etc/sysconfig/network
/etc/sysconfig  <== 取得的變成目錄名了！

```


## 3、文件内容查看

如果我们要查阅一个档案的内容是，该怎么办呢？  
最常用的指令有： cat 与 more 及 less  

如果需要查看一个很大的档案的最后几行字，怎么办呢？  
可以使用 tail 指令啊，此外，tac 这个指令也可以达到这个目的哦。  

- cat 由第一行开始显示档案内容  
- tac 从最后一行开始显示，可以看出 tac 是 cat 的到这写。  
- nl 显示的时候，顺道输出行号！  
- more 一页一页的显示档案内容  
- less 与 more 类似，但是比 more 更好的是，它可以往前翻页！  
- head 只看头几行  
- tail 只看尾巴几行  
- od 以二进位的方式读取档案内容  

### 3.1、直接查看文件内容

直接查阅一个档案的内容可以使用 cat/tac/nl 这几个指令啊！  

--------

#### cat (concatenate)

```
[root@study ~]# cat [-AbEnTv]
選項與參數：
-A  ：相當於 -vET 的整合選項，可列出一些特殊字符而不是空白而已；
-b  ：列出行號，僅針對非空白行做行號顯示，空白行不標行號！
-E  ：將結尾的斷行字元 $ 顯示出來；
-n  ：列印出行號，連同空白行也會有行號，與 -b 的選項不同；
-T  ：將 [tab] 按鍵以 ^I 顯示出來；
-v  ：列出一些看不出來的特殊字符

範例一：檢閱 /etc/issue 這個檔案的內容
[root@study ~]# cat /etc/issue
\S
Kernel \r on an \m

範例二：承上題，如果還要加印行號呢？
[root@study ~]# cat -n /etc/issue
     1  \S
     2  Kernel \r on an \m
     3
# 所以這個檔案有三行！看到了吧！可以印出行號呢！這對於大檔案要找某個特定的行時，有點用處！
# 如果不想要編排空白行的行號，可以使用『cat -b /etc/issue』，自己測試看看：

範例三：將 /etc/man_db.conf 的內容完整的顯示出來(包含特殊字元)
[root@study ~]# cat -A /etc/man_db.conf
# $
....(中間省略)....
MANPATH_MAP^I/bin^I^I^I/usr/share/man$
MANPATH_MAP^I/usr/bin^I^I/usr/share/man$
MANPATH_MAP^I/sbin^I^I^I/usr/share/man$
MANPATH_MAP^I/usr/sbin^I^I/usr/share/man$
.....(底下省略).....
# 上面的結果限於篇幅，鳥哥刪除掉很多資料了。另外，輸出的結果並不會有特殊字體，
# 鳥哥上面的特殊字體是要讓您發現差異點在哪裡就是了。基本上，在一般的環境中，
# 使用 [tab] 與空白鍵的效果差不多，都是一堆空白啊！我們無法知道兩者的差別。
# 此時使用 cat -A 就能夠發現那些空白的地方是啥鬼東西了！[tab]會以 ^I 表示，
# 斷行字元則是以 $ 表示，所以你可以發現每一行後面都是 $ 啊！不過斷行字元
# 在Windows/Linux則不太相同，Windows的斷行字元是 ^M$ 囉。
# 這部分我們會在第九章 vim 軟體的介紹時，再次的說明到喔！
```

Linux里面有【猫】指令？不是的，cat 是 concatenate(连续)的简写，主要功能是将一个档案的内容连续的打印在屏幕上。如果前面加上 `-n` 或 `-b` 的话，则每一行前面还会加上行号哦！**这里的 -n 是显示所有的行号，而 -b 则只是按照非空行来数**  

鸟哥还是比较少用cat的，毕竟档你的档案内容的行数超过40行以上，根本来不及在屏幕上看到结果！  
所以，配合等一下要介绍的 more 或者是 less 来执行比较好！  
此外，如果是一般的 DOS 档案时，就需要特别留意一些奇奇怪怪的符号了，例如断行与[tab]等，要显示出来，就得加入 -A 之类的选项了！  

--------

#### tac (反向列示)

```

[root@study ~]# tac /etc/issue

Kernel \r on an \m
\S
# 嘿嘿！與剛剛上面的範例一比較，是由最後一行先顯示喔！
```

tac这个好玩了！可以看一下，cat 与 tac ，刚好是反过来写的，所以它的功能就是跟cat相反的了。  
cat是由【第一行到最后一行连续显示在屏幕上】  
tac则是【由最后一行到第一行反向在屏幕上显示出来】  

--------

#### nl (添加行号列印)

```
[root@study ~]# nl [-bnw] 檔案
選項與參數：
-b  ：指定行號指定的方式，主要有兩種：
      -b a ：表示不論是否為空行，也同樣列出行號(類似 cat -n)；
      -b t ：如果有空行，空的那一行不要列出行號(預設值)；
-n  ：列出行號表示的方法，主要有三種：
      -n ln ：行號在螢幕的最左方顯示；
      -n rn ：行號在自己欄位的最右方顯示，且不加 0 ；
      -n rz ：行號在自己欄位的最右方顯示，且加 0 ；
-w  ：行號欄位的佔用的字元數。

範例一：用 nl 列出 /etc/issue 的內容
[root@study ~]# nl /etc/issue
     1  \S
     2  Kernel \r on an \m

# 注意看，這個檔案其實有三行，第三行為空白(沒有任何字元)，
# 因為他是空白行，所以 nl 不會加上行號喔！如果確定要加上行號，可以這樣做：

[root@study ~]# nl -b a /etc/issue
     1  \S
     2  Kernel \r on an \m
     3
# 呵呵！行號加上來囉～那麼如果要讓行號前面自動補上 0 呢？可這樣

[root@study ~]# nl -b a -n rz /etc/issue
000001  \S
000002  Kernel \r on an \m
000003
# 嘿嘿！自動在自己欄位的地方補上 0 了～預設欄位是六位數，如果想要改成 3 位數？

[root@study ~]# nl -b a -n rz -w 3 /etc/issue
001     \S
002     Kernel \r on an \m
003
# 變成僅有 3 位數囉～
```

nl 可以将输出的档案内容自动的加上行号！其预设的结果与 cat -n 优点不太一样， nl 可以将行号作比较多的显示设计，包括位数与是否自动补齐 0 等等的功能呢。  

### 3.2、可翻页查看

前面提到的 nl 与 cat，tac 等等，都是一次性的将资料一口气显示到屏幕上面，那有没有可以进行一页一页反动的指令啊？  
一页一页的观察，才不会前面的资料看不到啊。  
那就是 more 与 less 喽！  

--------

#### more (一页一页翻动)

```
[root@study ~]# more /etc/man_db.conf
#
#
# This file is used by the man-db package to configure the man and cat paths.
# It is also used to provide a manpath for those without one by examining
# their PATH environment variable. For details see the manpath(5) man page.
#
.....(中間省略).....
--More--(28%)  <== 重點在這一行喔！你的游標也會在這裡等待你的指令
```

仔细看上面的范例，如果 more 后面接的档案内容行数大于屏幕输出的行数时，就会出现类似上面的图像。重点在最后一行，最后一行会显示出目前显示的百分比，而且还可以在最后一行输入一些有用的指令呢！  
在 more 这个程序的运作过程中，你有几个按键可以按的：  

- 空白键(space) : 代表向下翻一页；  
- Enter : 代表向下翻【一行】；
- /字串 ： 代表在这个显示的内容当中，向下搜寻【字串】这个关键字；  
- :f : like显示出档名以及目前显示的行数；  
- q ： 代表立刻离开 more， 不在显示档案内容；  
- b 或[ctrl]-b : 代表往回翻页，不过这个动作只对档案有用，对管线无用。  

要离开more这个指令的显示工作，可以按q。  
向下翻页就是用空白即可。  
比较有用的就是搜索字符串的功能，例如：  

```

[root@study ~]# more /etc/man_db.conf
#
#
# This file is used by the man-db package to configure the man and cat paths.
# It is also used to provide a manpath for those without one by examining
# their PATH environment variable. For details see the manpath(5) man page.
#
....(中間省略)....
/MANPATH   <== 輸入了 / 之後，游標就會自動跑到最底下一行等待輸入！v
```

如同上面的说明，输入了 / 之后，光标会到最后一行，并等待你的输入，你输入了字符串并按下[enter]之后，more就会开始向下搜寻字符串了，而重复搜寻一个字符串，可以直接按下 n 即可。最后按q离开more。  

--------

#### less (一页一页翻动)

```
[root@study ~]# less /etc/man_db.conf
#
#
# This file is used by the man-db package to configure the man and cat paths.
# It is also used to provide a manpath for those without one by examining
# their PATH environment variable. For details see the manpath(5) man page.
#
.....(中間省略).....
:   <== 這裡可以等待你輸入指令！
```

less 的用法比起 more 又更加有弹性，在 more 的时候，我们并没有办法向前翻页，只能往后面看，但或使用less时，就可以使用[pageup][pagedown]等按键的功能功能前往前后翻看文件。  

除此之外，在less里头可以拥有更多的【搜索】功能，不止可以向下搜索，也可以向上搜索，非常不错，可用的指令有：  

- 空白键 ： 向下翻动一页；
- 【pagedown】 ： 向下翻动一页；
- 【pageup】 ： 向上翻动一页；
- /字串 ： 向下搜寻【字串】的功能；
- ？字串 ： 向上搜寻【字串】的功能；
- n ： 重复前一个搜寻（与 / 或 ? 有关）
- N ： 反向的重复前一个搜寻(与 / 或 ? 有关）
- g ： 前进到这个资料的第一行去；
- G ： 前进到这个资料的最后一行去（注意大小写）；
- q ： 离开 less 这个程式；  

查阅档案还可以进行搜寻的动作，less是否很不错呢？其实less还有很多的功能！更详细的使用方法可以用 man less 查询以下啊！  
你是否会觉得less 使用的画面与环境与 man page 非常类似呢？没错，因为man这个指令就是呼叫less来显示说明文件的内容的！现在是否会觉得less很重要呢？  
--------

### 3.3、数据截取

我们可以将输出的资料最为一个最简单的截取，那就是取出档案前面几行(head)或取出后面几行(tail)文字的功能。  
不过，需要之一的是，head和tail都是以【行】为单位来进行资料截取的哦！  

--------

#### head (取出前面的几行)

```

[root@study ~]# head [-n number] 檔案 
選項與參數：
-n  ：後面接數字，代表顯示幾行的意思

[root@study ~]# head /etc/man_db.conf
# 預設的情況中，顯示前面十行！若要顯示前 20 行，就得要這樣：
[root@study ~]# head -n 20 /etc/man_db.conf

範例：如果後面100行的資料都不列印，只列印/etc/man_db.conf的前面幾行，該如何是好？
[root@study ~]# head -n -100 /etc/man_db.conf
```

head 的英文意思就是 【头】了，那么这个东西的用法自然就是显示出一个档案的前几行了。  
若没有加上 `-n` 这个选项时，预设只显示十行。  
若是只要一行呢？那就加入【head -n 1 filename】即可！  

另外，那个 -n 选项后面的参数比较有趣，如果接的是负数，例如上面的范例 `-n -100` 时，代表列前的所有行数，但不包括后面的 100 行。  
例如：centos 7.1 的 /etc/man_db.conf 共有 131 行，则上述的指令【head -n -100 /etc/man_db.conf】就会列出前面31行，后面100行不会列印出来了。  

--------

#### tail (取出后面几行) 

```
[root@study ~]# tail [-n number] 檔案 
選項與參數：
-n  ：後面接數字，代表顯示幾行的意思
-f  ：表示持續偵測後面所接的檔名，要等到按下[ctrl]-c才會結束tail的偵測

[root@study ~]# tail /etc/man_db.conf
# 預設的情況中，顯示最後的十行！若要顯示最後的 20 行，就得要這樣：
[root@study ~]# tail -n 20 /etc/man_db.conf

範例一：如果不知道/etc/man_db.conf有幾行，卻只想列出100行以後的資料時？
[root@study ~]# tail -n +100 /etc/man_db.conf

範例二：持續偵測/var/log/messages的內容
[root@study ~]# tail -f /var/log/messages
  <==要等到輸入[ctrl]-c之後才會離開tail這個指令的偵測！
```



### 3.4、非纯文本文件：od

我们前面提到的，都是在查阅纯文字档案的内容。那么万一我们想要查阅非文字档案，例如： `/usr/bin/passwd` 这个执行档案的内容时，又该如何去读出资讯呢？事实上，由于执行档通常是 binary file ，使用上头提到的指令来读取他的内容时，却是会产生类似乱码的资料！怎么办？没关系，我们可以利用 od 这个指令来读取哦！  

```
[root@study ~]# od [-t TYPE] 檔案
選項或參數：
-t  ：後面可以接各種『類型 (TYPE)』的輸出，例如：
      a       ：利用預設的字元來輸出；
      c       ：使用 ASCII 字元來輸出
      d[size] ：利用十進位(decimal)來輸出資料，每個整數佔用 size bytes ；
      f[size] ：利用浮點數值(floating)來輸出資料，每個數佔用 size bytes ；
      o[size] ：利用八進位(octal)來輸出資料，每個整數佔用 size bytes ；
      x[size] ：利用十六進位(hexadecimal)來輸出資料，每個整數佔用 size bytes ；

範例一：請將/usr/bin/passwd的內容使用ASCII方式來展現！
[root@study ~]# od -t c /usr/bin/passwd
0000000 177   E   L   F 002 001 001  \0  \0  \0  \0  \0  \0  \0  \0  \0
0000020 003  \0   >  \0 001  \0  \0  \0 364   3  \0  \0  \0  \0  \0  \0
0000040   @  \0  \0  \0  \0  \0  \0  \0   x   e  \0  \0  \0  \0  \0  \0
0000060  \0  \0  \0  \0   @  \0   8  \0  \t  \0   @  \0 035  \0 034  \0
0000100 006  \0  \0  \0 005  \0  \0  \0   @  \0  \0  \0  \0  \0  \0  \0
.....(後面省略)....
# 最左邊第一欄是以 8 進位來表示bytes數。以上面範例來說，第二欄0000020代表開頭是
# 第 16 個 byes (2x8) 的內容之意。

範例二：請將/etc/issue這個檔案的內容以8進位列出儲存值與ASCII的對照表
[root@study ~]# od -t oCc /etc/issue
0000000 134 123 012 113 145 162 156 145 154 040 134 162 040 157 156 040
          \   S  \n   K   e   r   n   e   l       \   r       o   n
0000020 141 156 040 134 155 012 012
          a   n       \   m  \n  \n
0000027
# 如上所示，可以發現每個字元可以對應到的數值為何！要注意的是，該數值是 8 進位喔！
# 例如 S 對應的記錄數值為 123 ，轉成十進位：1x8^2+2x8+3=83。
```

利用这个指令，可以将data file 或者 binary file 的内容资料读出来哦！虽然读出来的数值预设是使用非文字档，亦即16进位的数值来显示的，不过，我们还是可以透过 `-t c` 的选项参数来讲资料内的字节以 ASCII 类型的字节显示，虽然对于一般使用者来说，这个指令的用处可能不大，但是对于工程师来说，这个指令可以将 binary file 的内容作出一个大致的输出，他们可以看得出很多东西了。。。  

```
例如：
我不想找 google，想要立刻找到 password 這幾個字的 ASCII 對照，該如何透過 od 來判斷？
答：
其實可以透過剛剛上一個小節談到的管線命令來處理！如下所示：
echo password | od -t oCc
echo 可以在螢幕上面顯示任何資訊，而這個資訊不由螢幕輸出，而是傳給 od 去繼續處理！就可以得到 ASCII code 對照囉！
```

### 3.5、修改文件时间或创建新文件：touch

我们在ls这个指令的介绍是，有稍微提到每个档案在linux底下都会记录许多的时间参数，其实是有三个主要的变动时间，那这三个时间的意义是什么呢？  

- modification time(mtime): 
	- 当该档案的【内容资料】变更时，就会更新这个时间！内容资料指的是档案的内容，而不是档案的属性或权限！  

- status time(ctime):  
	- 当该档案的【状态（status）】改变时，就会更新这个时间，例如，像是权限与属性被更改了，都会更新这个时间啊。  

- access time(atime):  
	- 当【该档案的内容被取用】时，就会更新这个读取时间（access）。例如，我们使用cat去读取 /etc/man_db.conf，就会更新该档案的atime了。  

```
[root@study ~]# date; ls -l /etc/man_db.conf ; ls -l --time=atime /etc/man_db.conf ; \
> ls -l --time=ctime /etc/man_db.conf # 這兩行其實是同一行喔！用分號隔開
Tue Jun 16 00:43:17 CST 2015  # 目前的時間啊！
-rw-r--r--. 1 root root 5171 Jun 10  2014 /etc/man_db.conf  # 在 2014/06/10 建立的內容(mtime)
-rw-r--r--. 1 root root 5171 Jun 15 23:46 /etc/man_db.conf  # 在 2015/06/15 讀取過內容(atime)
-rw-r--r--. 1 root root 5171 May  4 17:54 /etc/man_db.conf  # 在 2015/05/04 更新過狀態(ctime)
# 為了要讓資料輸出比較好看，所以鳥哥將三個指令同時依序執行，三個指令中間用分號 (;) 隔開即可。
```

**在预设的情况下，ls显示出来的是该档案的mtime，也就是这个档案的内容上次被更动的时间。**  

档案的时间是很重要的，因为，如果档案的时间误判的话，可能会曹成某些程序无法的运作。那万一我发现了一个档案来时未来，该如何让该档案的是事假编程【现在】的时刻呢？很简单！就用 【touch】 这个指令即可！  

```
[root@study ~]# touch [-acdmt] 檔案
選項與參數：
-a  ：僅修訂 access time；
-c  ：僅修改檔案的時間，若該檔案不存在則不建立新檔案；
-d  ：後面可以接欲修訂的日期而不用目前的日期，也可以使用 --date="日期或時間"
-m  ：僅修改 mtime ；
-t  ：後面可以接欲修訂的時間而不用目前的時間，格式為[YYYYMMDDhhmm]

範例一：新建一個空的檔案並觀察時間
[dmtsai@study ~]# cd /tmp
[dmtsai@study tmp]# touch testtouch
[dmtsai@study tmp]# ls -l testtouch
-rw-rw-r--. 1 dmtsai dmtsai 0 Jun 16 00:45 testtouch
# 注意到，這個檔案的大小是 0 呢！在預設的狀態下，如果 touch 後面有接檔案，
# 則該檔案的三個時間 (atime/ctime/mtime) 都會更新為目前的時間。若該檔案不存在，
# 則會主動的建立一個新的空的檔案喔！例如上面這個例子！

範例二：將 ~/.bashrc 複製成為 bashrc，假設複製完全的屬性，檢查其日期
[dmtsai@study tmp]# cp -a ~/.bashrc bashrc
[dmtsai@study tmp]# date; ll bashrc; ll --time=atime bashrc; ll --time=ctime bashrc
Tue Jun 16 00:49:24 CST 2015                         <==這是目前的時間
-rw-r--r--. 1 dmtsai dmtsai 231 Mar  6 06:06 bashrc  <==這是 mtime
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 15 23:44 bashrc  <==這是 atime
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 16 00:47 bashrc  <==這是 ctime
```

在上面这个案例中，我们用了【ll】这个指令（两个英文L的小写），这个指令其实就是【ls -l】的意思。  
ll 本省不存在，是被【做出来】的一个命令别名。相关的命令别名我们会在 bash 章节当中湘潭，这里先知道一下就好。  
至于【;】则代表连续指令的下达拉！你可以在一个指令当中写入多冲指令，这些指令可以【依序】执行，由上面的指令我们会知道ll那一行有三个指令被下达在同一行。  

至于执行的结果当中，我们可发现资料的内容与属性是被复制过来的，因此档案内容时间（mtime）与原本档案相同。但是由于这个档案是刚刚被建立的，因此状态（ctime）就变成现在的时间了！那如果想要变更整个档案的时间呢？可以直接这样做：  

```
範例三：修改案例二的 bashrc 檔案，將日期調整為兩天前
[dmtsai@study tmp]# touch -d "2 days ago" bashrc
[dmtsai@study tmp]# date; ll bashrc; ll --time=atime bashrc; ll --time=ctime bashrc
Tue Jun 16 00:51:52 CST 2015
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 14 00:51 bashrc
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 14 00:51 bashrc
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 16 00:51 bashrc
# 跟上個範例比較看看，本來是 16 日變成 14 日了 (atime/mtime)～不過， ctime 並沒有跟著改變喔！

範例四：將上個範例的 bashrc 日期改為 2014/06/15 2:02
[dmtsai@study tmp]# touch -t 201406150202 bashrc
[dmtsai@study tmp]# date; ll bashrc; ll --time=atime bashrc; ll --time=ctime bashrc
Tue Jun 16 00:54:07 CST 2015
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 15  2014 bashrc
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 15  2014 bashrc
-rw-r--r--. 1 dmtsai dmtsai 231 Jun 16 00:54 bashrc
# 注意看看，日期在 atime 與 mtime 都改變了，但是 ctime 則是記錄目前的時間！
```

透过 touch 这个指令，我们可以轻易的修订档案的时间与日期。并且也可以建立一个空的档案。  
不过要注意的是，即使我们赋值一个档案时，复制所有的属性，但也没有办法复制 ctime 这个属性的。  
ctime 可以记录这个档案最近的状态（status）被改变的时间。  
无论如何，我们平时看的档案属性中，比较重要的还是属于哪个 mtime 啊！我们关心的常常是这个档案的【内容】是什么时候被更动的，瞭乎？  

无论如何—— touch 这个指令最常用的情况是：  

- 建立一个空的档案；  
- 将某个档案日期修改为目前（mtime 与 atime）


## 4、文件与目录的默认权限与隐藏权限

### 4.1、文件默认权限：umask

### 4.2、文件隐藏属性

### 4.3、文件特殊权限：SUID、SGID、SBIT

### 4.4、观察文件类型：file

## 5、命令与文件的查找

### 5.1、脚本文件的查找

### 5.2、文件的查找

## 6、极其重要的复习：权限与命令的关系




