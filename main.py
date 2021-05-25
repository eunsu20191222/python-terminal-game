from time import sleep
from functions import main_game as game

#기본
print("게임을 시작합니다")
user = input("USER네임을 입력하세요: ")

sleep(1)

ask_for_i = input("게임을 플레이 하는 법을 보려면 i 를 클릭해 주세요, 바로 시작할려면 s 를 눌러주세요: ")

if ask_for_i == "i":
    sleep(1)
    print("\nthis is instroduction")
    sleep(3)
    game(user)

elif ask_for_i == "s":
    sleep(1)
    print("start game")
    sleep(2)
    game(user)