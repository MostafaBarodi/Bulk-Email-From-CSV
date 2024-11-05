# 📧 Email Automation Project

## 🚀 Overview

Elevate your job application process with this powerful Email Automation Project! This tool streamlines the process of sending personalized job application emails to numerous companies effortlessly, all while ensuring your data is clean and ready to go. 

## 🌟 Features

- **Data Cleansing**: Automatically cleans and validates company data, removing any invalid entries before email dispatch.
- **Personalized Email Sending**: Sends customized emails with tailored content to each recipient.
- **Attachment Support**: Seamlessly attaches your resume to every email sent.
- **Detailed Reporting**: Generates comprehensive reports on the success and failure of email deliveries, including reasons for any issues.

## 📁 Project Structure

```
/Email-Automation-Project
│
├── cleansing.py             # Script for cleansing and validating the CSV data
├── main.py                  # Main script for sending personalized emails
├── report.py                # Script for generating email delivery reports
├── email_body.html          # HTML file containing the email body template
├── UAE_Companies.csv        # Original CSV file with recipient information
├── UAE_Companies_Cleaned.csv # Cleaned CSV file ready for email dispatch
├── config.json              # Configuration file for email credentials
└── README.md                # Project documentation
```

## 📦 Requirements

- **Python 3.x**
- **pandas** library

## 💻 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Email-Automation-Project.git
   cd Email-Automation-Project
   ```

2. **Install required packages**:
   ```bash
   pip install pandas
   ```

3. **Configure Your Email Credentials**:  
   Set up your email details in the `config.json` file:
   ```json
   {
       "SENDER_EMAIL": "your_email@gmail.com",
       "PASSWORD": "your_app_password"
   }
   ```
   ### Generating an **App Password** with Google
   - Navigate to your [Google Account](https://myaccount.google.com/).
   - Click on **Security** from the left menu.
   - Under "Signing in to Google," select **App Passwords**. You may need to re-enter your password.
   - Choose **Select app** and pick the app you’re using.
   - Choose **Select device** and select the device you’re using.
   - Follow the instructions to generate the app password. Use this password in the `config.json` file.

## 📋 Usage

### 1. Data Cleansing

Cleanse your company data to ensure it’s ready for email dispatch using the `cleansing.py` script:
```bash
python cleansing.py
```
This script will read `UAE_Companies.csv`, eliminate rows with empty or whitespace values in the first six columns, and save the sanitized data as `UAE_Companies_Cleaned.csv`.

### 2. Sending Emails

To initiate the email sending process, run the `main.py` script:
```bash
python main.py
```

### 3. Generating Reports

To create a report detailing the email sending outcomes, run the `report.py` script:
```bash
python report.py
```

## 🔍 Hints and Tips to Avoid Being Blacklisted

Sending bulk emails can sometimes raise flags that may lead to your account being blacklisted. Here are some tips to avoid this:

1. **Limit the Number of Emails Sent per Hour**: Sending too many emails in a short period can trigger spam filters. Set a small delay between emails or limit the batch size to stay below your email provider's hourly limits.
   
2. **Use an Established Email Domain**: Email services may mark emails from new or untrusted domains as spam. If possible, use a reputable domain and avoid sending emails from free email accounts like Gmail for bulk messages.

3. **Personalize Each Email**: Use the recipient’s name, company name, and other details to make the email appear more personal. This can help avoid spam filters, as it makes your emails look less like generic bulk mail.

4. **Check Your Email Content**: Avoid spammy language (like "Free", "Guaranteed", "Click Here") in the subject or body, and ensure your HTML template is clean and well-structured.

5. **Monitor Your Sender Reputation**: Check email metrics (such as open rates and bounce rates) to ensure your account maintains a positive reputation.

### ⏰ Setting Up Delays Between Emails

If you need to add delays to prevent bulk email issues, you can use Python's `time.sleep()` function in `main.py` to introduce a pause between each email:
```python
import time
# After each email is sent
time.sleep(10)  # Delay in seconds (10 seconds here)
```

## 🤝 Contributing

Contributions are welcome! If you wish to contribute to this project, please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- A special thanks to all contributors and libraries that made this project possible.
- This project is powered by **Python** and **pandas** for seamless data handling.
