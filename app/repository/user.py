from fastapi import FastAPI, Depends, Response, status, HTTPException, APIRouter
from .. import schemas, models
import smtplib
from email.mime.text import MIMEText
import datetime
from ..db import db



def create(request):
    user_data = request.dict()

    if 'dob' in user_data and isinstance(user_data['dob'], datetime.date):
        user_data['dob'] = user_data['dob'].isoformat()

    users_ref = db.collection('users')
    doc_ref = users_ref.document()

    user_data['id'] = doc_ref.id

    doc_ref.set(user_data)

    return {
        "id": doc_ref.id,
        "data": user_data
    }

def get_all():
    users_ref = db.collection('users')
    all_users = [doc.to_dict() for doc in users_ref.get()]
    return all_users

def get_user(id: str):
    users_ref = db.collection('users')
    user_doc = users_ref.document(id).get()

    if not user_doc.exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    return user_doc.to_dict()

def update(request):
    user_data = request.dict()

    if 'dob' in user_data and isinstance(user_data['dob'], datetime.date):
        user_data['dob'] = user_data['dob'].isoformat()

    users_ref = db.collection('users')
    user_ref = users_ref.document(user_data['id'])

    if not user_ref.get().exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user_ref.update(user_data)
    return user_ref.get().to_dict()

def delete(id: str):
    users_ref = db.collection('users')
    user_ref = users_ref.document(id)

    if not user_ref.get().exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

    user_ref.delete()
    return {"data": "deleted!"}


def send_invitation(recipients):
    subject = "API Documentation Invitation"
    public_url = "http://54.167.19.161:8000"
    body = f"""
    <!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>API Documentation Invitation</title>
    <style>
      body {{
        font-family: 'Verdana', sans-serif;
        background-color: #eaeaea;
        margin: 0;
        padding: 0;
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }}
      .wrapper {{
        max-width: 700px;
        margin: 50px auto;
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        overflow: hidden;
      }}
      .main-header {{
        background-color: #292b2c;
        color: #ffffff;
        padding: 25px;
        text-align: center;
      }}
      .main-header h1 {{
        font-size: 26px;
        margin: 0;
      }}
      .main-content {{
        padding: 25px;
        color: #444444;
      }}
      .main-content h2 {{
        color: #292b2c;
      }}
      .main-content p {{
        line-height: 1.5;
      }}
      .main-footer {{
        background-color: #292b2c;
        color: #ffffff;
        padding: 15px;
        text-align: center;
      }}
      .cta-button {{
        display: block;
        width: 80%;
        margin: 20px auto;
        padding: 12px 0;
        font-size: 18px;
        color: #ffffff;
        background-color: #292b2c;
        text-align: center;
        text-decoration: none;
        border-radius: 8px;
      }}
      .cta-button:hover {{
        background-color: #3d3f40;
      }}
    </style>
  </head>
  <body>
    <div class="wrapper">
      <header class="main-header">
        <h1>Invitation to API Documentation</h1>
      </header>
      <section class="main-content">
        <h2>Hello,</h2>
        <p>
          We are thrilled to extend an invitation for you to explore our User Management API documentation via
          <strong>ReDoc</strong>.
        </p>
        <p>
          Please click the link below to access the documentation:
        </p>
        <a href="{public_url}/redoc" class="cta-button">View API Documentation</a>
        <p>
          As per the requirements, the 'Any' method was modified due to Flutter.
        </p>
        <p>
          Additionally, I have configured an AWS EC2 instance with a public IP, utilized a Reverse Proxy for port forwarding, and set up a GCP Postgres database.
        </p>
        <p>
          We value your input and look forward to your feedback.
        </p>
      </section>
      <footer class="main-footer">
        <p>Thank you!,<br />Vivek Dhage</p>
        <p>If you have any questions, please reply to this email.</p>
      </footer>
    </div>
  </body>
</html>
    """

    msg = MIMEText(body, "html")
    msg["Subject"] = subject
    msg["From"] = "vivekjd90@gmail.com"
    msg["To"] = ", ".join(recipients)

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "vivekjd90@gmail.com"
    smtp_password = "phis mrxz psvs kkos"  

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, recipients, msg.as_string())
        print("Invitation sent!!!")
    except Exception as e:
        print(f"Failed to send Invitation: {e}")
