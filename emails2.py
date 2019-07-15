from smtplib import SMTP, SMTPAuthenticationError, SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




host = "smtp.office365.com"
port = 587
username = "test@sipoli.onmicrosoft.com"
password = "M1cr0s0ft"
from_email = username






msg = MIMEMultipart("alternative")
msg["Subject"] = "test Subject!"
msg["From"] = from_email





plain_txt = "testing plain text part in the message"
html_txt = """\
<html>
  <head></head>
  <body>
    <p>hey!<br>
      Testing this email <b>message</b> Made by <b style='color:Tomato'>Vinicius</b> with Python !
    </p>
  </body>
</html>
"""

 




part_1 = MIMEText(plain_txt,"plain")
part_2 = MIMEText(html_txt,"html")






msg.attach(part_1)
msg.attach(part_2)






email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
try:
    email_conn.login(username,password)
    email_conn.sendmail(from_email, "vinicius@sipoli.onmicrosoft.com", msg.as_string())
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("An error occurred")






email_conn.quit()