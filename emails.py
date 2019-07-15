from smtplib import SMTP, SMTPAuthenticationError, SMTPException

host = "smtp.office365.com"
port = 587
username = "test2@sipoli.onmicrosoft.com"
password = "password"
from_email = username

email_conn = SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
try:
    email_conn.login(username,password)
    email_conn.sendmail(from_email, "vinicius@sipoli.onmicrosoft.com", "test message body")
except SMTPAuthenticationError:
    print("Could not login")
except:
    print("An error occurred")

email_conn.quit()
