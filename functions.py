import time
import os

def start(name):
    print(f"USER NAME: {name}")
    print(f"{name}님 환영합니다!!!")


def game():
    farm = 1
    print(f"농장: {farm}")
    mmoney = 0
    while True:
        mmoney += 100
        print(f"돈: {mmoney}")
        time.sleep(1)
        return os.system("clear")


