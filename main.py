### MADE BY BARZUKA ###
# Config
file_settings = False

# The email module
import smtplib
import os
from email.message import EmailMessage
from time import sleep

# Connecting to gmail servers
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

# Logging in
if not file_settings:
   sender_email = input(str("Please enter your email: "))
   password = input(str("Please enter your password: "))
else:
   print('Trying to log in using the file settings...')
   sender_email = 'mail@here'
   password = 'password'
try:
   server.login(sender_email, password)
   print(f"Login success")
except:
   print(f'Can not log in! Please turn on this setting https://myaccount.google.com/lesssecureapps or check your password')
   exit()
# Email info
rec_email = input(str("Please enter the target email: "))
message = input(str("Please enter the message content you want to submit: "))
subject = input(str("Please enter the subject of the mail you want to submit: "))
times = input("Please enter the amount of times you want to submit the message: ")


##Message
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = rec_email
msg.set_content(message)

# Sending the Email
try:
   for i in range(int(times)):
      server.send_message(msg)
      print(f"{i + 1}) Email has been sent to {rec_email}, Message: {message}")
      # server.sendmail(sender_email, rec_email, msg)
except:
   print(f"Can not submit mail to {rec_email}")

sleep(3)
print('Deleting console...')
sleep(4)
os.system('cls')

### MADE BY BARZUKA ###