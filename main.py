import WatchVideo.zjooc
from Website.zjooc import Zjooc

username = input('username: ')
password = input('password: ')

# 选择倍速
print('please input the index to choose the video speed:')
speed_map = {
    '0': 0.5,
    '1': 1.0,
    '2': 1.25,
    '3': 1.5,
    '4': 2.0,
    '5': 4.0
}
for i in range(6):
    print('[' + str(i) + ']. ' + str(speed_map[str(i)]) + 'x')
index = input('index: ')
# 如果超过范围
if int(index) > 5 or int(index) < 0:
    print('index out of range!use 1.x')
    index = '1'
WatchVideo.zjooc.VIDEO_SPEED = speed_map[index]

website = Zjooc(username, password)
flag = website.run()

print('><' * 20)
print('username: ', username)
print('password: ', password)
if flag:
    print('!finished!')
else:
    print('!failed!')
print('><' * 20)
