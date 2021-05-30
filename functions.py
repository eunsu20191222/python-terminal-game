import time
import os

def start(name):
    print(f"USER NAME: {name}")
    print(f"{name}님 환영합니다!!!")


def game():
    farm = 1
    mmoney = 0
    while True:
        mmoney += 100
        money = mmoney
        print(f"농장: {farm}")
        print(f"돈: {money}")
        time.sleep(1)
        os.system("clear")

        


