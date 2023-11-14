# coding = utf-8
# Author: Zoe
# File: base.py
# Time: 2023/10/25 2:47 下午
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.ios import iosPoco

name = "你好"
language = "英语"


class BaseElement:
    # poco = UnityPoco()

    # 使用图像识别点击

    def image_click(self, image, times=1):
        touch(image, times)

        # 使用图像识别拖动

    def image_swipe(self, place, to):
        swipe(place, to)

    # 截图
    def get_snapshot(self, filename, language):
        snapshot(filename=language + filename + ".png")
        return self

    # 停止游戏
    def stop_app(self, package):
        stop_app(package)
        sleep(2)

    def start_app(self, package):
        start_app(package)
        sleep(5)

    # 删除输入的文字
    def delete_word(self, times):
        for i in range(times):
            keyevent("KEYCODE_DEL")
            sleep(0.5)

    # 输入所需要的文字
    def input_word(self, word):
        text(word)
        sleep(0.5)

    # 睡眠的时间
    def sleep_time(self, second=2):
        sleep(second)
        return self

    # 设备连接及设备名称
    def devices_contact(self, devices):
        if not cli_setup():
            auto_setup(__file__, logdir=True, devices=[
                devices, ])

    # 物理back键
    def system_back(self, times):
        for i in range(times):
            keyevent("back")
            self.sleep_time()

    def ios_open_app(self, app_name):
        """
        airtest中的[start_app]不支持iOS17
        游戏的名称永远是英文的，所以使用poco的方式打开应用
        :param app_name:app在首页显示的应用名字
        :return:
        """
        poco = iosPoco()
        poco(app_name).click()
        return self


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/R3CW10C3D9N?cap_method=ADBCAP&touch_method=MAXTOUCH&", ])

    BaseElement().get_snapshot(name, language)
