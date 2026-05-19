 ##Prerequisites
##pip install tableauserverclient pillow


##/Python Script (tableau_extract_email.py)
import tableauserverclient as TSC
import smtplib
from email.message import EmailMessage
from datetime import timezone

# -----------------------
# Tableau Config
# -----------------------
TABLEAU_SERVER = "https://prod-apnortheast-a.online.tableau.com"
SITE_ID = "zahid-c655e788a3"              # empty for Default site
PAT_NAME = "TSM Token"
PAT_SECRET = "hYZG7mUDSVCSovbnwWpgXg==:nZgIs8FQRifWQ2KqRHDqmLBZElSsurH4"

WORKBOOK_NAME = "LBL Dashboard"
VIEW_NAME = "Main View"

# -----------------------
# Email Config
# -----------------------
SMTP_SERVER = "smtp.yourcompany.com"
SMTP_PORT = 587
EMAIL_FROM = "tableau@yourcompany.com"
EMAIL_TO = ["business@yourcompany.com"]

# -----------------------
# Tableau Login
# -----------------------
auth = TSC.PersonalAccessTokenAuth(
    PAT_NAME, PAT_SECRET, SITE_ID
)
server = TSC.Server(TABLEAU_SERVER, use_server_version=True)

with server.auth.sign_in(auth):

    # -----------------------
    # Get Workbook
    # -----------------------
    all_workbooks, _ = server.workbooks.get()
    workbook = next(w for w in all_workbooks if w.name == WORKBOOK_NAME)

    # -----------------------
    # Get Last Extract Refresh Time
    # -----------------------
    server.workbooks.populate_connections(workbook)

    extract_time = None
    for conn in workbook.connections:
        if conn.connection_type == "extract":
            extract_time = conn.updated_at.astimezone(timezone.utc)

    if not extract_time:
        raise Exception("No extract found for workbook")

    # -----------------------
    # Export Dashboard Image
    # -----------------------
    server.workbooks.populate_views(workbook)
    view = next(v for v in workbook.views if v.name == VIEW_NAME)

    image_req = TSC.ImageRequestOptions()
    server.views.populate_image(view, image_req)
        
    image_path = f"C:\TableauExport\{VIEW_NAME}.png"
    with open(image_path, "wb") as f:
         f.write(view.image)
        

# -----------------------
# Send Email
# -----------------------
msg = EmailMessage()
msg["Subject"] = "LBL Dashboard – Extract Completed"
msg["From"] = EMAIL_FROM
msg["To"] = ", ".join(EMAIL_TO)

msg.set_content(f"""
Extract Refresh Completed Successfully

Workbook: {WORKBOOK_NAME}
Last Refresh Time (UTC): {extract_time}
""")

with open(image_path, "rb") as img:
    msg.add_attachment(
        img.read(),
        maintype="image",
        subtype="png",
        filename="dashboard.png"
    )

with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.send_message(msg)

print("Email sent successfully")