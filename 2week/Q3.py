
# 2주차 과제 03_학점계산기
print("▧안녕하세요 학점 계산기 입니다.▧")

#학점계산 함수
def grade(score): # 학점 계산
    if score > 100 or score < 0:
        print("올바른 정보가 아닙니다, 다시 입력해주세요.")
    elif score >=95:
        grade= "A+"
        print("훌륭합니다 수고하셨습니다.")
    elif score >=90:
        grade= "A"
        print("훌륭합니다 수고하셨습니다.")
    elif score >=85:
        grade= "B+"
        print("수고하셨습니다.")
    elif score >=80:
        grade= "B"
        print("수고하셨습니다.")
    elif score >=75:
        grade= "C+"
        print("학업에 열중하시길 바랍니다.")
    elif score >=70:
        grade= "C"
        print("학업에 열중하시길 바랍니다.")
    elif score >=65:
        grade= "D+"
        print("학업에 열중하시길 바랍니다.")
    elif score >=60:
        grade= "D"
        print("학업에 열중하시길 바랍니다.")
    else:
        grade= "F"
        print("학업에 열중하시길 바랍니다.")
    return grade

#예외처리 (잘못입력된경우, 다시입력하시오.)
while True:
    try:
        name = input("이름을 입력하시오: ")
        classnum = int(input("학번을 입력하시오: "))
        subject_name = input("과목명을 입력하시오: ")
        semester = int(input("몇 학기 입니까?: "))
        score = int(input("점수를 입력하세요: "))
        break

    except ValueError:
        print('잘못 입력하셨습니다. 알맞게 다시 입력하세요!')

# 최종 출력
print('\n▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧')
print("학생 이름:", name)
print("학번: ", classnum)
print("과목명: ", subject_name)
print("학기: ", semester)
print("점수: ", score)
print("당신의 학점은:",grade(score))
print('▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧\n')