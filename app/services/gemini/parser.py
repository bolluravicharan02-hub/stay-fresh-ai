from datetime import datetime

from app.schemas import (
    InvoiceSchema,
    InvoiceItemSchema
)


class InvoiceParser:

    def parse(
        self,
        data: dict
    ) -> InvoiceSchema:

        items = []

        for item in data.get("items", []):

            items.append(
                InvoiceItemSchema(
                    product_name=item.get(
                        "product_name",
                        ""
                    ),
                    barcode=item.get(
                        "barcode",
                        ""
                    ),
                    quantity=float(
                        item.get(
                            "quantity",
                            0
                        )
                    ),
                    purchase_price=float(
                        item.get(
                            "purchase_price",
                            0
                        )
                    ),
                    mrp=float(
                        item.get(
                            "mrp",
                            0
                        )
                    ),
                    selling_price=float(
                        item.get(
                            "mrp",
                            0
                        )
                    ),
                    discount=float(
                        item.get(
                            "discount",
                            0
                        )
                    ),
                    gst=float(
                        item.get(
                            "gst",
                            0
                        )
                    )
                )
            )

        invoice_date = datetime.strptime(
            data["invoice_date"],
            "%Y-%m-%d"
        ).date()

        return InvoiceSchema(

            supplier_name=data.get(
                "supplier_name",
                ""
            ),

            invoice_number=data.get(
                "invoice_number",
                ""
            ),

            invoice_date=invoice_date,

            total_amount=float(
                data.get(
                    "total_amount",
                    0
                )
            ),

            items=items
        )