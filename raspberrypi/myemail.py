import smtplib

smtpUser = 'nikitush10@gmail.com'
smtpPass = 'Jonathan10?'

toAdd = 'jonathan.sherbakov@gmail.com'
fromAdd = smtpUser

subject = '?!'
header = 'to ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subjects: ' + subject
body = 'YOU EAT ALL MY BEANS'

print (header + '\n' + body)

s = smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, header + '\n\n' + body)

s.quit