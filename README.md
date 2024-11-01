# 📧 Bulk-Email-From-CSV

## 🚀 Overview

Elevate your job application process with this powerful Email Automation Project! This tool streamlines the process of sending personalized job application emails to numerous companies effortlessly, all while ensuring your data is clean and ready to go. 

## 🌟 Features

- **Data Cleansing**: Automatically cleans and validates company data, removing any invalid entries before email dispatch.
- **Personalized Email Sending**: Sends customized emails with tailored content to each recipient.
- **Attachment Support**: Seamlessly attach your resume to every email sent.
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
   To create an **App Password** with Google:
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

To initiate the email-sending process, run the `main.py` script:
```bash
python main.py
```

### 3. Generating Reports

To create a report detailing the email-sending outcomes, run the `report.py` script:
```bash
python report.py
```

## 🤝 Contributing

Contributions are welcome! If you wish to contribute to this project, please fork the repository and submit a pull request.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- A special thanks to all contributors and libraries that made this project possible.
- This project is powered by **Python** and **pandas** for seamless data handling.
