from params_ import *


class OpticalDistanceSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'optical_distance_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/optische_abstandssensoren/'
        self.payload['grp_id'] = 'A1-2-1-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Type of scanning system',
                                'Special design',
                                'Light source',
                                'Measurement range',
                                'Geometric resolution',
                                'Accuracy of measurement, distant range',
                                'Measuring accuracy',
                                'Absolute measurement accuracy',
                                'Type',
                                'Type 2',
                                'Switching element',
                                'Switching element 2',
                                'Supply voltage',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class UltrasonicDistanceSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'ultrasonic_distance_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/ultraschall_abstandssensoren/'
        self.payload['grp_id'] = 'A1-2-1-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Measurement range',
                                'Geometric resolution',
                                'Measuring accuracy',
                                'Type',
                                'Current',
                                'Voltage',
                                'Switching element',
                                'Switching principle',
                                'Supply voltage',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (Ø x L)',
                                'Degree of protection']


class OpticalLaserMeasuringSystem(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'optical_laser_measuring_systems'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/sensoren_zur_positionierung/ams_3_i_3/'
        self.payload['grp_id'] = 'A1-2-2-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Functions',
                                'Light source',
                                'Measurement range',
                                'Absolute measurement accuracy',
                                'Type',
                                'Supply voltage',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class BarCodePositioningSystem(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'bar_code_positioning_systems'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/sensoren_zur_positionierung/bps_8_34_3/'
        self.payload['grp_id'] = 'A1-2-2-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Functions',
                                'Working range',
                                'Light source',
                                'Type',
                                'Type 2',
                                'Supply voltage',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class LightSection(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'light_section'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/3d_sensoren_1/lichtschnittsensoren_1/'
        self.payload['grp_id'] = 'A1-2-3'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Special design',
                                'Supply voltage',
                                'Switching element',
                                'Switching element 2',
                                'Switching element 3',
                                'Switching element 4',
                                'Switching element 5',
                                'Switching element 6',
                                'Type',
                                'Type of connection',
                                'Thread size',
                                'Type of connection 2',
                                'Thread size 2',
                                'Type of connection 3',
                                'Thread size 3',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class LightCurtainMeasuring(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'light_curtains_measuring'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/lichtvorhaenge_1/'
        self.payload['grp_id'] = 'A1-2-4'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Operating principle',
                                'Device type',
                                'Application',
                                'Operating range',
                                'Measurement field length',
                                'Supply voltage',
                                'Type',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class ForkedMeasuring(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'forked_measuring'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/messende_sensoren/messende_gabelsensoren/'
        self.payload['grp_id'] = 'A1-2-5'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Measurement field length',
                                'Light source',
                                'Supply voltage',
                                'Type',
                                'Type 2',
                                'Function',
                                'Mouth width',
                                'Mouth depth',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']