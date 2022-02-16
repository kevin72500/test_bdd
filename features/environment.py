from dotenv import load_dotenv
load_dotenv(verbose=True)
import os
host=os.getenv("host")
port=os.getenv("port")