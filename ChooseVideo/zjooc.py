import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from WatchVideo.zjooc import ZjoocWatchVideo

DEBUG = False

SLEEP_TIME = 5

class ZjoocCaptureList:
    def __init__(self, web: Chrome):
        self.web = web  # 浏览器

        if DEBUG:
            time.sleep(SLEEP_TIME)
            # 按下`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[2]/button[1]/span`
            # 时,视频列表会出现
            web.find_element(By.XPATH,
                             '//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[2]/div/div[2]/div[3]/div[2]/button[1]/span') \
                .click()
            time.sleep(SLEEP_TIME)
            web.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div/div[1]/ul/li[3]/div') \
                .click()

        # 等待视频列表出现
        # 视频的XPATH为`//*[@id="app"]/div/section/main/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/span`
        # 等待视频列表出现
        try:
            if DEBUG:
                time.sleep(SLEEP_TIME)

            self.video_list = self.web.find_elements(By.XPATH,
                                                     '//*[@id="app"]/div/section/main/div/div/div[2]/div/div[2]/div[1]/div/div/div/div/div/div/div/span')
        except:
            print('找不到视频列表')
            self.video_list = []

    # 检查列表下的<i>标签的class,来判断是否已经看过
    @staticmethod
    def check_video_status(element: WebElement) -> bool:
        # 检查是否已经看过
        if 'complete' in element.find_element(By.XPATH, './i').get_attribute('class'):
            return True
        else:
            return False

    def run(self, watched: bool = False, is_all: bool = False) -> list[WebElement]:
        if is_all:  # 返回所有视频
            return self.video_list

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


class ZjoocChooseVideo:
    def __init__(self, web: Chrome):
        self.class_list = None
        self.web = web  # 浏览器
        self.class_page = 'https://www.zjooc.cn/ucenter/student/course/build/list'  # 课程列表页面
        self.queue = []  # 课程列表

    def get_class_list(self) -> list[WebElement]:
        # 回到课程列表页面
        self.return_to_class_page()
        # 获取课程列表
        # 课程列表的`class`是`main_list`
        try:
            self.class_list = self.web.find_elements(By.CLASS_NAME, 'main_list')
        except Exception as e:
            print('找不到课程列表')
            print(e)
            self.class_list = []
        return self.class_list

    @staticmethod
    def get_class_name(class_element: WebElement) -> str:
        # 元素的XPATH为`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[1]`
        # 完整的XPATH为`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[1]/div/div[2]/div[1]/h6`
        return class_element.find_element(By.XPATH, './div/div[2]/div[1]/h6').text

    def go_to_capture_page(self, class_element: WebElement):
        """error code,使用XPATH查找会出问题"""
        # # 元素的XPATH为`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[1]`
        # # 按钮的XPATH为`//*[@id="app"]/div/section/main/div/div[2]/div/div[3]/div[1]/div/div[2]/div[3]/div[2]/button[1]/span`
        # class_element.find_element(By.XPATH, './div/div[2]/div[3]/div[2]/button[1]/span').click()
        """error code"""

        # 按钮的内容是`进入学习`
        class_element.find_element(By.XPATH, './/button[.//span[text()="进入学习"]]').click()
        time.sleep(SLEEP_TIME)  # 等待页面加载
        # 再按下`//*[@id="app"]/div/section/main/div/div/div[1]/ul/li[3]/div/span`
        self.web.find_element(By.XPATH, '//*[@id="app"]/div/section/main/div/div/div[1]/ul/li[3]/div/span') \
            .click()
        time.sleep(SLEEP_TIME)  # 等待页面加载

    # 打印课程列表
    def print_class_list(self):
        self.get_class_list()
        print('-' * 50)
        for index, _ in enumerate(self.class_list):
            print('[', end='')
            print(f'{index}.{ZjoocChooseVideo.get_class_name(_)}', end='')
            print(']')
        print('-' * 50)

    def return_to_class_page(self):
        self.web.get(self.class_page)
        # 等待页面加载
        time.sleep(SLEEP_TIME)
        # 调整为每面显示20个课程
        # 按下`//*[@id="app"]/div/section/main/div/div[2]/div/div[4]/div/span[2]/div/div/input`
        self.web.find_element(By.XPATH,
                              '//*[@id="app"]/div/section/main/div/div[2]/div/div[4]/div/span[2]/div/div/input') \
            .click()
        time.sleep(SLEEP_TIME)
        # 按下`/html/body/div[2]/div[1]/div[1]/ul/li[4]`
        self.web.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[4]').click()
        time.sleep(SLEEP_TIME)

    def run(self):
        self.print_class_list()  # 打印课程列表

        # 选择课程,输入序号,直到回车结束
        print("""
        !!!输入序号,直接回车代表结束!!!
        """)
        while True:
            try:
                index = input('输入序号:')

                if index.strip() == '':  # 如果输入为空,则结束
                    break

                index = int(index)  # 转换为整数
                if len(self.class_list) > index >= 0:
                    self.queue.append(index)
                else:
                    print('输入错误,请重新输入')
            except ValueError:
                print('输入错误,请重新输入')

        while len(self.queue) > 0:
            print('-' * 50)
            print('正在观看课程:[', ZjoocChooseVideo.get_class_name(self.class_list[self.queue[0]]), ']...')

            self.watch_class(self.class_list[self.queue.pop(0)])  # 播放课程

            print('!!!课程观看完毕!!!')
            print('-' * 50)

            self.get_class_list()  # 更新课程列表

    def watch_class(self, class_element: WebElement):
        # 前往课程页面
        self.go_to_capture_page(class_element)
        # 获取视频列表
        video_list = ZjoocCaptureList(self.web).run()
        # 播放视频
        while True:
            capture_list = ZjoocCaptureList(self.web).run()

            if len(capture_list) == 0:  # 没有视频了
                break

            item = capture_list[0]  # 选择第一个视频
            print('capture name: [', item.text, ']')
            # 点击
            item.click()
            test_watch_video = ZjoocWatchVideo(self.web)  # DEBUG
            self.web = test_watch_video.run()
            print('the video that unwatched: ', len(capture_list) - 1)
