##import keyring
import tableauserverclient as tsc
import smtplib
from email.message import EmailMessage
from datetime import timezone

WORKBOOK_NAME = "Maheen Textile Working"
VIEW_NAME = "Maheen Textile Dashboard"


def main():
    # Setup
    # Store token name, token value, and site ID in variables.
    token_name = 'TSM Token'
    token_value = 'hYZG7mUDSVCSovbnwWpgXg==:nZgIs8FQRifWQ2KqRHDqmLBZElSsurH4'
    site_id = 'zahid-c655e788a3'
    # Create authentication object using the token and site ID details.
    tableau_auth = tsc.PersonalAccessTokenAuth(token_name=token_name, personal_access_token=token_value, site_id=site_id)
    # Create a tableau server client object using specified server URL.
    server = tsc.Server('https://prod-apnortheast-a.online.tableau.com')
    # Disable certificate verification. The next line of code may be required due to certificate issues.
    # server.add_http_options({'verify': False})

    # Sign-in to server.
    with server.auth.sign_in(tableau_auth):
        # Ensure the most recent Tableau REST API version is used.
        server.use_highest_version()
        # Display server info.
        print(server.server_info)

    # -----------------------
    # Get Workbook
    # -----------------------
        all_workbooks, _ = server.workbooks.get()
        workbook = next(w for w in all_workbooks if w.name == WORKBOOK_NAME)
        print(workbook)

    # -----------------------
    # Get Last Extract Refresh Time
    # -----------------------
        server.workbooks.populate_connections(workbook)

        extract_time = None
        for conn in workbook.connections:
         if conn.connection_type == "extract":
            extract_time = conn.updated_at.astimezone(timezone.utc)

        ##if not extract_time:
         ##raise Exception("No extract found for workbook")
        print(extract_time)
    # -----------------------
    # Export Dashboard Image
    # -----------------------
        server.workbooks.populate_views(workbook)
        view = next(v for v in workbook.views if v.name == VIEW_NAME)

        image_req = tsc.ImageRequestOptions()
        server.views.populate_image(view, image_req)
        
        image_path = f"C:\TableauExport\{VIEW_NAME}.png"
        with open(image_path, "wb") as f:
         f.write(view.image)
         print(image_path)

if __name__ == '__main__':
    main()