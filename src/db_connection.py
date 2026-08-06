import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def obter_engine():
    url = (
        f'postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}'
        f'@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}'
    )

    return create_engine(url)