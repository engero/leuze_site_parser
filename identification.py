from params_ import *


class StationaryBarcodeReaders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'stationary_barcode_readers'
        self.product_url = 'https://www.leuze.de/en/deutschland/produkte/identifikation/barcode_identifikation/stationaere_barcodeleser/'
        self.payload['grp_id'] = 'A1-4-1-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Code types, readable',
                                'Reading distance',
                                'Module size',
                                'Reading method',
                                'Type',
                                'Type 2',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class MobileBarcodeReaders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'mobile_barcode_readers'
        self.product_url = 'https://www.leuze.de/en/deutschland/produkte/identifikation/barcode_identifikation/mobile_barcodeleser/'
        self.payload['grp_id'] = 'A1-4-1-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Code types, readable',
                                'Reading distance',
                                'Module size',
                                'Reading method',
                                'Type',
                                'Type of connection',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class Stationary2DCodeReaders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'stationary_2dcode_readers'
        self.product_url = 'https://www.leuze.de/en/deutschland/produkte/identifikation/2d_code_identifikation/stationaere_2d_codeleser/'
        self.payload['grp_id'] = 'A1-4-2-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Working range',
                                'Software functions',
                                'Code types, readable',
                                'Reading distance',
                                'Module size',
                                'Type',
                                'Type 2',
                                'Type 3',
                                'Type 4',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class Mobile2DCodeReaders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'mobile_2dcode_readers'
        self.product_url = 'https://www.leuze.de/en/deutschland/produkte/identifikation/2d_code_identifikation/mobile_2d_codeleser/'
        self.payload['grp_id'] = 'A1-4-2-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Code types, readable',
                                'Reading distance',
                                'Module size',
                                'Type',
                                'Type of connection',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class RFIDReaders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'rfid_readers'
        self.product_url = 'https://www.leuze.de/en/deutschland/produkte/identifikation/rf_identifikation/stationaere_rfid_schreib_lesesysteme/'
        self.payload['grp_id'] = 'A1-4-3-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Working frequency',
                                'Functions',
                                'Reading/writing range, max.',
                                'Transponder, readable',
                                'Type',
                                'Design',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Dimension',
                                'Degree of protection']


class Transponders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'transponders'
        self.product_url = 'https://www.leuze.de/en/deutschland/produkte/identifikation/rf_identifikation/transponder_2/'
        self.payload['grp_id'] = 'A1-4-3-3'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Suitable for',
                                'Working frequency',
                                'Design',
                                'Housing material',
                                'Degree of protection']