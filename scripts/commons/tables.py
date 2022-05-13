
from sqlalchemy import Column, Integer, String, Date, cast
# Import the function required
from sqlalchemy.orm import column_property

from commons.base import Base

class PprRawAll(Base):
    __tablename__ = "ppr_raw_all"

    id = Column(Integer, primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(255))

    # Create transaction_id which will act a unique key
    transaction_id = column_property(
        date_of_sale + "_" + address + "_" + county + "_" + price
    )

class PprCleanAll(Base):
    __tablename__ = "ppr_clean_all"

    id = Column(Integer, primary_key=True)
    date_of_sale = Column(Date)
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(Integer)
    description = Column(String(255))

    # Create a unique transaction id
    # all non-string columns are casted as string
    transaction_id = column_property(
        cast(date_of_sale, String) + "_" + address + "_" + county + "_" + cast(price, String)
    )
