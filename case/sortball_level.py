from airtest.cli.parser import cli_setup
from airtest.core.api import *
from page.gameplay_guide_page import GamePlayGuide
from page.privacy_page import PrivacyPage
from base.base import BaseElement
from page.game_page import GamePage
from page.home_page import HomePage
from page.shop_page import ShopPage

# 暂时关闭截图
ST.SAVE_IMAGE = False
# 设置全局的截图精度为90
ST.SNAPSHOT_QUALITY = 90


class SortBallLevel:
    number1 = [81, 1962]
    number2 = [184, 1979]
    number3 = [314, 1942]
    number4 = [449, 1962]
    number_5 = [584, 1958]
    number_6 = [695, 1975]
    number_7 = [830, 1975]
    number_8 = [948, 1962]
    number_9 = [1083, 1979]
    number_0 = [1214, 1970]
    iphone = "13max"

    def __init__(self):
        self.GamePlayGuide = GamePlayGuide
        self.PrivacyPage = PrivacyPage
        self.BaseElement = BaseElement()
        self.GamePage = GamePage
        self.HomePage = HomePage
        self.ShopPage = ShopPage

    def get_normal_level3(self):
        normal_level3 = "普通关卡第三关"

        self.PrivacyPage().first_open().click_accept()
        self.GamePlayGuide().first_guide_step1().first_guide_step2()
        self.GamePage().game_victory().get_debug().get_debug().debug_win().game_victory().get_snapshot(normal_level3,
                                                                                                       self.iphone)
        return self

    def get_debug(self):
        """
        打开debug
        :return:
        """
        self.GamePage().game_victory().get_debug().get_debug()
        return self

    def get_normal_level_number(self):
        """
        得到普通模式对应的输入框
        :return:
        """
        self.BaseElement.image_click([1091, 1202])
        self.BaseElement.sleep_time(1)
        self.BaseElement.image_click([609, 1369])
        self.BaseElement.sleep_time(1)
        self.BaseElement.image_click([1214, 2310], times=3)
        return self

    def get_special_level_number(self):
        self.BaseElement.image_click([1206, 1198])
        self.BaseElement.sleep_time(1)
        self.BaseElement.image_click([609, 1369])
        self.BaseElement.sleep_time(1)
        self.BaseElement.image_click([1214, 2310], times=3)
        return self


    def get_level_number(self, number):
        """
        在输入框输入对应的关卡
        :param number:
        :return:
        """
        self.BaseElement.image_click(number)
        self.BaseElement.sleep_time()
        return self

    def click_yes(self):
        """
        输入关卡后点击确认
        :return:
        """
        self.BaseElement.image_click([838, 1508])
        self.BaseElement.sleep_time()
        return self

    def get_normal5(self):
        normal_5 = "普通关卡第五关"
        self.get_normal_level_number().get_level_number(self.number4).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_normal10(self):
        normal_5 = "普通关卡第11关"
        self.get_normal_level_number().get_level_number(self.number1).get_level_number(self.number_0).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_normal181(self):
        normal_5 = "普通关卡第181关"
        self.get_normal_level_number().get_level_number(self.number1).get_level_number(self.number_8).get_level_number(
            self.number1).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_normal182(self):
        normal_5 = "普通关卡第182关"
        self.get_normal_level_number().get_level_number(self.number1).get_level_number(self.number_8).get_level_number(
            self.number2).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_special16(self):
        normal_5 = "特殊关第16关"
        self.get_special_level_number().get_level_number(self.number1).get_level_number(self.number_6).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_special14(self):
        normal_5 = "特殊关第14关"
        self.get_special_level_number().get_level_number(self.number1).get_level_number(self.number3).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_special10(self):
        normal_5 = "特殊关第10关"
        self.get_special_level_number().get_level_number(self.number_9).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self


    def get_special20(self):
        normal_5 = "特殊关第21关"
        self.get_special_level_number().get_level_number(self.number2).get_level_number(self.number_0).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_special21(self):
        normal_5 = "特殊关第22关"
        self.get_special_level_number().get_level_number(self.number2).get_level_number(self.number2).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_special19(self):
        normal_5 = "特殊关第20关"
        self.get_special_level_number().get_level_number(self.number1).get_level_number(self.number_9).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self

    def get_special37(self):
        normal_5 = "特殊关第38关"
        self.get_special_level_number().get_level_number(self.number3).get_level_number(self.number_7).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self


    def get_special45(self):
        normal_5 = "特殊关第46关"
        self.get_special_level_number().get_level_number(self.number4).get_level_number(self.number_5).click_yes()
        self.BaseElement.get_snapshot(normal_5, self.iphone)
        self.BaseElement.sleep_time(1)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    (SortBallLevel().get_normal_level3().get_normal5().get_normal10().get_normal181().get_normal182().get_special16().
     get_special14().get_special10()).get_special20().get_special21(). get_special19().get_special37().get_special45()
    # SortBallLevel().get_special20().get_special21(). get_special19().get_special37().get_special45()
