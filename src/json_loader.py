import os
import json


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_config():
    CONFIG_PATH = os.path.join(BASE_DIR, "..", "config.json")
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
    return config

def load_emails():
    CONFIG_PATH = os.path.join(BASE_DIR, "..", "emails.json")
    with open(CONFIG_PATH, "r") as f:
        emails = json.load(f)
    return emails
 

        
        