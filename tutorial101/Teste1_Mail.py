import smtplib
from arquivo import user, passw

HOST = "smtp.ufsc.br" #Servidor da UFSC
SUBJECT = "Test email from Python"
TO = "nicolas.grad.ufsc@gmail.com"
FROM = "nicolas.santos1707@gmail.com"
text = "Python 3.4 rules them all!"

BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT ,
    "",
    text
    ))

server = smtplib.SMTP(HOST)
server.login(user, passw)
server.sendmail(FROM, [TO], BODY)
server.quit()
