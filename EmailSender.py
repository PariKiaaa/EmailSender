import smtplib

gmail_user = input('Please enter your email:\n')
gmail_password = input('Enter your password:\n')

sent_from = gmail_user
print('Enter the emails that you want to send email to them. Then, enter 0:')
to = []
while True:
	email = input()
	if email!='0':
		to.append(email)
	else:
		break

subject = input('Now, please enter the email subject:\n')
body = input('Enter the body:\n')

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
	smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	smtp_server.ehlo()
	smtp_server.login(gmail_user, gmail_password)
	smtp_server.sendmail(sent_from, to, email_text)
	smtp_server.close()
	print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong… check your google account, you should sign in to your gmail")
    print('If not solved, check this link and enable the switch:\n')
    print('https://www.google.com/settings/security/lesssecureapps')