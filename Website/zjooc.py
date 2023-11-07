from selenium.webdriver import Chrome

from Login.zjooc import ZjoocLogin
from ChooseVideo.zjooc import ZjoocChooseVideo


class Zjooc:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def run(self) -> bool:
        # 登录
        try:
            web = ZjoocLogin(headless=False, mute_audio=True, no_log=True).run(self.username, self.password)
        except Exception as e:
            print(e)
            return False

        # 选择视频
        try:
            ZjoocChooseVideo(web).run()
        except Exception as e:
            print(e)
            return False

        return True
