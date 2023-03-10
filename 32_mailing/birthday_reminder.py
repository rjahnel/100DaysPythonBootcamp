import random
import datetime as dt
import smtplib
import pandas


def Send_Mail(to, subject, msg):
    my_email = input("Email-Address:")
    my_password = input("Password")
    to_adress =  to
    connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    header = 'To:' + to_adress + '\n' + 'From: ' + my_email + '\n' + 'Subject: ' + subject +  '\n'
    message = header + '\n' + msg
    connection.sendmail(my_email, to_adress, message)
    connection.close()

# get day an month
today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]

    # choose textfile
    letter = f"letter_{random.randint(1, 3)}.txt"
    with open(letter) as file:
        content = file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    
    Send_Mail("rjahnel@googlemail.com", "Happy birthday", content)
    