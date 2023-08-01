import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # 从options模块中调用Options类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ZjoocWatchVideo:
    def __init__(self, web: Chrome):
        self.video_time = None
        self.web: Chrome = web

        # 开始按钮的XPATH为`//*[@id="video-show"]/div/div[10]`,暂停的按钮同一个
        self.video_btn_xpath: str = '//*[@id="video-show"]/div/div[10]'
        # 当按钮的`style`是
        # `width: 80px; height: 80px; border-radius: 50%; position: absolute; display: block; cursor: pointer; z-index: 996; left: 762px; top: 381px;`
        # 时,按钮是暂停状态
        self.stop_btn_style: str = 'width: 80px; height: 80px; border-radius: 50%; position: absolute; display: block; cursor: pointer; z-index: 996; left: 762px; top: 381px;'
        # 当按钮的`style`是
        # `width: 80px; height: 80px; border-radius: 50%; position: absolute; display: none; cursor: pointer; z-index: 996; left: 762px; top: 381px;`
        # 时,按钮是播放状态
        self.play_btn_style: str = 'width: 80px; height: 80px; border-radius: 50%; position: absolute; display: none; cursor: pointer; z-index: 996; left: 762px; top: 381px;'

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

    # # 检查是否播放结束
    # def check_video_end(self) -> bool:
    #     if self.video_btn.get_attribute('style') == self.stop_btn_style:
    #         return True
    #     else:
    #         return False
    #
    # # 直到视频播放结束
    # def wait_video_end(self):
    #     time.sleep(5)  # 等待视频加载
    #     while not self.check_video_end():
    #         time.sleep(1)
    #     print('视频播放结束')

    # 获取视频时长
    def get_video_time(self) -> int:
        # 时长显示的XPATH为`//*[@id="video-show"]/div/div[2]/div[8]`
        # 显示格式是`00:00/00:00`,第一个`00:00`是当前播放时间,第二个`00:00`是视频总时长
        # 获取时长
        time_str = self.web.find_element(By.XPATH, '//*[@id="video-show"]/div/div[2]/div[8]')
        # 分割字符串
        time_list = time_str.text.split('/')
        # 获取总时长
        time_str = time_list[1]
        # 分割字符串
        time_list = time_str.split(':')
        # 计算总时长
        time_int = int(time_list[0]) * 60 + int(time_list[1])
        # 如果时长为0,则抛出异常
        if time_int == 0:
            raise Exception('获取视频时长失败')
        return time_int

    # 返回章节列表界面
    def return_to_chapter_list_page(self):
        # 返回按钮的XPATH为`//*[@id="app"]/div/section/section/header/span`
        try:
            return_btn = self.web.find_element(By.XPATH, '//*[@id="app"]/div/section/section/header/span')
            return_btn.click()
        except:
            print('找不到返回按钮')
            raise Exception('找不到返回按钮')

    def run(self) -> bool:
        # 等待视频可以播放
        time.sleep(5)
        # 获取视频时长
        try:
            self.video_time = self.get_video_time()
        except:
            print('获取视频时长失败')
            return False

        # 开始看视频
        self.video_btn.click()
        # 等待视频播放结束
        time.sleep(self.video_time + 5)
        return True
