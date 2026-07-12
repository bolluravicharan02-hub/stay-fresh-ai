from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.invoice import Invoice, InvoiceItem
from app.schemas.invoice import InvoiceSchema


class DatabaseService:

    def __init__(self):
        self.db: Session = SessionLocal()

    def save_invoice(
        self,
        file_id: str,
        invoice: InvoiceSchema
    ) -> Invoice:

        db_invoice = Invoice(
            file_id=file_id,
            supplier_name=invoice.supplier_name,
            invoice_number=invoice.invoice_number,
            invoice_date=invoice.invoice_date,
            total_amount=invoice.total_amount,
            status="Processed"
        )

        self.db.add(db_invoice)
        self.db.commit()
        self.db.refresh(db_invoice)

        for item in invoice.items:

            db_item = InvoiceItem(
                invoice_id=db_invoice.id,
                product_name=item.product_name,
                barcode=item.barcode,
                quantity=item.quantity,
                purchase_price=item.purchase_price,
                mrp=item.mrp,
                selling_price=item.selling_price,
                discount=item.discount,
                gst=item.gst
            )

            self.db.add(db_item)

        self.db.commit()

        return db_invoice

    def get_invoice(self, invoice_id: int):

        return (
            self.db.query(Invoice)
            .filter(Invoice.id == invoice_id)
            .first()
        )

    def update_invoice(self, invoice_id: int, data: dict):

        invoice = (
            self.db.query(Invoice)
            .filter(Invoice.id == invoice_id)
            .first()
        )

        if not invoice:
            return None

        invoice.supplier_name = data["supplier_name"]
        invoice.invoice_number = data["invoice_number"]
        invoice.invoice_date = data["invoice_date"]
        invoice.total_amount = data["total_amount"]

        # Delete existing items
        self.db.query(InvoiceItem).filter(
            InvoiceItem.invoice_id == invoice.id
        ).delete()

        # Add updated items
        for item in data["items"]:

            db_item = InvoiceItem(
                invoice_id=invoice.id,
                product_name=item["product_name"],
                barcode=item["barcode"],
                quantity=item["quantity"],
                purchase_price=item["purchase_price"],
                mrp=item["mrp"],
                selling_price=item["selling_price"],
                discount=item["discount"],
                gst=item["gst"]
            )

            self.db.add(db_item)

        self.db.commit()
        self.db.refresh(invoice)
        return invoice

    def get_all_invoices(self):
        return (
            self.db.query(Invoice)
            .order_by(Invoice.id.desc())
            .all()
        )

    def approve_invoice(self, invoice_id: int):

        invoice = (
            self.db.query(Invoice)
            .filter(Invoice.id == invoice_id)
            .first()
        )

        if not invoice:
            return None

        invoice.status = "Approved"

        self.db.commit()
        self.db.refresh(invoice)

        return invoice