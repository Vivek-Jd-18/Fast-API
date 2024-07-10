import firebase_admin
from firebase_admin import credentials, firestore
import os
from .etc.secrets import firebase_creds

cred = credentials.Certificate(firebase_creds.firebase_credentials)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()