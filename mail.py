import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 # gmail SMTP 사용하려면 SERVER와 PORT를 이렇게 설정해주어야함

message = EmailMessage() #메시지 통 만들기
message.set_content("코드라이언 수업중입니다.") #본문 만들기

message["subject"] = "이것은 제목입니다."
message["From"] = "###@gmail.com" # 보내는 이메일 (내 이메일)
message['to'] = "#####@gmail.com" # 받는 이메일

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT) # 보안문제 때문에 반드시 뒤에 _SSL를 붙여주어야함
smtp.login("blosson.mh@gmail.com","a123456789")

smtp.send_message()
smtp.quit()

