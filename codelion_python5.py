total_list = [] # 아무 내용도 없는 빈 리스트가 만들어짐

while True:
    question = input('질문을 입력해주세요 : ')
    if question == 'q':
        break
    else:
        total_list.append({'질문': question, '답변':''}) # list에 해당 딕셔너리를 넣어주는 작업

for i in total_list: # 하나씩 꺼내주는 역할
    print(i['질문'])
    answer = input("답변을 입력해주세요 : ")
    i['답변'] = answer
print(total_list)