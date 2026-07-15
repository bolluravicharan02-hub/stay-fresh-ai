# PROJECT_CONTEXT.md

# VasyERP Supermarket Invoice Automation Agent

## Overview
This project automates supplier invoice entry into VasyERP for supermarket owners.

Current manual workflow:
1. Receive a printed supplier invoice.
2. Read every product manually.
3. Search/identify barcode when needed.
4. Open VasyERP.
5. Enter every product manually.
6. Save the invoice.

Target workflow:
1. User uploads an image or PDF.
2. OCR extracts invoice information.
3. AI structures supplier and product data.
4. Barcode lookup service finds missing barcodes.
5. User reviews extracted data.
6. After approval, Playwright/API enters data into VasyERP.
7. Success report is shown.

## Tech Stack

Backend
- FastAPI
- Python
- SQLAlchemy
- Pydantic
- Playwright
- OCR (Gemini/OCR pipeline)
- SQLite initially

Frontend
- Modern web UI
- Pastel colors
- Drag & Drop upload
- Review screen

## Architecture

Frontend
    ↓
FastAPI API
    ↓
Invoice Processing
    ├── OCR
    ├── AI Extraction
    ├── Validation
    ├── Barcode Lookup
    └── Approval
            ↓
VasyERP Integration
            ↓
Database

## Major Modules

- Authentication (future)
- Upload API
- OCR Service
- Invoice Parser
- Supplier Detection
- Product Extraction
- Barcode Lookup
- Review UI
- VasyERP Automation
- Logging
- Error Handling

## Functional Requirements

- Accept image/PDF invoices.
- Extract supplier details.
- Extract invoice metadata.
- Extract products.
- Preserve quantities, prices, GST, totals.
- Support user corrections.
- Never push to ERP without confirmation.

## Non-functional Requirements

- Modular architecture
- Easy to maintain
- Strong logging
- Recover from failures
- Production-ready code

## Current Status

Completed
- High-level architecture
- Module planning
- Tech stack selection
- API direction
- FastAPI structure planning

Remaining
- OCR implementation
- Data models
- Barcode service
- Approval workflow
- VasyERP integration
- Frontend
- Testing
- Deployment

## Coding Principles

- Clean architecture
- Small reusable services
- Dependency injection where appropriate
- Type hints
- Docstrings
- Minimal duplication
