import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.daum.net/"
response = requests.get(url)
# print(requests.get(url)) # 200이라는 숫자는 보통 프로그래밍에서 '성공'을 의미함

# print(response.text) # 해당 사이트 html 코드 확인하는법

# print(type(BeautifulSoup(response.text, 'html.parser'))) # type() 어떤 타입인지 알려주는 함수(str, int 등)
# BeautifulSoup -> 통에 담아주는 역할 BeautifulSoup(데이터, 파싱방법) 파싱: 데이터를 의미있게 변경하는 과정

soup = BeautifulSoup(response.text, 'html.parser')

'''file = open("daum.html","w",encoding='UTF-8')  # r=읽기전용,w=쓰기모드,a=기존파일에 새로운 내용 덧붙이기
file.write(response.text)
file.close()'''

#print(soup.title)
#print(soup.title.string)
#print(soup.span)
#print(soup.findAll('span'))


#print(response.url)
#print(response.content)
#print(response.encoding)
#print(response.headers)
#print(response.json)
#print(response.links)
#print(response.ok)
#print(response.status_code)

# html 문서에서 모든 a태그를 가져오는 코드

results = soup.findAll('a','Link_favorsch') # a태그와 link_favsch 클래스만 출력되게 함

'''for result in results:
    print(result.get_text(),'\n')
    rank += 1

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

search_rank_file = open("rankresult.txt",'w')'''


for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1