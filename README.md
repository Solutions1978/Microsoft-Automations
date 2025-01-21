# Microsoft Automations

Welcome to **Microsoft Automations**, a collection of Python scripts and tools designed to automate and simplify tasks within the Microsoft ecosystem. This repository includes scripts for working with the Microsoft Graph API, automating email workflows in Outlook, managing files in OneDrive, and more.

## Features

- **Automated Email Attachment Downloader**:
  - Downloads attachments from all emails in your Outlook Inbox.
  - Handles pagination to process large volumes of emails.
  - Ensures secure authentication using the Microsoft Graph API and MSAL.

- **Secure Authentication**:
  - Implements OAuth 2.0 authentication via Azure Active Directory.
  - Supports both single-tenant and multi-tenant app configurations.

- **Scalable and Modular Code**:
  - Scripts are written with modularity in mind, allowing for easy customization and scalability.

- **Real-World Use Cases**:
  - Automates repetitive tasks, such as downloading attachments, managing email workflows, and handling large datasets.

## Prerequisites

Before using the scripts in this repository, ensure you have the following:

1. **Python 3.8 or later** installed on your system.
2. Required Python libraries:
   - `msal`
   - `requests`
3. A registered application in Azure Active Directory with the following:
   - **API permissions**: `Mail.Read`, `Mail.ReadWrite`
   - Redirect URI: `http://localhost` (or as per your configuration)
4. A Microsoft 365 account with access to the required resources (e.g., Outlook, OneDrive).

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/yourusername/Microsoft-Automations.git
cd Microsoft-Automations
