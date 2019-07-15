import smtplib

host = "smtp.office365.com"
port = 587
username = "test@sipoli.onmicrosoft.com"
password = "M1cr0s0ft"
from_email = username
to_list = ["vinicius@sipoli.onmicrosoft.com"]


email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello this is a test message")
email_conn.quit()

from smtplib import SMTP
email_conn2 = SMTP(host, post)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, "Hello this is a test message")
email_conn.quit()

