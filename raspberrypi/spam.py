import smtplib
smtpUser = 'nikitush10@gmail.com'
smtpPass = 'Jonathan10'

toAdd = 'nikitush10@gmail.com'
fromAdd = smtpUser

subject = 'Python Test'
header = 'To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject
body = 'From within a Python script'

print (header + '\n' + body)

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit