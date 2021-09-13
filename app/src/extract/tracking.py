import pandas as pd
from io import BytesIO

from src.extract.extractor import Extractor


class TrackingExtractor(Extractor):
    display_name = 'FRTDPB14'
    column_mapping = {
        'Tracking Number': 'tracking_number',
        'Pick Ticket': 'pick_ticket',
    }
