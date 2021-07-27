# 요금
card = (0, 450, 720, 1200, 0)
cash = (0, 450, 1000, 1300, 0)

# 함수
# 카드 요금
def method_card(age):
    if age < 8:
        return card[0]
    elif 8 <= age <14:
        return card[1]
    elif 14 <= age < 20:
        return card[2]
    elif 20 <= age <75:
        return card[3]
    else:
        return card[4]
# 현금 요금
def method_cash(age):
    if age < 8:
        return cash[0]
    elif 8 <= age <14:
        return cash[1]
    elif 14 <= age < 20:
        return cash[2]
    elif 20 <= age <75:
        return cash[3]
    else:
        return cash[4]
# 카드 현금 분류
def Age_calculation(age, method):
    if method == "카드":
        return method_card(age)
    elif method == "현금":
        return method_cash(age)
    else:
        raise Exception

# 메인
while True:
    try:
        print("나이를 입력해주세요.")
        age = int(input())
        print("카드인가요 현금인가요?")
        method = str(input())
        fare = Age_calculation(age, method)
        print("나이:"+str(age)+"세")
        print("수단:"+method)
        print("요금:"+str(fare)+"원")
        break
    except ValueError:
        print("잘못된 입력입니다")
        continue
    except:
        print("잘못된 입력입니다 \"현금\" 또는 \"카드를\"입력해주세요 ")
