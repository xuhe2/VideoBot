# VideoBot
刷zjooc水课视频

可以使用docker部署

* 没有设置倍速,可以添加这个功能(但是我懒)



# 本地部署

1. 使用以下命令设置环境

```shell
pip install -r requirements.txt
```

2. 安装**chrome**和**chromedriver**.(学习博客配置)

3. 使用`python main.py`运行

* 输入账号密码即可



# 使用docker部署

> 作者是个大FW,只会打成简单的docker镜像,不是docker file

1. 你可以找到我的镜像在docker hub上

```shell
docker search xuhe114514/video_bot
```



2. 拉取

```shell
docker pull xuhe114514/video_bot
```



3. 运行

```shell
docker run -it 646b49740891 /bin/bash
```





# 修改日志

- [x] 添加刷PPT的功能

- [ ] 前端界面里面有个叫做`icon-iconset0387`的CSS选择器,感觉后续可能修改成为新的名字,可能需要修改.

