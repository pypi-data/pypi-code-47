"""高级模式"""
import ddcmaker
import subprocess


class ad_mode(object):

    def __init__(self, timeout=30):
        self.__version__ = ddcmaker.__version__
        self.Xpath = ""
        self.sleeptime = timeout
        self.name = ""
        self.list = []

    def run(self):
        from ddcmaker.public import killprocess
        from ddcmaker.linux.armv7l.get_equipment_type import get_init_func
        # for s in self.list:
        #     killprocess.kill_process(s)
        cmd = self.Xpath + self.name
        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            try:
                proc.communicate(timeout=self.sleeptime)
            except Exception as e:
                print("超时中断动作，该动作默认执行最长时间为"+str(self.sleeptime)+"秒")
        except Exception as e:
            print(e)
        # time.sleep(self.sleeptime)
        finally:
            killprocess.kill_process(cmd.split(" ")[1])
            get_init_func()

