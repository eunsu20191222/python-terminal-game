import time
import os

def clear():
    return os.system("clear")

def start(name):
    print(f"USER NAME: {name}")
    print(f"{name}님 환영합니다!!!")

def money(user):
    mmoney = 0
    while True:
        mmoney += 100
        money = mmoney
        f = open("money.txt", "w")
        f.write(f"{user}님의 자산 \n 돈: {money}")
        f.close()
        time.sleep(1)
        


        



        


