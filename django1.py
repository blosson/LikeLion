# try, except, finally 파이썬 멈춤없이 실행시킬 수 있는 방법! 중요
# 상태와 동작을 한 번에 여러 개 정의할 수 있는 방법 == 객체지향프로그래밍 like 달고나 찍어내기
# pip freeze == 현재 설치된 패키지 목록 보기
# python -m venv myvenv== 가상환경 만들기 / 실행하기 source myvenv/Scripts/activate / 가상환경 끄기 == deactivate.
# django-admin startproject myproject(파일이름) == 프로젝트 시작하는 명령어

# __init__.py == 해당 폴더가 패키지라는 걸 알려주기 위한 파일 (일종의 약속)
# urls.py == url들을 관리하는 파일

# cd 사용법 숙지하기 / ls = 현재폴더

''' manage.py 기능 4가지
1. python manage.py runserver == 서버를 키는 기능 / ctrl + c == 서버를 끄는 기능
2. python manage.py startapp 파일이름(dashboard, payment 등) == application 만들기  
어플리케이션을 만들었으면 basicsetting의 installed app 리스트 안에 추가시켜주어야 함!! - 중요
3. python manage.py migrate == DB 초기화 및 변경사항 반영
4. python manage.py createsuperuser == 관리자 계정 만들기
'''