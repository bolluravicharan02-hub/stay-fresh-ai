from datetime import datetime

from fastapi import APIRouter, HTTPException

from app.schemas import InvoiceSchema
from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/invoice",
    tags=["Invoice"]
)

database = DatabaseService()


@router.get("/{invoice_id}")
async def get_invoice(invoice_id: int):

    invoice = database.get_invoice(invoice_id)

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found."
        )

    return {
        "success": True,
        "invoice": {
            "id": invoice.id,
            "supplier_name": invoice.supplier_name,
            "invoice_number": invoice.invoice_number,
            "invoice_date": invoice.invoice_date,
            "total_amount": invoice.total_amount,
            "status": invoice.status,
            "items": [
                {
                    "id": item.id,
                    "product_name": item.product_name,
                    "barcode": item.barcode,
                    "quantity": item.quantity,
                    "purchase_price": item.purchase_price,
                    "mrp": item.mrp,
                    "selling_price": item.selling_price,
                    "discount": item.discount,
                    "gst": item.gst
                }
                for item in invoice.items
            ]
        }
    }


@router.put("/{invoice_id}")
async def update_invoice(
    invoice_id: int,
    invoice: InvoiceSchema
):

    existing = database.get_invoice(invoice_id)

    if not existing:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found."
        )

    data = invoice.model_dump()

    # Convert string date to Python date object
    if isinstance(data["invoice_date"], str):
        data["invoice_date"] = datetime.strptime(
            data["invoice_date"],
            "%Y-%m-%d"
        ).date()

    updated_invoice = database.update_invoice(
        invoice_id,
        data
    )

    return {
        "success": True,
        "message": "Invoice updated successfully.",
        "invoice_id": updated_invoice.id
    }


@router.post("/{invoice_id}/approve")
async def approve_invoice(invoice_id: int):

    invoice = database.get_invoice(invoice_id)

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found."
        )

    invoice.status = "Approved"

    database.db.commit()

    return {
        "success": True,
        "message": "Invoice approved successfully."
    }