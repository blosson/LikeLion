import requests
import json

city = "gwangju"
apikey = "e7b749fffe7cef4808eb50d5e7b034f0"
lang = "kr"
units = "metric" # 화시를 섭씨로 바꾸는 것
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}" #파이썬 f스트링 사용 / 문자열 안에 변수를 넣고 싶다면 꼭 중괄호를 사용해야함

result = requests.get(api)
#print(result.text)
#print(type(result.text))

data = json.loads(result.text) # json을 활용하여 딕셔너리 형태로 바꾸는 과정
#print(type(data))

print(data["name"],"의 날씨입니다.")
print("날씨는", data["weather"][0]["description"],"입니다.")
print("현재 온도는", data["main"]["temp"],"입니다.")
print("하지만 체감 온도는", data["main"]["feels_like"],"입니다.")
print("최저 기온은",data["main"]["temp_min"],"입니다.")
print("최고 기온은",data["main"]["temp_max"],"입니다.")
print("습도는",data["main"]["humidity"],"입니다.")
print("기압은",data["main"]["pressure"],"입니다.")
print("풍향은",data["wind"]["deg"],"입니다.")
print("풍속은",data["wind"]["speed"],"입니다.")
