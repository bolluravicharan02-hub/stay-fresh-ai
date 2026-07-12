from fastapi import APIRouter, HTTPException

from app.services.invoice_processor import InvoiceProcessor

router = APIRouter(
    prefix="/process",
    tags=["Invoice Processing"]
)

processor = InvoiceProcessor()


@router.post("/{file_id}")
async def process_invoice(file_id: str):

    try:

        file_path = f"uploads/{file_id}"

        invoice_id, invoice = processor.process(file_path)

        return {
            "success": True,
            "message": "Invoice processed successfully.",
            "invoice_id": invoice_id,
            "invoice": invoice.model_dump()
        }

    except FileNotFoundError:

        raise HTTPException(
            status_code=404,
            detail="Invoice file not found."
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )