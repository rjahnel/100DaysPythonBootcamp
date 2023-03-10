import smtplib

my_email = input("Email-Account to send")
my_password = input("input your password for your email.account:")
to_adress = input("Send to Email")

connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
connection.starttls()
connection.login(user=my_email, password=my_password)

header = 'To:' + to_adress + '\n' + 'From: ' + my_email + '\n' + 'Subject: This is an test-mail' + '\n'
message = header + '\n Message in testmail.\n\nGreetings from Rolf.'
connection.sendmail(my_email, to_adress, message)
connection.close()
