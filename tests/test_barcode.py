from app.services.barcode import BarcodeAgent

agent = BarcodeAgent()

result = agent.search(
    "RAP NORMAL BOLT 500G"
)

print(result)