import gspread
import pickle
import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('exam_results')

print("Student Exam Record Book")
print("Please choose from the following options:")

while True:
    d = str(input("To search for a student press {}\n" "to add student press {}\n" "to delete a student press {}\n" "to exit press {}\n" "Please enter your option here:\n".format("(s)", "(a)", "(d)","(e)")))
 