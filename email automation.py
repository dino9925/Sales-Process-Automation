import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.parse

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "luciferinreallife@gmail.com"
sender_password = "gpls ---- ---- kazu"

with open("companies.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    print("Detected CSV columns:", reader.fieldnames)


    for row in reader:
        to_email = row['Company Email']
        recipient_name = row['Name']
        recipient_company = row['Company Name']

        tracking_pixel_url = f"http://172.20.10.4:5000/track_open?email={to_email}"


        subject = f"Offering Our Services to {recipient_company}"

        encoded_email = urllib.parse.quote(to_email)
        body = f"""
        <html>
        <body>
            <p>Hi {recipient_name},</p>

            <p>I noticed your company, <strong>{recipient_company}</strong>, might benefit from our services.</p>

            <p>We specialize in helping companies like <strong>{recipient_company}</strong> streamline operations and improve efficiency. 
            Our solutions are tailored and have shown proven results across industries.</p>

            <p>If you're open to a quick conversation, I’d love to share how we can support your team’s goals.</p>

            <p>Looking forward to hearing from you!</p>

            <p>Best regards,<br>
            Dhruv Dave<br>
            luciferinreallife@gmail.com</p>
            <img src="{tracking_pixel_url}" width="1" height="1" style="display:none" />


        </body>
        </html>
        """

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            print(f"Email sent to {to_email}")
        except Exception as e:
            print(f"Error sending to {to_email}: {e}")
            break
