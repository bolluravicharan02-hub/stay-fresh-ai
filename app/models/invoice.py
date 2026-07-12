from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from app.database import Base


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    file_id = Column(String, unique=True, nullable=False)

    supplier_name = Column(String)

    invoice_number = Column(String)

    invoice_date = Column(Date)

    total_amount = Column(Float)

    status = Column(
        String,
        default="Uploaded"
    )

    items = relationship(
        "InvoiceItem",
        back_populates="invoice",
        cascade="all, delete-orphan"
    )


class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True, index=True)

    invoice_id = Column(
        Integer,
        ForeignKey("invoices.id")
    )

    product_name = Column(String)

    barcode = Column(String)

    quantity = Column(Float)

    purchase_price = Column(Float)

    mrp = Column(Float)

    selling_price = Column(Float)

    discount = Column(Float)

    gst = Column(Float)

    invoice = relationship(
        "Invoice",
        back_populates="items"
    )