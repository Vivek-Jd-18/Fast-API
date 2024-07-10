import firebase_admin
from firebase_admin import credentials, firestore
import os


# cred = credentials.Certificate(r"C:\Users\admin\Desktop\Learnings\FastAPI\git-project\Fast-API\app\credentials\aviato-02-firebase-adminsdk-83j9s-ed26195547.json")

# default_app = firebase_admin.initialize_app(cred)
# db = firestore.client()


relative_path = os.path.join(os.getcwd(), 'app', 'credentials', 'aviato-02-firebase-adminsdk-83j9s-ed26195547.json')

cred = credentials.Certificate(relative_path)
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()