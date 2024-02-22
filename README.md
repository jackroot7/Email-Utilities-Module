# Email Utilities Module

A Python utility for sending emails with HTML content and attachments, utilizing SMTP protocol, Jinja2 templating, and environment variables for configuration.

## Features

- Send HTML emails with dynamic data using Jinja2 templates.
- Attach files to emails.
- Use environment variables for secure configuration.
- Support for CC recipients.

## Requirements

- Python 3.x
- smtplib
- email
- Jinja2
- python-dotenv

## Setup

1. **Install Dependencies**

   Use pip to install the required Python packages.


2. **Environment Variables**

Create a `.env` file in the root directory of your project and define the following variables:

`EMAIL_HOST`=your_smtp_server_host

`EMAIL_PORT`=your_smtp_server_port

`EMAIL_USER`=your_email_username

`EMAIL_PASSWORD`=your_email_password

`DEFAULT_FROM_EMAIL`=your_default_from_email



Replace the placeholder values with your actual SMTP server details and email account credentials.

3. **HTML Templates**

Place your Jinja2 HTML templates in a directory accessible by your script. Update the `FileSystemLoader` path in the script to point to your templates directory.

## Usage

To use the EmailUtils class to send an email:

# Send the email
```python3
EmailUtils.send_email(receiver_email, subject, html_file_path, context, attachments)
```



# License
This project is licensed under the MIT License - see the LICENSE file for details.
