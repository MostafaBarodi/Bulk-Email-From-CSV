def generate_report(success_count, failure_count, failure_reasons):
    with open("email_sending_report.txt", "w") as report_file:
        report_file.write("Email Sending Report\n")
        report_file.write("=====================\n")
        report_file.write(f"Total Emails Sent Successfully: {success_count}\n")
        report_file.write(f"Total Emails Failed to Send: {failure_count}\n\n")

        if failure_count > 0:
            report_file.write("Failure Reasons:\n")
            for email, company, reason in failure_reasons:
                report_file.write(f" - Failed to send to {email} (Company: {company}): {reason}\n")

    print("Report generated: email_sending_report.txt")
