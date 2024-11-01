import smtplib
import pandas as pd
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import re
from report import generate_report  # Import the reporting function

# Load your CSV file
data = pd.read_csv("UAE_Companies_Cleaned.csv")  # Update with your actual CSV file path

# Load credentials from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

SENDER_EMAIL = config["SENDER_EMAIL"]
PASSWORD = config["PASSWORD"]

# Function to validate email addresses
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Function to read the HTML body from a file
def read_email_body(company_name):
    with open("email_body.html", "r") as html_file:
        body = html_file.read()
    return body.replace("{company_name}", company_name)

# Function to send an email
def send_email(to_address, company_name):
    sector = "Telecoms and IT"
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_address
    msg['Subject'] = f"Job Application for {company_name}"

    body = read_email_body(company_name)  # Read the HTML body
    msg.attach(MIMEText(body, 'html'))

    resume_path = "resume.pdf"  # Replace with the actual path to your resume
    with open(resume_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(resume_path)}')
        msg.attach(part)

    # Try sending the email and catch any exceptions
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, PASSWORD)
            server.sendmail(SENDER_EMAIL, to_address, msg.as_string())
        return True, None  # Successful send
    except Exception as e:
        return False, str(e)  # Failed send with error message

# Send emails to each HR contact
success_count = 0
failure_count = 0
failure_reasons = []

for index, row in data.iterrows():
    email = row['Email']
    company_name = row['Company Name']

    if pd.notna(email) and pd.notna(company_name):
        if is_valid_email(email):
            success, reason = send_email(email, company_name)
            if success:
                success_count += 1
                print(f"Email sent to {email} for {company_name} in Telecoms and IT sector")
            else:
                failure_count += 1
                failure_reasons.append((email, company_name, reason))
                print(f"Failed to send email to {email} for {company_name}: {reason}")
        else:
            failure_count += 1
            failure_reasons.append((email, company_name, "Invalid email format"))
            print(f"Skipping invalid email: {email} for {company_name}")
    else:
        print(f"Skipping row {index} due to missing data")

# Generate the final report
generate_report(success_count, failure_count, failure_reasons)
