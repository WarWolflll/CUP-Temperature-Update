# CUP-Temperature-Update
中石大自动填体温

##第一步：使用 Fiddler 获取 token

安装 Fiddler，在电脑微信上登录中石大填体温小程序，在 Fiddler 抓到的数据包里找到这一项并双击。

![1_LI](https://user-images.githubusercontent.com/35026476/144780248-b13af073-881d-47cb-b418-aaf4b57d4d38.jpg)

在右边找到 token 并记录下来。

![2_LI](https://user-images.githubusercontent.com/35026476/144780418-b36966c1-b9f1-455b-8857-8e87b13ce80e.jpg)

##第二步：填写数据

将 temperature.py 中的带 & 符号的数据替换为你需要的内容，运行该程序即可。
你可以在 PC 或服务器上设置一个定时任务，每天自动填写体温。
