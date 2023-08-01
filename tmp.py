import time

from Login.zjooc import ZjoocLogin
from WatchVideo import zjooc
from ChooseVideo.zjooc import ZjoocCaptureList

if __name__ == '__main__':
    test_login = ZjoocLogin()
    # # 获取登陆按钮
    # loginButton = test.web.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/div[2]/a')
    # # 点击登陆按钮
    # loginButton.click()

    # # 暂停直到我的`/html/body/div[1]/div[2]/div[2]/div[3]/button`的按钮的text是`登录`才继续运行
    # WebDriverWait(test.web, 10).until(
    #     EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/button'), '登录')
    # )

    test_login.run('18968683833', '200310230015xh')

    # 按下`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[2]/button[1]/span`按钮
    test_capture_list = ZjoocCaptureList(test_login.web)
    list = test_capture_list.run()
    print(list)
    print(len(list))

    # 在当前界面停下
    input('按下回车键继续...')

# web: Chrome = Chrome()
# web.set_window_size(1920, 1080)  # 设置浏览器窗口大小
#
# url: str = 'https://www.zjooc.cn/'
# web.get(url)  # 访问网址
#
# # 获取登陆按钮
# loginButton = web.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/div[2]/a')
# # 点击登陆按钮
# loginButton.click()
#
# # 暂停直到我的`/html/body/div[1]/div[2]/div[2]/div[3]/button`的按钮的text是`登录`才继续运行
# WebDriverWait(web, 10).until(
#     EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/button'), '登录')
# )
#
# # 截图
# web.save_screenshot('zjooc.png')
# # 截取验证码图片
# screenshot('zjooc.png')
#
# # 找到账号输入框,`id="login_name"`
# username_entry = web.find_element(By.ID, 'login_name')
#
# # 找到验证码输入框,`name="captchaCode"`
# captcha_entry = web.find_element(By.NAME, 'captchaCode')
# # 输入验证码
# captcha_entry.send_keys(captcha_solver('zjooc.png'))
#
# # 在当前界面暂停
# input('请按回车键退出')
# web.quit()  # 关闭浏览器
