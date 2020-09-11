print('''
                       ___                   _ _           
                      / _ \      /\/\   __ _(_) | ___ _ __ 
                     / /_\/____ /    \ / _` | | |/ _ \ '__|
                    / /_\\_____/ /\/\ \ (_| | | |  __/ |   
                    \____/     \/    \/\__,_|_|_|\___|_|   
''')

# IMPORTS
import smtplib
from email.message import EmailMessage
from time import sleep
import os
import json
import time

# CONFIG
try:
   file_settings = input('Use settings? Yes = [1] | No = [2] | Create \ Edit settings = [3] | Exit = [4]: ')
   file_settings = int(file_settings)

   if file_settings == 1:
         file_settings = True
   elif file_settings == 2:
         file_settings = False
   elif file_settings == 3:
         # Create settings
         mailc = input("What mail do you want to save? ")
         passc = input("What password do you want to save? ")

         settings = {
         "email": mailc,
         "password": passc,
         }
         with open('settings.json', 'w') as f:
            json.dump(settings, f, sort_keys=True, indent=4)
         print('Restarting program!')
         sleep(1)
         os.system('python main.py')
   elif file_settings == 4:
          print('Existing.')
          print('Just a sec clearing console')
          sleep(3)
          os.system('cls')
          exit()
   else:
         print('Not an option!')
         exit()
except ValueError:
   print('Please type a number!')
   exit()


# CONNECTING TO GMAIL SERVERS
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

# LOGGING IN
if not file_settings:
   sender_email = input(str("Please enter your email: "))
   password = input(str("Please enter your password: "))
else:
   try:
      with open('settings.json') as f:
         print('Trying to log in using the settings...')
         data = json.load(f)
         sender_email = data['email']
         password = data['password']
   except FileNotFoundError:
      print("Settings do not exist! please restart and press 3!")
      exit()
try:
   s.login(sender_email, password)
   print(f"Login success")
except:
   print(f'Can not log in! Please turn on this setting https://myaccount.google.com/lesssecureapps or check your password')
   exit()


# E-MAIL INPUTS
rec_email = input(str("Please enter the target email: "))
message = input(str("Please enter the message content you want to submit: "))
subject = input(str("Please enter the subject of the mail you want to submit: "))
times = input("Please enter the amount of times you want to submit the message: ")


# MESSAGE
msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = rec_email
msg.set_content(message)


# SENDING THE MAIL MESSAGE
try:
   begin = time.time()
   print('**********************************************')
   for i in range(int(times)):
      s.send_message(msg)
      print(f"{i + 1}) Email has been sent to {rec_email}, Message: {message}")

   stop = time.time()
   # LAST ACTIONS
   sleep(2)
   print('**********************************************')
   print('Deleting console...')
   sleep(3)
   os.system('cls')
   print(f"{times} Emails were sent succesfully in {stop - begin} seconds!")
except:
   print(f"Can not submit mail to {rec_email}")
   print('Please try again!')
   os.system('python main.py')