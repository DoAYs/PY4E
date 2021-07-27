while True :
#월급입력
    try :
        monthly_income = int(input('당신의 월급은 얼마인가요? ex)135만원은 135까지 입력해 주세요 : '))
        annual_income = int(monthly_income * 12)
        print('당신의 세전 연봉은',annual_income, '만 원입니다')
#함수 활용 : 세전/세후 연봉 계산
        def actual_income() :
            if annual_income <= 1200 :
                print('당신의 세후 연봉은', round(annual_income*(1-0.06)), '만 원입니다')
            elif annual_income <= 4600 :
                print('당신의 세후 연봉은', round(annual_income*(1-0.15)), '만 원입니다')
            elif annual_income <= 8800 :
                print('당신의 세후 연봉은', round(annual_income*(1-0.24)), '만 원입니다')
            elif annual_income <= 15000 :
                print('당신의 세후 연봉은', round(annual_income*(1-0.35)), '만 원입니다')
            elif annual_income <= 30000 :
                print('당신의 세후 연봉은', round(annual_income*(1-0.38)), '만 원입니다')
            elif annual_income <= 50000 :
                print('당신의 세후 연봉은', round(annual_income*(1-0.40)), '만 원입니다')
            else:
                print('당신의 세후 연봉은', round(annual_income*(1-0.42)), '만 원입니다')
        actual_income()
        break
    except : print('숫자로 입력해 주세요')