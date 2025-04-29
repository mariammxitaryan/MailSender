import smtplib
import os
import getpass
from email.mime.text import MIMEText

# ---------------------------------------------------------------------------- #
#    `get_credentials()`: Securely retrieves the sender's email and password.  #
# ---------------------------------------------------------------------------- #
def get_credentials():
    sender_email = input("Enter your email address: ")
    password = getpass.getpass("Enter your email password (input hidden): ")
    return sender_email, password

# ---------------------------------------------------------------------------------- #
#    `compose_message()`: Creates the email message with sender, recipient, subject, #
#                      and body.                                                     #
# ---------------------------------------------------------------------------------- #
def compose_message(sender, recipient, subject, body):
    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    return msg

# ------------------------------------------------------------------------------------ #
#   `send_email()`: Establishes a secure connection to the SMTP server, logs in, and   #
#                   sends the provided email message.                                  #
# ------------------------------------------------------------------------------------ #
def send_email(sender, password, recipient, msg):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        return True, "Email sent successfully!"
    except smtplib.SMTPException as e:
        return False, f"Failed to send email: {e}"

# ---------------------------------------------------------------------------- #
#  `main()`: Orchestrates the email sending process by getting user input,     #
#               composing the message, and sending it.                         #
# ---------------------------------------------------------------------------- #
def main():
    print("=== Simple Email Sender ===")
    sender, password = get_credentials()
    recipient = input("Enter the recipient's email address: ")
    subject = input("Enter the subject of the email: ")
    print("Enter your message. Predd Enter twice to finish:")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    body = "\n".join(lines)

    msg = compose_message(sender, recipient, subject, body)
    success, feedback = send_email(sender, password, recipient, msg)
    print(feedback)

if __name__ == "__main__":
    main()