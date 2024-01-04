# coding = utf-8
# Author: Zoe
# File: game_page.py
# Time: 2023/10/25 3:07 下午
"""
这里存放一些游戏页面中的通用操作，比如设置页面、胜利页面、开启奖励等
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from base.base import BaseElement
from page.home_page import HomePage
from poco.drivers.unity3d import UnityPoco


# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# from poco.drivers.unity3d import UnityPoco

class GamePage(BaseElement):
    next_button = Template(r"../picture/game_page/next_button.png", record_pos=(-0.227, 0.528), resolution=(1440, 3088))
    setting_button = Template(r"../picture/game_page/setting_button.png", record_pos=(-0.404, -0.906),
                              resolution=(1440, 3088))
    contace_us_button = Template(r"../picture/game_page/contace_us_button.png", record_pos=(-0.316, 0.31),
                                 resolution=(1440, 3088))
    language_button = Template(r"../picture/game_page/language_button.png", record_pos=(-0.318, 0.182),
                               resolution=(1440, 3088))
    setting_close_button = Template(r"../picture/game_page/setting_close_button.png", record_pos=(0.341, -0.497),
                                    resolution=(1440, 3088))
    setting_home_button = Template(r"../picture/game_page/setting_home_button.png", record_pos=(-0.31, -0.081),
                                   resolution=(1440, 3088))
    add_tube_button = Template(r"../picture/game_page/add_tube_button.png", record_pos=(0.391, -0.906),
                               resolution=(1440, 3088))
    debug_win_button = Template(r"../picture/game_page/debug_win_button.png", record_pos=(0.355, -0.181),
                                resolution=(1440, 3088))
    special_play_button = Template(r"../picture/game_page/special_play_button.png", target_pos=6,
                                   record_pos=(-0.24, 0.312), resolution=(1440, 3088))
    game_back_button = Template(r"../picture/game_page/game_back_button.png", record_pos=(-0.41, -0.912),
                                resolution=(1440, 3088))
    quit_button = Template(r"../picture/game_page/quit_button.png", record_pos=(-0.224, 0.1), resolution=(1440, 3088))
    reward_use_button = Template(r"../picture/game_page/reward_use_button.png", target_pos=6,
                                 record_pos=(-0.242, 0.307), resolution=(1440, 3088))
    withdraw_button = Template(r"../picture/game_page/withdraw_button.png", record_pos=(0.249, -0.912),
                               resolution=(1284, 2778))
    # 重开按钮
    restart_button = Template(r"../picture/game_page/restart_button.png", record_pos=(-0.243, -0.906),
                              resolution=(1440, 3088))

    # 英语nextbutton
    victory_english_button = Template(r"../picture/game_page/victory_english_button.png", record_pos=(-0.01, 0.638),
                                      resolution=(1440, 3088))
    # 开宝箱的claim按钮
    claim_button = Template(r"../picture/game_page/claim_button.png", record_pos=(0.001, 0.739),
                            resolution=(1440, 3088))
    # 广告关闭按钮
    ad_close_button = Template(r"../picture/game_page/ad_close_button.png", record_pos=(0.454, -0.953),
                               resolution=(1440, 3088))
    # 新增加的获得道具弹窗中的看广告获得道具
    ad_add_tools = Template(r"../picture/game_page/ad_add_tools.png", record_pos=(-0.111, 0.373),
                            resolution=(1440, 3088))
    # 新增加的获得道具弹窗中的用金币获得道具
    coins_button = Template(r"../picture/game_page/coins_button.png", record_pos=(-0.103, 0.168),
                            resolution=(1440, 3088))
    # 开宝箱的看广告按钮A组
    reward_Ad = Template(r"../picture/game_page/reward_Ad.png", record_pos=(-0.137, 0.569), resolution=(1440, 3088))
    # 设置页面的收藏页面入口
    game_goto_shop_button = Template(r"../picture/game_page/game_goto_shop_button.png", record_pos=(-0.315, 0.069),
                                     resolution=(1440, 3088))
    # debug输入关卡之后的close按钮
    debug_close = Template(r"../picture/game_page/debug_close.png", record_pos=(0.438, -0.956), resolution=(1440, 3088))
    # 设置页面打开音效状态
    setting_sound_open_button = Template(r"../picture/game_page/setting_sound_open_button.png",
                                         record_pos=(-0.141, -0.253),
                                         resolution=(1440, 3088))
    # 设置页面关闭音效状态
    setting_sound_close_button = Template(r"../picture/game_page/setting_sound_close_button.png",
                                          record_pos=(-0.142, -0.255),
                                          resolution=(1440, 3088))
    # 设置页面震动开启状态
    setting_vibration_open_button = Template(r"../picture/game_page/setting_vibration_open_button.png",
                                             record_pos=(0.137, -0.258),
                                             resolution=(1440, 3088))
    # 设置页面震动关闭状态
    setting_vibration_close_button = Template(r"../picture/game_page/setting_vibration_close_button.png",
                                              record_pos=(0.142, -0.258),
                                              resolution=(1440, 3088))

    # 西班牙语调整
    espanol_button = Template(r"../picture/game_page/espanol_button.png", target_pos=6, record_pos=(-0.028, -0.192),
                              resolution=(1440, 3088))
    # 英语调整
    english_button = Template(r"../picture/game_page/english_button.png", target_pos=6, record_pos=(-0.035, -0.322),
                              resolution=(1440, 3088))
    # 语言选择ok
    language_ok_button = Template(r"../picture/game_page/language_ok_button.png", record_pos=(0.001, 0.415),
                                  resolution=(1440, 3088))
    # 零颗星星
    one_to_four_star = Template(r"../picture/game_page/one_to_four_star.png", record_pos=(0.015, 0.138),
                                resolution=(1440, 3088))
    five_star = Template(r"../picture/game_page/five_star.png", record_pos=(-0.011, 0.141), resolution=(1440, 3088))
    zero_star = Template(r"../picture/game_page/zero_star.png", record_pos=(-0.002, 0.142), resolution=(1440, 3088))

    def game_victory(self):
        """
        点击游戏胜利页面的胜利按钮进入下一关
        :return:
        """
        self.sleep_time(6)
        if exists(self.victory_english_button):
            self.image_click(self.victory_english_button)
        else:
            self.image_click([696, 2468])
        self.sleep_time()

        # picList = [self.vtory_english_button, self.claim_button]  # 截图的图片对象列表
        # for pic in picList:
        #     pos = exists(pic)
        #     if pos:
        #         self.image_click(pos)
        return self

    def goto_setting(self):
        """
        从游戏页面进入设置弹窗
        :return:
        """
        if exists(self.setting_button):
            self.image_click(self.setting_button)
        else:
            self.image_click([133, 260])
        self.sleep_time(2)
        return self

    def goto_contact_us(self):
        """
        点击进入邮箱页面
        :return:
        """
        if exists(self.contace_us_button):
            self.image_click(self.contace_us_button)
        else:
            self.image_click([624, 1989])
        self.sleep_time()
        self.system_back(1)
        return self

    def setting_language(self):
        """
        进入设置页面的多语言页面
        :return:
        """
        if exists(self.language_button):
            self.image_click(self.language_button)
        else:
            self.image_click([578, 1821])
        self.sleep_time()
        return self

    def drag_page(self):
        """
        在设置页面的多语言界面滑动，查看剩余的多语言
        :return:
        """
        self.image_swipe([582, 1376], [565, 439])
        self.sleep_time()
        return self

    def setting_close(self):
        """
        点击设置页面的关闭按钮
        :return:
        """
        if exists(self.setting_close_button):
            self.image_click(self.setting_close_button)
        else:
            self.image_click([1179, 815])
            self.image_click([1191, 699])
        self.sleep_time()
        return self

    def goto_home(self):
        """
        从设置页面到主页
        :return:
        """
        if exists(self.setting_home_button):
            self.image_click(self.setting_home_button)
        else:
            self.image_click([717, 1434])
        self.sleep_time()
        return HomePage

    def add_tube(self):
        """
        点击加管道具
        :return:
        """
        if exists(self.add_tube_button):
            self.image_click(self.add_tube_button)
        else:
            print("未找到元素")
            self.image_click([862, 2690])
        return self

    def add_tool_page(self):
        """
        1.0.5新增加弹窗：
        点击获得道具时弹出
        :return:
        """
        self.image_click(self.ad_add_tools)
        self.sleep_time()
        self.image_click([761, 2059])
        return self

    def get_debug(self):
        """
        打开debug与展开debug
        :return:
        """
        self.image_click([640, 228])
        self.sleep_time(1)
        return self

    def debug_win(self):
        """
        点击debug中的胜利按钮
        :return:
        """
        self.sleep_time(2)
        if exists(self.debug_win_button):
            self.image_click(self.debug_win_button)
        else:
            self.image_click([1095, 1087])
        self.sleep_time(4)
        return self

    def debug_goto_normal(self):
        self.image_click([1219, 1415])
        self.sleep_time()
        return self

    def debug_goto_special(self):
        self.image_click([1249, 1198])
        self.sleep_time()
        return self

    def debug_get_level_site(self):
        self.image_click([766, 1592])
        self.sleep_time()
        return self

    def get_normal_ten(self):
        self.image_click([91, 1972])
        self.image_click([1212, 1944])
        self.image_click([1015, 1807])
        return self

    def special_play(self):
        """
        在特殊关卡说明页面点击play，进入特殊关卡
        :return:
        """
        self.sleep_time()
        # poco = UnityPoco()
        # poco("PlayButton").click()
        self.sleep_time()
        self.image_click([937, 1880])
        self.sleep_time()
        # self.image_click([732, 2477])
        # if exists(self.special_play_button):
        #     self.image_click(self.special_play_button)
        # else:
        #     self.image_click([757, 1972])
        # self.sleep_time()
        return self

    def game_back(self):
        """
        弹出退出特殊关卡弹窗
        :return:
        """
        if exists(self.game_back_button):
            self.image_click(self.game_back_button)
        else:
            self.image_click([133, 237])
        self.sleep_time(1)
        return self

    def quit_special(self):
        """
        在特殊关卡退出弹窗点击ok，退出特殊关卡
        :return:
        """
        if exists(self.quit_button):
            self.image_click(self.quit_button)
        else:
            self.image_click([682, 1665])
        self.sleep_time()
        return self

    def reward_page_use(self):
        if not exists(self.reward_use_button):
            self.image_click([737, 2472])
        else:
            self.image_click(self.reward_use_button)
        self.sleep_time()
        return self

    def reward_page_no_use(self):
        self.image_click([737, 2472])
        self.sleep_time()
        self.image_click([604, 2117])
        self.sleep_time()
        return self

    def click_withdraw(self):
        """
        点击撤回道具，弹出无法撤回toast
        :return:
        """
        self.image_click([579, 2714])
        return self

    def click_restart(self):
        """
        点击重开按钮
        :return:
        """
        self.image_click(self.restart_button)
        return self

    def get_level_12(self):
        self.debug_goto_normal().debug_get_level_site().image_click([1253, 2054])
        self.image_click([1253, 2054]).image_click([176, 2074], times=2).image_click([1287, 2300])
        return self

    def ad_close(self):
        self.sleep_time(4)
        if exists(self.victory_english_button):
            return self
        else:
            self.sleep_time(15)
            if exists(self.ad_close_button):
                self.image_click(self.ad_close_button)
            else:
                self.keyevent_command("BACK")
                self.image_click([1384, 152])
        return self

    def victory_ad(self):
        """
        点击胜利之后出现广告，关掉广告之后点击结算页面的next按钮
        :return:
        """
        self.debug_win().ad_close().game_victory()
        return self

    def claim_click(self):
        """
        点击开启宝箱的claim按钮
        :return:
        """
        self.sleep_time()
        self.image_click([742, 2600])
        self.image_click([727, 2615])
        return self

    def double_claim_click(self):
        """
        点击开启双倍宝箱
        :return:
        """
        self.sleep_time()
        if exists(self.reward_Ad):
            self.image_click(self.reward_Ad)
        else:
            self.image_click([712, 2394])
        return self

    def setting_goto_shop(self):
        """
        从设置页面进入shop页面
        :return:
        """
        self.sleep_time(1)
        if exists(self.game_goto_shop_button):
            self.image_click(self.game_goto_shop_button)
        else:
            self.image_click([771, 1627])
        return self

    def debug_input_close(self):
        self.sleep_time(1)
        if exists(self.debug_close):
            self.image_click(self.debug_close)
        else:
            self.image_click([1337, 147])
        return self

    def debug_change_level(self, times, word):
        """
        使用debug进入对应的关卡
        :param times:删除已经存在的关卡
        :param word:输入对应的关卡内容
        :return:
        """
        self.debug_goto_normal().debug_get_level_site().delete_word(times).input_word(word).debug_input_close()
        return self

    def setting_close_sound(self):
        """
        点击关闭音效
        :return:
        """
        if exists(self.setting_sound_open_button):
            self.image_click(self.setting_sound_open_button)
        else:
            self.image_click([505, 1148])
        return self

    def setting_open_sound(self):
        """
        点击开启音效
        :return:
        """
        if exists(self.setting_sound_close_button):
            self.image_click(self.setting_sound_close_button)
        else:
            self.image_click([505, 1148])

        return self

    def setting_close_vibration(self):
        """
        点击关闭震动
        :return:
        """
        if exists(self.setting_vibration_open_button):
            self.image_click(self.setting_vibration_open_button)
        else:
            self.image_click([908, 1158])
        return self

    def setting_open_vibration(self):
        """
        点击开启震动
        :return:
        """
        if exists(self.setting_vibration_close_button):
            self.image_click(self.setting_vibration_close_button)
        else:
            self.image_click([908, 1158])
        return self

    def change_language_espanol(self):
        """
        在语言选择页面点击西班牙语
        :return:
        """
        self.image_click(self.espanol_button)
        return self

    def change_language_english(self):
        """
        在语言选择页面点击英语
        :return:
        """
        self.image_click(self.english_button)
        return self

    def language_ok(self):
        """
        在语言选择页面点击ok
        :return:
        """
        self.image_click(self.language_ok_button)
        return self

    def rating_zero_star(self):
        """
        评分引导零颗星星
        :return:
        """
        self.image_click(self.zero_star)
        return self

    def rating_one_star(self):
        """
        评分引导一颗到四颗星星
        :return:
        """
        self.image_click(self.one_to_four_star)
        return self

    def rating_five_star(self):
        """
        评分引导五颗星星
        :return:
        """
        self.image_click(self.five_star)
        return self

    def click_one_star(self):
        """
        评分引导点击一颗星
        :return:
        """
        self.image_click([294, 1445])
        return self

    def click_five_Star(self):
        """
        评分引导点击五颗星
        :return:
        """
        self.image_click([1106, 1420])
        return self

    def add_coin_click(self):
        """
        点击加金币入口
        :return:
        """
        self.image_click([978, 250])
        self.image_click([1106, 245])
        self.image_click([1125, 226])
        return self

    def add_coin_poco(self):
        add_coin = "GoldIcon"
        self.poco_click(add_coin)
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
    # GamePage().()
