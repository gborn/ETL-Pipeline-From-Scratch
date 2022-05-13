
from commons.base import Base, engine
# Import the PprRawAll table
from commons.tables import PprRawAll, PprCleanAll

# Create the table in the database
if __name__ == "__main__":
    print('creating tables', Base.metadata.tables)
    Base.metadata.create_all(engine)