# coding = utf-8
# Author: Zoe
# File: shop_page.py
# Time: 2023/10/25 3:10 下午
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from base.base import BaseElement


class ShopPage(BaseElement):
    background_button = Template(r"../picture/shop_page/background_button.png", record_pos=(-0.008, -0.758),
                                 resolution=(1440, 3088))
    unlocked_tube = Template(r"../picture/shop_page/unlocked_tube.png", record_pos=(-0.177, -0.021),
                             resolution=(1440, 3088))
    ball_button = Template(r"../picture/shop_page/ball_button.png", record_pos=(0.311, -0.751), resolution=(1440, 3088))
    get_coins_button = Template(r"../picture/shop_page/get_coins_button.png", record_pos=(0.183, 0.429),
                                resolution=(1440, 3088))
    back_home_button = Template(r"../picture/shop_page/back_home_button.png", record_pos=(-0.382, -0.906),
                                resolution=(1440, 3088))
    get_ad_coins = Template(r"../picture/shop_page/get_ad_coins.png", record_pos=(0.058, 0.776),
                            resolution=(1440, 3088))
    # 点击购买皮肤
    buy_click_button = Template(r"../picture/shop_page/buy_click_button.png", record_pos=(0.186, 0.439),
                                resolution=(1440, 3088))
    # 点击需要看广告的皮肤
    ad_claim_button = Template(r"../picture/shop_page/ad_claim_button.png", record_pos=(-0.182, 0.086),
                               resolution=(1440, 3088))
    # 得到金币的ad按钮
    get_coin_ad = Template(r"../picture/game_page/get_coin_ad.png", record_pos=(-0.166, 0.086), resolution=(1440, 3088))

    def lock_tube(self):
        if exists(self.unlocked_tube):
            self.image_click(self.unlocked_tube)
        else:
            self.image_click([422, 1532])
        return self

    def goto_background(self):
        """
        从管的商店页面到背景商店页面
        :return:
        """
        if exists(self.background_button):
            self.image_click(self.background_button)
        else:
            self.image_click([728, 456])
        self.sleep_time(2)
        return self

    def goto_ball(self):
        """
        进入商店页面的球页面
        :return: 
        """
        if exists(self.ball_button):
            self.image_click(self.ball_button)
        else:
            self.image_click([895, 387])
        self.sleep_time()
        return self

    def get_coins(self):
        """
        点击获得金币弹窗
        :return: 
        """
        if exists(self.get_coins_button):
            self.image_click(self.get_coins_button)
        else:
            self.image_click([965, 2157])
        self.sleep_time()
        return self

    def shop_back_home(self):
        """
        从商店页面回到首页
        :return:
        """
        if exists(self.back_home_button):
            self.image_click(self.back_home_button)
        else:
            self.image_click([150, 254])
        self.sleep_time()
        return self

    def ad_coins_click(self):
        """
        点击购买200金币弹窗
        :return:
        """
        self.sleep_time()
        if exists(self.get_ad_coins):
            self.image_click(self.get_ad_coins)
        else:
            self.image_click([752, 2644])
        return self

    def buy_click(self):
        """
        点击购买管皮肤/主题/球皮肤
        :return:
        """
        if exists(self.buy_click_button):
            self.image_click(self.buy_click_button)
        else:
            self.image_click([1001, 2179])
        return self

    def ad_claim(self):
        if exists(self.ad_claim_button):
            self.image_click(self.ad_claim_button)
        else:
            self.image_click([485, 1668])
        return self

    def click_get_coin_ad(self):
        if exists(self.get_coin_ad):
            self.image_click(self.get_coin_ad)
        else:
            self.image_click([653, 1641])
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])
        ShopPage().ad_coins_click()
