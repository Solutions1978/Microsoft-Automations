import os
import requests
from msal import PublicClientApplication  # type: ignore

# Azure App details (replace placeholders with your actual details)
CLIENT_ID = "your-client-id-here"  # Replace with your Application (client) ID
AUTHORITY = "https://login.microsoftonline.com/your-tenant-id-here"  # Replace with your Tenant ID or use 'common' for multi-tenant
SCOPES = ["Mail.Read", "Mail.ReadWrite"]

# Initialize the MSAL client
app = PublicClientApplication(CLIENT_ID, authority=AUTHORITY)

# Get an access token
accounts = app.get_accounts()
if accounts:
    # If an account is already logged in, acquire token silently
    result = app.acquire_token_silent(SCOPES, account=accounts[0])
else:
    # Interactive login (defaults to http://localhost as the redirect URI)
    result = app.acquire_token_interactive(SCOPES)

if "access_token" in result:
    token = result["access_token"]

    # API request to get emails
    headers = {"Authorization": f"Bearer {token}"}
    base_url = "https://graph.microsoft.com/v1.0/me/messages"
    save_folder = r"C:\path\to\your\attachment\folder"
    next_link = base_url

    while next_link:
        response = requests.get(next_link, headers=headers)

        if response.status_code == 200:
            data = response.json()
            emails = data.get("value", [])

            for email in emails:
                if email.get("hasAttachments"):
                    message_id = email["id"]
                    # Get attachments for the email
                    attachment_url = f"https://graph.microsoft.com/v1.0/me/messages/{message_id}/attachments"
                    attachment_response = requests.get(attachment_url, headers=headers)

                    if attachment_response.status_code == 200:
                        attachments = attachment_response.json().get("value", [])
                        for attachment in attachments:
                            file_name = attachment["name"]
                            file_content = attachment["contentBytes"]

                            # Save the attachment
                            file_path = os.path.join(save_folder, file_name)
                            with open(file_path, "wb") as file:
                                file.write(file_content.encode("utf-8"))
                            print(f"Downloaded: {file_name}")
            # Get the next page link
            next_link = data.get("@odata.nextLink")
        else:
            print(f"Failed to fetch messages: {response.status_code}, {response.text}")
            break
else:
    print(f"Authentication failed: {result.get('error_description')}")
