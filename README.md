# VideoBot
刷zjooc水课视频

可以使用docker部署

可以使用dockerfile部署



# 本地部署

1. 使用以下命令设置环境

```shell
pip install -r requirements.txt
```

2. 安装**chrome**和**chromedriver**.(学习博客配置)

3. 使用`python main.py`运行

* 输入账号密码即可



# 使用docker部署(不再更新,请使用dockerfile部署)

1. 你可以找到我的镜像在docker hub上

```shell
docker search xuhe114514/video_bot
```



2. 拉取

```shell
docker pull xuhe114514/video_bot:1.2
```



3. 进入容器

```shell
sudo docker run -it d4e9df7b7866 /bin/bash
```



4. 运行代码

```shell
./main.sh
```

> 这个SHELL脚本会进入指定目录运行代码



5. 输入**账号,密码**,选择你想要的视频速度(如果选择错误,会默认1倍速),然后等待登陆,选择要观看的课程

> 可以选择多个课程,按选择顺序观看(但是,因为BUG,一般无法正常连续播放)



# 使用Dockerfile部署

1. 构建镜像

```bash
docker build -t video-bot .
```

2. 运行镜像

```bash
sudo docker run --rm -it video-bot
```

> `--rm`代表运行完成之后就删除



# 修改日志

- [x] 添加刷PPT的功能

- [ ] 前端界面里面有个叫做`icon-iconset0387`的CSS选择器,感觉后续可能修改成为新的名字,可能需要修改.

- [x] 添加倍速观看功能



# BUG

* 内存不能正常释放

> 应该是**浏览器的内存**不能正常释放
>
> 会出现代码运行到一半,浏览器关闭了自己,导致代码报错,终止任务.

大概每隔4-5个小时,需要重新启动一遍代码
