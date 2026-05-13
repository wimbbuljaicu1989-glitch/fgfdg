import smtplib
import os

email_user = os.environ.get("EMAIL_USER")F
email_pass = os.environ.get("EMAIL_PASS")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()ds
server.login(email_user, email_pass)
x
subject = "GitHub Action Email"W
body = "This email was sent automatically from GitHub Actions."
s
message = f"Subject: {subject}\n\n{body}"
D
server.sendmail(email_user, "speednet.Scok@gmail.com", message)
server.quit()

print("Email sent successfully")S
sSD
