import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SLEEP_TIME = 3


class ZjoocWatchPPT:
    def __init__(self, web: Chrome):
        self.web: Chrome = web  # 存储当前的界面

        # 获取URL
        url: str = self.web.current_url
        # 使用URL最后一段
        url_last_part: str = url.split('/')[-1]
        self.PPT_button_xpath = f'//*[@id="pane-{url_last_part}"]/div/div/div[2]/button/span'

    def return_to_chapter_list_page(self):
        # 返回按钮的XPATH为`//*[@id="app"]/div/section/section/header/span`
        try:
            return_btn = self.web.find_element(By.XPATH, '//*[@id="app"]/div/section/section/header/span')
            return_btn.click()
            # 等待返回
            time.sleep(SLEEP_TIME)
        except:
            print('找不到返回按钮')
            raise Exception('找不到返回按钮')

    def click_ppt_button(self):
        try:
            ppt_btn = self.web.find_element(By.XPATH, self.PPT_button_xpath)
            ppt_btn.click()
            # 等待返回
            time.sleep(SLEEP_TIME)
        except:
            print('找不到ppt按钮')
            raise Exception('找不到ppt按钮')

    def run(self) -> Chrome:
        time.sleep(SLEEP_TIME)  # 等待
        self.click_ppt_button()  # 点击完成按钮
        self.return_to_chapter_list_page()  # 回到章节列表页面
        print('PPT观看完成')

        return self.web
