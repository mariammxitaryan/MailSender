# Simple Email Sender

A Python script to send emails using the `smtplib` library.

## Description

This script provides a simple command-line interface for sending emails. It securely obtains the sender's email address and password, allows you to compose a message with a subject and body, and then sends the email to the specified recipient.

## Features

* **Secure Password Input:** Uses `getpass.getpass()` to hide password input.
* **Email Composition:** Allows you to specify the recipient, subject, and body of the email.
* **SMTP Handling:** Connects to the SMTP server (currently configured for Gmail) to send the email.
* **Error Handling:** Includes error handling for SMTP exceptions to provide feedback on sending success or failure.

## Prerequisites

* Python 3.x installed on your system.
* A Gmail account (or modify the script for another email provider).
* **Important Security Note:** For Gmail, you might need to enable "less secure app access" in your Google account settings for this script to work.  **However, this is NOT recommended for production or long-term use.** A more secure approach is to use OAuth 2.0.

## How to Use

1.  **Clone the repository (or download the script):**

2.  **Run the script:**
    ```bash
    python email_sender.py
    ```

3.  **Follow the prompts:**
    * Enter your email address.
    * Enter your email password (it will be hidden).
    * Enter the recipient's email address.
    * Enter the subject of the email.
    * Enter the body of the email.  Press Enter twice to finish entering the body.

4.  **Check the output:** The script will display a message indicating whether the email was sent successfully or if an error occurred.

## Code Overview

Here's a brief overview of the main functions in the script:

* `get_credentials()`:  Gets the sender's email address and password using `input()` and `getpass.getpass()`.
* `compose_message(sender, recipient, subject, body)`:  Creates a `MIMEText` object representing the email message.
* `send_email(sender, password, recipient, msg)`:  Connects to the SMTP server, logs in, sends the message, and handles potential errors.
* `main()`:  The main function that orchestrates the email sending process.

