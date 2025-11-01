import psutil
import smtplib
from email.message import EmailMessage

CPU_LIMIT = 80
MEM_LIMIT = 80

cpu = psutil.cpu_percent(4)
mem = psutil.virtual_memory().percent
print(f"cpu usage is '{cpu}'")
print(f"memory usage is '{mem}'")

if cpu > CPU_LIMIT or mem > MEM_LIMIT:

    msg = EmailMessage()
    msg["From"] = "mokchheduls46@gmail.com"
    msg["To"] = "muttakinscomputer@gmail.com"
    msg["Subject"] = "ALERT: High CPU / Memory Usage"
    msg.set_content(f"ALERT!\nCPU={cpu}%\nMEM={mem}%")

    print("Sending alert email...")
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("mokchheduls46@gmail.com", "upmd hsyo vqpj jeym")  
        server.send_message(msg)
        print("Email sent successfully!")
