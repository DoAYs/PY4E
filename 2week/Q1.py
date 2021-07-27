
# 2주차 과제 01_컴퓨터랑 가위바위보(랜덤)
import random

rps = ['가위', '바위', '보']
result = {0: '사용자 승리! Congraturation!!!!!!', 1: '당신은 컴퓨터한테 졌어요.', 2: '무승부 입니다.'}
def checkWin(user, com): # 사용자 vs 컴퓨터 겨루기
    try:
        if not user in rps: # 가위, 바위, 보 말고 다른 것을 쓴 경우 다시 입력
           raise ValueError("가위, 바위, 보중 하나의 값이여야 합니다.")
    except ValueError:
       print('잘못입력하셨습니다. 다시 입력하세요')
       return False

    print(f'User ( {user} vs {com} ) Computer')
    if user == com: # 사용자와 컴퓨터가 같은 것을 낼때
        state = 2
    elif user == '가위' and com == '바위': # 사용자와 컴퓨터가 긱긱 가위와  를 낼때, 사용자
        state = 1
    elif user == '바위' and com == '보': # 사용자와 컴퓨터가 긱긱 바위와 보를 낼때, 사용자 패배
        state = 1
    elif user == '보' and com == '가위': # 사용자와 컴퓨터가 긱긱 보와  를 낼때, 사용자 패배
        state = 1
    else: # 그밖의 경우는 사용자
        state = 0
    print(result[state])
    return True

print('\n▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧')
while True:
    user = input("자 이제부터 가위바위보 게임을 시작합니다. 가위, 바위, 보 중 하나를 입력하세요. : ") # 사용자 입력 (가위,바위,보)
    com = rps[random.randint(0, 2)]
    if checkWin(user, com):
        break
print('▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧\n')