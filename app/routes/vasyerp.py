from fastapi import APIRouter, HTTPException

from app.services.database_service import DatabaseService
from app.services.playwright.playwright_service import PlaywrightService

router = APIRouter(
    prefix="/vasyerp",
    tags=["VasyERP"]
)

database = DatabaseService()
playwright = PlaywrightService()


@router.post("/{invoice_id}")
async def sync_invoice(invoice_id: int):

    invoice = database.get_invoice(invoice_id)

    if not invoice:
        raise HTTPException(
            status_code=404,
            detail="Invoice not found."
        )

    if invoice.status != "Approved":
        raise HTTPException(
            status_code=400,
            detail="Invoice is not approved."
        )

    playwright.sync_invoice(invoice)

    invoice.status = "Synced"
    database.db.commit()

    return {
        "success": True,
        "message": "Invoice synced successfully."
    }