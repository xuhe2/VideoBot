import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

debug = True


class ZjoocCaptureList:
    def __init__(self, web: Chrome):
        self.web = web  # 浏览器

        if debug:
            time.sleep(2)
            # 按下`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[2]/button[1]/span`
            # 时,视频列表会出现
            web.find_element(By.XPATH,
                             '//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[2]/button[1]/span') \
                .click()
            time.sleep(1)
            web.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div/div[1]/ul/li[3]/div') \
                .click()

        # 等待视频列表出现
        # 视频的XPATH为`//*[@id="app"]/div/section/main/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/span`
        # 等待视频列表出现
        try:
            time.sleep(2)
            self.video_list = self.web.find_elements(By.XPATH,
                                                     '//*[@id="app"]/div/section/main/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/span')
        except:
            print('找不到视频列表')
            self.video_list = None
            raise Exception('找不到视频列表')

    # 检查列表下的<i>标签的class,来判断是否已经看过
    @staticmethod
    def check_video_status(element) -> bool:
        # 检查是否已经看过
        if element.find_element(By.XPATH, './i').get_attribute('class') == 'complete iconfont icon-shipin':
            return True
        else:
            return False

    def run(self, watched: bool = False):
        watched_list = []
        unwatched_list = []
        # 检查是否被看过
        for video in self.video_list:
            if ZjoocCaptureList.check_video_status(video):
                watched_list.append(video)
            else:
                unwatched_list.append(video)

        if watched:
            return watched_list
        else:
            return unwatched_list


if __name__ == '__main__':
    pass
