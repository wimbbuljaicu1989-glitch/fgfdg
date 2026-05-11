import smtplib
import os

email_user = os.environ.get("EMAIL_USER")F
email_pass = os.environ.get("EMAIL_PASS")

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()ds
server.login(email_user, email_pass)

subject = "GitHub Action Email"W
body = "This email was sent automatically from GitHub Actions."

message = f"Subject: {subject}\n\n{body}"

server.sendmail(email_user, "speednet.cok@gmail.com", message)
server.quit()

print("Email sent successfully")
