
import smtplib
from email.message import EmailMessage
import imghdr

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("코드라이언 수업중입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "###@gmail.com"
message["To"] = "###@gmail.com"

def senEmail(Addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,"blosson.mh@gmail.com"))
     smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")    
    else:
        print("유효한 이메일 주소가 아닙니다.")

# image = open("hello.png","rb") # 바이너리 파일
with open('hello.png','rb') as image: # 안전하게 이미지 파일 열고 닫는 방법
    image_file = image.read()
# print(image.read())

image_type = imghdr.what('hello.png',image_file)
print(image_type)
# message.add_attachment((image_file,maintype='image',subtype='png'))



# open() - codelion.png / rb
#image = open("codelion.png","rb")
# 파일을 읽어서 출력해보세요. read()
#print(image.read())

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("###@gmail.com","######")
smtp.send_message(message)
sendEmail("blosson.mh@gamil.com","dfadsfasefasf")
smtp.quit()

