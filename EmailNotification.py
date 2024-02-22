import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from jinja2 import Environment, FileSystemLoader
from dotenv import dotenv_values
config = dotenv_values(".env")

class EmailUtils:
    @staticmethod
    def send_email(receiver_email, subject, html_file_path, context, attachments=None):
        print(receiver_email)
        EMAIL_HOST = config['EMAIL_HOST']
        EMAIL_PASSWORD = config['EMAIL_PASSWORD']
        EMAIL_USER = config['EMAIL_USER']
        EMAIL_PORT = config['EMAIL_PORT']
        DEFAULT_FROM_EMAIL = config['DEFAULT_FROM_EMAIL']

        # Create a Jinja2 environment to load templates from the filesystem
        env = Environment(loader=FileSystemLoader('/'))  # You can set the path to the templates directory

        # Load the HTML template using the Jinja2 environment
        template = env.get_template(html_file_path)

        # Render the template with the provided context data
        rendered_html = template.render(context)

        # Create a multipart message and set the headers
        msg = MIMEMultipart()
        msg['From'] = f'Your Name <{DEFAULT_FROM_EMAIL}>'
        msg['To'] = ', '.join(receiver_email)
        msg['Cc'] = '' # Add cc email list separated by comma(,)
        msg['Subject'] = subject

        # Attach the rendered HTML content as the email body
        msg.attach(MIMEText(rendered_html, 'html'))

        # Add other attachments, if provided
        if attachments:
            for attachment_path in attachments:
                with open(attachment_path['path'], 'rb') as attachment_file:
                    attachment = MIMEApplication(attachment_file.read())
                    attachment.add_header('Content-Disposition', 'attachment', filename=attachment_path['name'])
                    msg.attach(attachment)

        # Create a secure SSL/TLS connection to the SMTP server
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()

        # Login to the email account
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        # Send the email
        recipients = receiver_email
        server.sendmail(DEFAULT_FROM_EMAIL, recipients, msg.as_string())

        # Disconnect from the server
        server.quit()

