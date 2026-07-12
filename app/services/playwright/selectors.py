class Selectors:
    """
    All VasyERP selectors in one place.
    """

    # ----------------------------
    # Login
    # ----------------------------
    USERNAME = 'input[name="username"]'
    PASSWORD = 'input[name="password"]'
    LOGIN_BUTTON = 'button[type="submit"]'

    # ----------------------------
    # Navigation
    # ----------------------------
    PURCHASE_MENU = 'a:has-text("Purchase")'
    SUPPLIER_BILLS = 'a:has-text("Supplier Bills")'
    CREATE_NEW = 'a:has-text("Create New")'

    # ----------------------------
    # Supplier
    # ----------------------------
    SUPPLIER_SEARCH = 'input[type="search"]'

    # ----------------------------
    # Product Search
    # ----------------------------
    BARCODE_SEARCH = 'input[placeholder="Scan Barcode/Enter Product"]'

    # ----------------------------
    # Save
    # ----------------------------
    SAVE_BUTTON = "#save_purchase"

    # ==================================================
    # Dynamic Row Selectors
    # ==================================================

    @staticmethod
    def qty(index: int):
        return f'input[name="purchaseItemVos[{index}].qty"]'

    @staticmethod
    def purchase_price(index: int):
        return f"#price{index}"

    @staticmethod
    def selling_price(index: int):
        return f"#sellingPrice{index}"

    @staticmethod
    def amount(index: int):
        return f"#itemamount{index}"