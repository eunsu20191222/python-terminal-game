import time
import os

def start(name):
    print(f"USER NAME: {name}")
    print(f"{name}님 환영합니다!!!")


def game(user):
    farm = 1
    mmoney = 0
    while True:
        mmoney += 100
        money = mmoney
        print(f"{user}님의 자산")
        print(f"농장: {farm}")
        print(f"돈: {money}")
        print("농장: 100원")
        print("농장을 사려면 n를 눌러주세요")
        print("게임을 나갈려면 g를 입력해 주세요")
        ask = input(": ")
        if ask == "n":
            if money > 100:
                farm += 1
                money -= 100
        elif ask == "g":
            break
        time.sleep(1)
        os.system("clear")

        


