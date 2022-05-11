import random
import time

lunch = ['된장찌개','피자','제육볶음','짜장면']
#lunch.append('돈까스')
while True:
    print(lunch)
    item = input('음식을 추가해주세요 : ') # ctrl+c를 누르면 터미널에서 나가짐
    if(item == 'q'): # q를 누르면 무한루프가 중지되게 하는 if문
        break
    else:
        lunch.append(item)

#print(lunch)

set_lunch  = set(lunch) # lunch라는 변수가 집합 형태로 저장됨
while True:
    print(set_lunch)
    item = input('음식을 삭제해주세요 : ')
    if(item == 'q'):
        break
    else:
        set_lunch = set_lunch - set([item])

print(set_lunch, '중에서 선택합니다.')
print("5")
time.sleep(1) # xx초 쉬는 함수
print("4")
time.sleep(1) 
print("3")
time.sleep(1) 
print("2")
time.sleep(1) 
print("1")
time.sleep(1)

print(random.choice(list(set_lunch))) # 랜덤으로 선택해주는 함수


  