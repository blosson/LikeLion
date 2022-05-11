
# 메뉴삭제하기 / 차집합 쓰려면 둘 다 집합이어야하고 / 리스트형태로 짜장면을 감싸야함
set_lunch = set(['된장찌개','피자','제육볶음','짜장면'])
item = ['짜장면']
set_item = set(item)
set_lunch = set_lunch - set_item

print(set_lunch)


'''set_dinner = set(['1','2','3','4'])
food = '4'
set_dinner = set_dinner - set([food])
print(set_dinner)'''


