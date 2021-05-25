from time import sleep

#기본
print("게임을 시작합니다")

sleep(1)

ask_for_i = input("게임을 플레이 하는 법을 보려면 i 를 클릭해 주세요, 바로 시작할려면 s 를 눌러주세요: ")

if ask_for_i == "i":
    print("this is instroduction")
elif ask_for_i == "s":
    print("start game")
