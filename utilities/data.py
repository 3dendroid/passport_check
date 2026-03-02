import os

from dotenv import load_dotenv

load_dotenv()

application_number = [
    {
        "application_number": os.getenv("application_number"),
    }
]
