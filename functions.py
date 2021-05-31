import time
import os

def start(name):
    print(f"USER NAME: {name}")
    print(f"{name}님 환영합니다!!!")

def n(farm):
    farm += 1
    

def game(user):
    farms = 1
    mmoney = 0
    while True:
        mmoney += 100
        money = mmoney
        print(f"{user}님의 자산")
        print(f"농장: {farm}")
        print(f"돈: {money}")
        print("농장: 100원")
        ask = input(": ")
        if ask == n:
            time.sleep(1)
            n(farms)
            farms += 1
            farm = farms
        time.sleep(1)
        os.system("clear")




        


