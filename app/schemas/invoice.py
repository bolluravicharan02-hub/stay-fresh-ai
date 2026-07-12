from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class InvoiceItemSchema(BaseModel):

    product_name: str

    barcode: Optional[str] = None

    quantity: float = 0

    purchase_price: float = 0

    mrp: float = 0

    selling_price: float = 0

    discount: float = 0

    gst: float = 0

    confidence: float = 0.0

    barcode_source: str = "unknown"


class InvoiceSchema(BaseModel):

    supplier_name: str

    invoice_number: str

    invoice_date: date

    gst_number: str | None = None

    total_amount: float

    items: List[InvoiceItemSchema]