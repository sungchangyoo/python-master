# 교재 557 페이지 예지
y = [10,20,30] # 리스트 생성

try:
    index,x = map(int, input("인덱스와 나눌 숫자를 입력하세요.").split())

except ZeroDivisionError as e : #현존하는 ERROR CODE
    print("숫자를 0으로 나눌수 없습니다.", e)
except IndexError as e: #현존하는 ERROR CODE
    print("잘못된 인덱스입니다.", e)
except ValueError as e: #현존하는 ERROR CODE
    print("값을 다시 입력하세요", e)

else:
    print(3)

finally