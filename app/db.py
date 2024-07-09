import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate(r"C:\Users\admin\Desktop\Learnings\FastAPI\aviato-task\credentials\aviato-01-firebase-adminsdk-99aa1-ee8ba4ad8b.json")
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()