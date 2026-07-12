from app.services.barcode.google_sheet_service import GoogleSheetService

service = GoogleSheetService()

result = service.search(
    "COMFORT FAB CON BLUE 210ML"
)

print(result)