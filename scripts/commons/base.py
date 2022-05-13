
# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
import os 

endpoint="postgresql+psycopg2://{}:{}@{}?port={}&dbname={}".format(
    os.environ['DATABASE_USER'],
    os.environ['DATABASE_PASS'],
    os.environ['DATABASE_HOST'],
    os.environ['DATABASE_PORT'],
    os.environ['DATABASE_NAME'],
)

# Create the engine
engine = create_engine(endpoint)
print('Connecting to', engine)

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()