import json
import cv2
import time
import smtplib
from email.message import EmailMessage
import imghdr

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
count = 1

while 1:
    f = open('/Users/kartik/Desktop/website/cameraProj/data.json')
    data = json.load(f)
    f.close
    minutes = int(data['time'])
    limit = int(data['sense'])
    to = data['send']
    frames = cv2.VideoCapture('http://10.153.42.238:8081/')
    ret, frame = frames.read()

    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, limit)
    if len(faces) > 0:
        cv2.imwrite(f"frame{count}.jpg", frame)

        Sender_Email = "verficationemailbluecoder@gmail.com"
        Password = "jgpzwoarxcgqcrgs"

        newMessage = EmailMessage()    #creating an object of EmailMessage class
        newMessage['Subject'] = "Camera Alert" #Defining email subject
        newMessage['From'] = Sender_Email  #Defining sender email
        newMessage['To'] = to  #Defining reciever email
        newMessage.set_content('There was a person detected at your camera. Please be careful.') #Defining email body
        with open(f'frame{count}.jpg', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name

        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password) #Login to SMTP server
            smtp.send_message(newMessage)      #Sending email using send_message method by passing EmailMessage object
        count += 1
        time.sleep(60*minutes)

frames.release()
cv2.destroyAllWindows()