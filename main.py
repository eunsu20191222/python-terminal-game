from time import sleep
from functions start as game
import os
def clear():
    return os.system("clear")
#기본
print("게임을 시작합니다")
user = input("USER네임을 입력하세요: ")

sleep(1)

ask_for_i = input("게임을 플레이 하는 법을 보려면 i 를 클릭해 주세요, 바로 시작할려면 s 를 눌러주세요 경고: i 와 s 만 입력하시오: ")


if ask_for_i == "i":
    sleep(1)
    print("\nthis is instrodu ction")
    sleep(0.5)
    f = open('instroduction.txt', 'r')
    introduction = f.read()
    f.close()
    print(introduction)
    sleep(3)
    clear()
    game(user)
    sleep(4)

elif ask_for_i == "s":
    sleep(1)
    print("start game")
    sleep(2)
    clear()
    game(user)
