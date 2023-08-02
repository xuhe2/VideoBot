import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEBUG = False


class ZjoocWatchVideo:
    def __init__(self, web: Chrome):
        self.video_time = None
        self.web: Chrome = web

        # 开始按钮的XPATH为`//*[@id="video-show"]/div/div[10]`,暂停的按钮同一个
        self.video_btn_xpath: str = '//*[@id="video-show"]/div/div[10]'

        try:
            time.sleep(2)
            # 等待按钮出现
            WebDriverWait(self.web, 10).until(
                EC.presence_of_element_located((By.XPATH, self.video_btn_xpath))
            )
            self.video_btn = self.web.find_element(By.XPATH, self.video_btn_xpath)
        except:
            print('找不到开始按钮')
            self.video_btn = None
            raise Exception('找不到开始按钮')

    # 获取视频时长
    def get_video_time(self) -> int:
        # 等待时长显示
        time.sleep(2)
        # 显示格式是`00:00/00:00`,第一个`00:00`是当前播放时间,第二个`00:00`是视频总时长
        # 获取时长
        time_str = self.web.find_element(By.XPATH, '//*[@id="video-show"]/div/div[2]/div[8]').text
        # 分割字符串
        time_list = time_str.split('/')
        # 等到now_time和total_time
        now_time = time_list[0]
        total_time = time_list[1]

        # 转换为秒的形式
        def time_to_second(time_str: str) -> int:
            # 分割字符串
            time_list = time_str.split(':')
            # 转换为秒
            return int(time_list[0]) * 60 + int(time_list[1])

        # 转换时间
        total_time = time_to_second(total_time)
        now_time = time_to_second(now_time)

        if DEBUG:
            print('total_time:', total_time)
            print('now_time:', now_time)
        if DEBUG:
            return 1  # DEBUG

        return total_time - now_time

    # 返回章节列表界面
    def return_to_chapter_list_page(self):
        # 返回按钮的XPATH为`//*[@id="app"]/div/section/section/header/span`
        try:
            return_btn = self.web.find_element(By.XPATH, '//*[@id="app"]/div/section/section/header/span')
            return_btn.click()
            # 等待返回
            time.sleep(2)
        except:
            print('找不到返回按钮')
            raise Exception('找不到返回按钮')

    def run(self) -> Chrome:
        # 等待视频可以播放
        time.sleep(5)
        # 开始看视频
        self.video_btn.click()
        # 获取视频时长
        try:
            self.video_time = self.get_video_time()
            print('video time:', self.video_time)
        except Exception as e:
            print('watch video error')
            print(e)
            raise Exception('观看视频出错')

            # 等待视频播放结束
        time.sleep(self.video_time + 5)
        # 返回章节列表界面
        self.return_to_chapter_list_page()
        return self.web
