from Website.zjooc import Zjooc

username = input('username: ')
password = input('password: ')

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
