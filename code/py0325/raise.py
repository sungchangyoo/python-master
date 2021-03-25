try :
    x = int(input("숫자를 입력하시오. "))

    if x % 3 != 0 :
        raise Exception("3의 배수가 아닙니다.")
    print(x)

except Exception as e :
    print("예외가 발생했습니다.", e)