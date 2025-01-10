import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from frac_prop import settings


def send_email(subject, body, to_email):
    # SMTP server configuration
    smtp_server = settings.SMTP_SERVER
    smtp_port = settings.SMTP_PORT
    username = settings.SMTP_USERNAME
    password = settings.SMTP_PASSWORD

    # Construct the email
    msg = MIMEMultipart()
    msg["From"] = username
    msg["To"] = to_email
    msg["Subject"] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, "html"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Use TLS for security
        server.login(username, password)  # Login to your email account
        server.send_message(msg)  # Send the email
        server.quit()  # Disconnect from the server
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
