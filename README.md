# Bulk-Email-From-CSV

## Overview

This project automates the process of sending job application emails to multiple companies using information from a CSV file. It includes a data cleansing script to prepare the recipient data and generates reports on the email sending status, detailing success and failure reasons.

## Features

- Cleanses company data to ensure all entries are valid before sending emails.
- Sends personalized emails to multiple recipients.
- Attaches a resume to each email.
- Generates a report detailing the success and failure of email deliveries.

## Project Structure

```
/Email-Automation-Project
│
├── cleansing.py             # Script for cleansing the CSV data
├── main.py                  # Main script for sending emails
├── report.py                # Script for generating email sending reports
├── email_body.html          # HTML file containing the body of the email
├── UAE_Companies.csv        # Original CSV file with recipient information
├── UAE_Companies_Cleaned.csv # Cleaned CSV file ready for email sending
├── config.json              # Configuration file for email credentials
└── README.md                # Project documentation
```

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Email-Automation-Project.git
   cd Email-Automation-Project
   ```

2. Install required packages:
   ```bash
   pip install pandas
   ```

3. Set up your email credentials in the `config.json` file:
   ```json
   {
       "SENDER_EMAIL": "your_email@gmail.com",
       "PASSWORD": "your_email_password"
   }
   ```

## Usage

### Data Cleansing

Before sending emails, you can cleanse the company data using the `cleansing.py` script:
```bash
python cleansing.py
```
This will read the `UAE_Companies.csv`, remove rows with empty or whitespace values in the first six columns, and save the cleaned data to `UAE_Companies_Cleaned.csv`.

### Sending Emails

To send emails, run the `main.py` script:
```bash
python main.py
```

### Generating Reports

To generate a report of the email sending status, run the `report.py` script:
```bash
python report.py
```

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.

