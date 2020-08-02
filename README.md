# LightChat



## :page_with_curl: Introduction

💬 LightChat —— 一个微博客社交平台，用户可以发布动态、查看他人动态、关注或取关他人。另外可以通过上传图片的形式修改头像，且可以通过接收邮件的形式修改密码。



后台技术：Flask、MySQL

前端技术：Bootstrap、HTML



## :arrow_right: Instruction

配置完虚拟环境、部署完项目并修改 `config.py` 文件中的 `MAIL_PASSWORD` 后，运行 `run.py` 文件即可。



## :large_orange_diamond: Features

#### 1. 登录页面

进入系统后，首先进入登录页面，新用户可点击右上角的 `Register` 按钮进行注册。

![登录页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/登录页面.png?raw=true)



### 2. 注册页面

进入注册页面后，用户需填写必要的信息进行账号注册。

![注册页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E6%B3%A8%E5%86%8C%E9%A1%B5%E9%9D%A2.png?raw=true)



### 3. 找回密码页面

若忘记密码，可点击登录页面下方的 `Click here to reset your password.` 链接，进入找回密码页面，并输入注册时所填电子邮箱地址，系统会发送一封找回密码的邮件至所填邮箱。

![找回密码页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E6%89%BE%E5%9B%9E%E5%AF%86%E7%A0%81%E9%A1%B5%E9%9D%A2.png?raw=true)



### 4. 找回密码邮件

收到找回密码的邮件后，打开邮件，邮件内容会出现两个链接，点击其中一个链接即可进入重设密码页面。

![找回密码邮件.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E6%89%BE%E5%9B%9E%E5%AF%86%E7%A0%81%E9%82%AE%E4%BB%B6.png?raw=true)



### 5. 重设密码页面

进入重设密码页面后，输入密码即可重设。

![重设密码页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E9%87%8D%E8%AE%BE%E5%AF%86%E7%A0%81%E9%A1%B5%E9%9D%A2.png?raw=true)



### 6. 系统主页面

登录成功后进入系统主页面，用户可以发布动态，页面下方可以看到其他用户发布的最新动态。页面右方是用户的个人信息，包括头像、昵称、关注人数和粉丝人数。

![系统主页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E7%B3%BB%E7%BB%9F%E4%B8%BB%E9%A1%B5%E9%9D%A2.png?raw=true)



### 7. 用户个人页面

点击自己头像，进入用户个人页面，可以看到用户自己发布过的动态以及 `Edit Profile` 按钮，点击 `Edit Profile` 按钮即可进入修改头像页面。

![用户个人页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E7%94%A8%E6%88%B7%E4%B8%AA%E4%BA%BA%E9%A1%B5%E9%9D%A2.png?raw=true)



### 8. 修改头像页面

进入修改头像页面，用户可上传图片格式的文件进行修改头像的操作。

![修改头像页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E4%BF%AE%E6%94%B9%E5%A4%B4%E5%83%8F%E9%A1%B5%E9%9D%A2.png?raw=true)



### 9. 其他用户页面

在系统主页面点击其他用户头像即可进入其他用户页面，在此可以看到其他用户发布过的动态，以及进行关注和取关操作。

![其他用户页面.png](https://github.com/Giyn/LightChat/blob/master/Screenshot/%E5%85%B6%E4%BB%96%E7%94%A8%E6%88%B7%E9%A1%B5%E9%9D%A2.png?raw=true)

