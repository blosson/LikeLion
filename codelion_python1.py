import random
import time

# for i in range(30): --->  반복문 
# while True: -> 무한루프(T는 대문자) / 1초마다 쉬는 코드 : Time.sleep(원하는초)
# for i in range(30):
while True:
    print(random.choice(["피자", "햄버거", "치킨", "된장찌개", "떡볶이", "감자튀김"]))
    #time.sleep(1)
    break
# 무한반복이 멈추지 않을 경우엔 break를 넣어주면 됨

print("이 문장도 반복되나?") 

lunch = random.choice(['된장찌개', '피자', '제육볶음'])
#lunch = '냉장고'
dinner = random.choice(['김밥', '쫄면', '돈까스'])
print(lunch)

info = {'고향':'광주', '취미':'음악감상', '좋아하는 음식':'천하일면'}
print(info)
print(info.get('취미'))  # 함수.get 기억하기!
info2 = {'고향':'서울', '특기':'피아노'}
print(info2.get('고향'))
print(info2.get('특기'))

information = {'고향':'수원', '취미':'영화감상', '좋아하는 음식':'국수'}
foods = ['된장찌개', '피자', '제육볶음']
print(information.get('취미'))
information['특기'] = '피아노' # 이렇게 하면 딕셔너리에 새로운 값들을 추가할 수 있음. 
information['사는곳'] = '서울'
print(information)
# del information['좋아하는 음식']  ---> 해당 값 삭제
# print(len(information)) # 해당 딕셔너리에 정보 묶음이 몇개 있는지

information.clear()  # 딕셔너리 안 전체 비우기
print(information)

print(foods[0])
print(foods[1])
print(foods[2])
foods.append('김밥') # 리스트에 항목 추가
print(foods)
foods.remove('피자') # del foods[0] 이렇게도 가능
print(foods)

for x in range(10):
    print(x)

foods2 = ['된장찌개', '피자', '제육볶음']

for i in range(3):
    print(foods2[i])

for i in foods2: # foods 리스트에 있는 모든 요소를 다 출력하는 방법
    print(i)

information1 = {'고향':'수원', '취미':'영화관람', '좋아하는 음식':'음식'} 
for x, y in information1.items(): # 딕셔너리 출력하는 방법
    print(x)
    print(y)


# 집합 : 리스트와는 달리 순서가 없음. 

foods3 = ['1', '2', '3','1']
foods_set = set(foods3)
#foods_set2 = set(['1', '2', '3'])
print(foods3)
print(foods_set)

menu1 = set(['된장찌개','피자','제육볶음'])
menu2 = set(['된장찌개','떡국','피자'])
menu3 = menu1 | menu2 # | 합집합 / & 교집합 / - 차집합
print(menu3)

# 만약에

food = random.choice(['된장찌개','피자','제육볶음'])

if food == '제육볶음':
    print('곱빼기 주세요')
else:
    print('그냥 주세요')
print('종료')