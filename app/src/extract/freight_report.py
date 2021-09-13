import pandas as pd
from io import BytesIO

from src.extract.extractor import Extractor


class FreightExtractor(Extractor):
    display_name = 'FRTDPB13'
    column_mapping = {
        'Pick Ticket': 'pick_ticket',
        'Order': 'order_number',
        'Doc#': 'document_number',
        'Freight Cost': 'freight_cost',
        'Company': 'company',
        'Business Unit': 'business_unit',
        'Carrier#': 'carrier_number',
        'Cost': 'cost',
        'Customer#': 'customer_number',
        'Freight Sales': 'freight_sales',
        'Invoice': 'invoice',
        'Sales': 'sales',
        'Ship Day': 'ship_day',
        'Ship Month': 'ship_month',
        'Ship To': 'ship_to',
        'Ship Year': 'ship_year',
        'Warehouse': 'warehouse',
        'Original Pick Ticket 1': 'original_pick_ticket_1',
        'Original Pick Ticket 2': 'original_pick_ticket_2',
        'Original Pick Ticket 3': 'original_pick_ticket_3',
    }
