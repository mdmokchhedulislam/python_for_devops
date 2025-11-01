import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time


sender_email = "mokchheduls46@gmail.com"
password = "upmd hsyo vqpj jeym"  
receivers = ["mokchheduls46@gmail.com", "mokchheduls467@gmail.com"]  

subject = "Daily Report"
body = "Hello,\n\nThis is your daily automated report from Python.\n\nRegards,\nAutomation System"

# Optional attachment
attachment_path = "report.pdf"  # file must exist in same folder

# ---------------------------
# Email sending function
# ---------------------------
def send_email():
    try:
        # Create message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ", ".join(receivers)
        message['Subject'] = subject

        # Attach body
        message.attach(MIMEText(body, 'plain'))

        # Attach file (optional)
        if attachment_path:
            try:
                with open(attachment_path, "rb") as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
                    message.attach(part)
            except FileNotFoundError:
                print(f"Attachment '{attachment_path}' not found, sending without it.")

        # Connect to SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Send email
        server.sendmail(sender_email, receivers, message.as_string())
        print("Email sent successfully to:", receivers)

    except Exception as e:
        print("Error:", e)
    finally:
        server.quit()

# ---------------------------
# Schedule daily email
# ---------------------------
# Example: send email every day at 08:00 AM
# schedule.every().day.at("08:00").do(send_email)
send_email();
print("email send successfully")
# print("Email automation system started. Waiting for scheduled time...")

# while True:
#     schedule.run_pending()
#     time.sleep(60)  # check every minute
