from dotenv import load_dotenv
import os
import redis

load_dotenv()

class AppConfig:
    SECRET_KEY=os.environ["SECRET_KEY"]