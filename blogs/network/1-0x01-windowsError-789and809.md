# 解决win-7连接IPsec报错789和809错误

萌新一枚，大神请飘过~~~   

最近遇到一个很沙雕的问题，win7连接IPsec一直报错789，百度方法解决掉后又报错809，809解决掉后继续报789，很是恼火。  

网络上基本找不到可行方案，问题解决后写篇博客分享一下。

如果不出意外的话，windows7、vista、xp应该都试用，但因为我要用的这台电脑是win7，所以还是仅供参考。

## 应该具备的材料

- server IP
- IPsec PSK
- Username
- password

## 上菜

### 1、 退出流氓安全软件

不多说

### 2、 导入注册表

开始 ——> 在搜索栏搜索`cmd` ——> 右击，以管理员身份运行  

复制以下代码，粘贴，回车

`REG ADD HKLM\SYSTEM\CurrentControlSet\Services\PolicyAgent /v AssumeUDPEncapsulationContextOnSendRule /t REG_DWORD /d 0x2 /f`  

`REG ADD HKLM\SYSTEM\CurrentControlSet\Services\RasMan\Parameters /v ProhibitIpSec /t REG_DWORD /d 0x0 /f`


## 3、 设置本地安全策略

`win + R` 搜索 `secpol.msc`

1. 本地策略 > 安全选项
2. 网络安全：LAN Manager身份验证级别...
	- 设置为：发送LM和NTLMv2-使用NTLMv2....
3. 网络安全性：最低会话安全性...客户端
	- 取消选中“需要128位加密”

## 4、 启动服务

`win + R` 搜索 `services.msc`  

启动以下服务 **（设置为自动）**  

1. IPsec Policy Agent
2. Routing and Remote Access
3. Remote Access Auto Connection Manager
4. Remote Access Connection Manager
5. Secure Socket Tunneling Protocol Service

## 5、 设置网络

1. 开始 --》 控制面板
2. 网络和Internet部分
3. 网络和共享中心
4. 设置新的连接或网络
5. 连接到工作区 --》 下一步
6. 使用我的Internet连接（vpn）
7. internet地址  输入 `server IP`
8. 目标名称 （随便填）
9. 现在不连接；仅进行设置以便稍后连接
10. 下一步
11. 用户名、密码
12. 创建、关闭
13. 网络和共享中心 --》 更改适配器设置
14. 右击你创建的连接 --》 属性
15. 常规
	- 输入ip，如果前面没有输入的话（否则忽略）
16. 选项
	- 拨号选项 --》 取消`包括windows登录域`
	- PPP设置 --》 启用LCP扩展（仅）
17. 安全
	- vpn类型 --》 使用IPsec的第2层隧道协议（L2TP/IPsec）
	- 高级设置 --》 使用预共享秘钥（输入IPsec预共享秘钥）
	- 数据加密 --》 可选加密（没有加密也可以连接）
	- 身份认证 --》 允许使用这些协议`质询握手...(CHAP)(H)`和`Microsoft ... (MA_CHAP v2)(C)`
18. 确定
19. 重启电脑
20. 关闭流氓杀软，尽情享受吧。



