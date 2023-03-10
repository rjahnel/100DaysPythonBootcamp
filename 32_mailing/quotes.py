import random
import datetime as dt
import smtplib

weekdays = ["Monday", "Thuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
quotes = []

my_email = input("Email-Account to send")
my_password = input("input your password for your email.account:")
to_adress = input("Send to Email")
connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
connection.starttls()
connection.login(user=my_email, password=my_password)


with open('quotes.txt') as f:
    quotes = f.read().splitlines()
    
now = dt.datetime.now()
wd = now.weekday()
randquote = random.choice(quotes)
#print(f"Quote for {weekdays[wd]}:\n{quotes[randquote]}")

header = 'To:' + to_adress + '\n' + 'From: ' + my_email + '\n' + 'Subject: Quote for ' + weekdays[wd] + '\n'
message = header + '\n ' + quotes[randquote]
connection.sendmail(my_email, to_adress, message)
connection.close()

