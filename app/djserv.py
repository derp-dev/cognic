from django import *
import os
import sys
import time


class djServ:
    def __init__(self, path):
        self.path = path

    def start(self):
        os.system("cd " + self.path + " && python3 manage.py runserver")

    def stop(self):
        os.system("killall python3")

    def restart(self):
        os.system("killall python3")
        time.sleep(1)
        os.system("cd " + self.path + " && python3 manage.py runserver")

    def status(self):
        os.system("ps -aux | grep python3")
        
    def exit(self):
        sys.exit()

    def help(self):
        print("start - start server")
        print("stop - stop server")
        print("restart - restart server")
        print("status - status server")
        print("help - help")
        print("exit - exit")