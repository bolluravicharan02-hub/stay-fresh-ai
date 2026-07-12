from datetime import date

from app.schemas import InvoiceSchema, InvoiceItemSchema
from app.services.playwright import PlaywrightService


invoice = InvoiceSchema(
    supplier_name="VIRUPAKSHI ENTERPRISES",
    invoice_number="TEST001",
    invoice_date=date.today(),
    total_amount=1000,
    items=[
        InvoiceItemSchema(
            product_name="RAP NORMAL BOLT 500G",
            barcode="8901030737091",
            quantity=10,
            purchase_price=40.76,
            mrp=53,
            selling_price=53,
            discount=0,
            gst=18
        ),
        InvoiceItemSchema(
            product_name="COMFORT FAB CON BLUE 210ML",
            barcode="8909106022003",
            quantity=5,
            purchase_price=45.64,
            mrp=60,
            selling_price=60,
            discount=0,
            gst=18
        ),
        InvoiceItemSchema(
            product_name="vim pouch 25rs",
            barcode="8909106084261",
            quantity=6,
            purchase_price=19.62,
            mrp=25,
            selling_price=25,
            discount=0,
            gst=18
        )
    ]
)

service = PlaywrightService()

service.sync_invoice(invoice)