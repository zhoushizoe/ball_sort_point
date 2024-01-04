from airtest.cli.parser import cli_setup
from airtest.core.api import *
import subprocess
import fcntl

# 连接iOS设备
if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
        "ios:///http://127.0.0.1:8300", ])
ballsort_ios_package = "ios.game.ballsort.inner"


class IOSLogCatch:
    """
    1.开始记录日志
    2.操作步骤
    3.过滤日志
    4.输出
    """

    def __init__(self):
        self.process = None

    def start(self):
        """
        开始记录日志
        :return:
        """
        try:
            self.process = subprocess.Popen(["idevicesyslog"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            fd = self.process.stdout.fileno()
            flags = fcntl.fcntl(fd, fcntl.F_GETFL)
            fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

        except subprocess.CalledProcessError as e:
            print("Error:", e)

    def close(self):
        """
        关闭日志按钮
        :return:
        """
        self.process.terminate()

    def read(self):
        """
        读取日志
        :return:
        """
        global log
        result = self.process.stdout.readlines()
        for line in result:
            log = line.decode("utf-8").strip()

            if "FACEBOOK     : EVENT_SEND       : settings_home_click" in log:
                print("2")
                print(log)
        return log


log_catch = IOSLogCatch()
# 开始读取日志
print("Start")
log_catch.start()
# 操作步骤
touch([394, 1938])
log_catch.read()
log_catch.close()
print("End")