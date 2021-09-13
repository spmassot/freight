from src.extract.extractor import Extractor


class AccessQueryExtractor(Extractor):
    display_name = 'Access Query'
    column_mapping = {
        'thing': 'pick_ticket',
        'Company': 'company',
        'LOB': 'line_of_business',
        'SumOfCost': 'sum_of_cost',
    }
