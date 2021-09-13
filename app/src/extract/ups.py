from src.extract.extractor import Extractor


class UpsExtractor(Extractor):
    display_name = 'UPS Invoice'
    column_mapping = {
        'Recipient Number': 'recipient_number',
        'Invoice Date': 'invoice_date',
        'Transaction Date': 'transaction_date',
        'Net Amount': 'net_amount',
        'Tracking Number': 'tracking_number',
    }
    sheet_name = 'accrual'
