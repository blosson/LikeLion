'''def make_dolchelatte():
    print('1. 얼음을 넣는다.')
    print('2. 연유를 30ml 넣는다.')
    print('3. 찬 우유를 넣는다.')
    print('4. 에스프레소샷을 넣는다.')

def make_blueberry_smoothie():
    print('1. 블루베리 20g을 넣는다.')
    print('2. 연유를 30ml 넣는다.')
    print('3. 얼음을 넣는다.')
    print('4. 믹서기에 간다.')

def make_simple_latte():
    print('1. 커피를 넣는다.')
    print('2. 우유를 넣는다.')
    print('3. 신나게 섞는다.')

make_simple_latte()
make_blueberry_smoothie()
make_dolchelatte()
make_dolchelatte()'''

total_dictionary = {}

while True:
    question = input('질문을 입력해주세요 : ')
    if question == 'q':
        break
    else:
        total_dictionary[question] = "" # 딕셔너리에 입력값을 넣어주는 것

for i in total_dictionary: # 하나씩 꺼내주는 역할
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer # 이게 어떻게 value 값으로 들어가게 되는거지..?
print(total_dictionary)
        
    