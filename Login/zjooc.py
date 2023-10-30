import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Login import captcha_solver
from Login import save_image_from_base64


class ZjoocLogin:
    def __init__(self, headless: bool = False, mute_audio: bool = False, no_log: bool = False):
        # 使用headless无界面浏览器模式
        chrome_options: Options = Options()  # 实例化Option对象
        if headless:  # 设置headless模式
            chrome_options.add_argument('--headless')  # 把Chrome浏览器设置为静默模式
        if mute_audio:  # 设置静音模式
            chrome_options.add_argument('--mute-audio')
        if no_log:  # 设置日志不打印
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

        """
        在linux上运行的时候，需要一些额外的配置
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('--disable-browser-side-navigation')
        chrome_options.add_argument('enable-automation')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('enable-features=NetworkServiceInProcess')
        """

        self.web = Chrome(options=chrome_options)  # 设置引擎为Chrome，在后台默默运行
        # !注意:一定要设置窗口大小,否则按钮无法按下!
        self.web.set_window_size(1920, 1080)  # 设置浏览器窗口大小

        self.url: str = 'https://www.zjooc.cn/'
        self.web.get(self.url)  # 访问网址

    def check_captcha(self) -> bool:
        time.sleep(5)
        # 如果不存在登录按钮就是登陆成功
        # 登录按钮的`class = "dologin"`
        try:
            self.web.find_element(By.CLASS_NAME, 'dologin')
            return False
        except:
            return True

    # 输入账户信息
    def input_account_info(self, username: str, password: str) -> bool:
        # 获取验证码图片的base64编码
        img_base64 = (self.web.find_element(By.XPATH,
                                            '/html/body/div[1]/div[2]/div[2]/div[3]/div[3]/img').get_attribute('src'))
        # 保存验证码图片
        save_image_from_base64(img_base64, 'zjooc.png')

        try:
            # 找到账号输入框,`id="login_name"`
            username_entry = self.web.find_element(By.ID, 'login_name')
            # 输入账号
            username_entry.send_keys(username)

            # 找到密码输入框,`id="password"`
            userpassword_entry = self.web.find_element(By.ID, 'password')
            # 输入密码
            userpassword_entry.send_keys(password)

            # 找到验证码输入框,`name="captchaCode"`
            captcha_entry = self.web.find_element(By.NAME, 'captchaCode')
            # 输入验证码
            captcha_entry.send_keys(captcha_solver('zjooc.png'))

            return True
        except:
            return False

    # 进入登录界面
    def enter_login_page(self) -> bool:
        try:
            # 获取登陆按钮,内容是`请登录`
            login_button = self.web.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/div[2]/a')
            # 点击登陆按钮
            login_button.click()
            # 暂停直到我的`/html/body/div[1]/div[2]/div[2]/div[3]/button`的按钮的text是`登录`才继续运行
            WebDriverWait(self.web, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/button'),
                                                 '登录')
            )
            return True
        except Exception as e:
            print(e)
            return False

    # 回到初始界面
    def back_to_home_page(self) -> None:
        self.web.get(self.url)

    # 退出登录
    def logout(self) -> bool:
        # 推出按钮的`//*[@id="app"]/section/header/div/div[1]/div/div[2]/div/a[2]`
        try:
            # 回到初始界面
            self.back_to_home_page()
            # 获取退出按钮
            logout_button = self.web.find_element(By.XPATH,
                                                  '//*[@id="app"]/section/header/div/div[1]/div/div[2]/div/a[2]')
            # 点击退出按钮
            logout_button.click()
            # 直到`//*[@id="app"]/section/header/div/div[1]/div/div[2]/a`的内容是`请登录`才继续运行
            WebDriverWait(self.web, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/div[2]/a'),
                                                 '请登录')
            )
            return True
        except:
            return False

    def run(self, username: str, password: str, max_login_num: int = 100) -> Chrome:
        flag = False  # 是否登陆成功
        index: int = 0  # 登陆次数

        while not flag and index < max_login_num:
            index += 1

            if not self.enter_login_page():
                print('第', index, '次登陆失败')  # 登陆失败
                continue

            try:
                # 等待3秒
                time.sleep(3)
                self.input_account_info(username, password)  # 输入账户信息

                # 找到登陆按钮,`/html/body/div[1]/div[2]/div[2]/div[3]/button`,点击登陆
                login_button = self.web.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/button')
                login_button.click()

                if self.check_captcha():
                    flag = True
                    print('username:', username, 'password:', password, '第', index, '次登陆成功')
                    return self.web

            except Exception as e:
                pass

            self.back_to_home_page()  # 回到初始界面
            print('username:', username, 'password:', password, '第', index, '次登陆失败')  # 登陆失败

        raise Exception('登陆失败')


if __name__ == '__main__':
    test = ZjoocLogin()
    # # 获取登陆按钮
    # loginButton = test.web.find_element(By.XPATH, '//*[@id="app"]/section/header/div/div[1]/div/div[2]/a')
    # # 点击登陆按钮
    # loginButton.click()

    # # 暂停直到我的`/html/body/div[1]/div[2]/div[2]/div[3]/button`的按钮的text是`登录`才继续运行
    # WebDriverWait(test.web, 10).until(
    #     EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/button'), '登录')
    # )

    # username = input('请输入账号:')
    # password = input('请输入密码:')

    test.login('18968683833', '200310230015xh')

    # 在当前界面停下
    input('按下回车键退出...')

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
