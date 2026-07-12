from contextlib import asynccontextmanager

from app.models import Invoice, InvoiceItem

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_tables
from app.routes.uploads import router as upload_router
from app.routes.process import router as process_router
from app.routes.vasyerp import router as vasyerp_router
from app.routes.invoice import router as invoice_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Stay Fresh AI Backend...")

    create_tables()

    yield

    print("Stopping Stay Fresh AI Backend...")


app = FastAPI(
    title="Stay Fresh AI Backend",
    version="1.0.0",
    description="AI Powered Supplier Bill Automation for VasyERP",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(process_router)
app.include_router(vasyerp_router)
app.include_router(invoice_router)


@app.get("/")
def root():
    return {
        "project": "Stay Fresh AI Backend",
        "version": "1.0.0",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }