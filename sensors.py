from params_ import *


class PhotoSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'photo_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/optische_sensoren/'
        self.payload['grp_id'] = 'A1-1-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Operating principle',
                                'Operating range limit',
                                'Supply voltage',
                                'Light source',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Type',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Design',
                                'Degree of protection',
                                'Application',
                                'Operating range, white 90%']


class InductiveSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'inductive_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/induktive_sensoren/'
        self.payload['grp_id'] = 'A1-1-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Typ. operating range limit Sn',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Type of connection',
                                'Thread size',
                                'Thread size 2',
                                'Housing material',
                                'Dimension (Ø x L)',
                                'Dimension (W x H x L)',
                                'Design',
                                'Type of installation',
                                'Degree of protection']


class CapacitiveSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'capacitive_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/kapazitive_sensoren/'
        self.payload['grp_id'] = '1488804867078'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Assured switching distance',
                                'Switching distance Sn (non-embedded installation)',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Type of connection',
                                'Thread size',
                                'Thread size 2',
                                'Housing material',
                                'Dimension (Ø x L)',
                                'Dimension (W x H x L)',
                                'Design',
                                'Type of installation',
                                'Degree of protection']


class UltrasonicSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'ultrasonic_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/ultraschall_sensoren/'
        self.payload['grp_id'] = 'A1-1-3'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Operating principle',
                                'Special design',
                                'Operating range',
                                'Operating range 2',
                                'Direction of beam',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Type of connection',
                                'Thread size',
                                'Design',
                                'Thread size 2',
                                'Housing material',
                                'Dimension (Ø x L)',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class FiberOpticAmplifier(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'fiber_optic_amplifiers'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/faseroptische_sensoren_2/verstaerker/'
        self.payload['grp_id'] = 'A1-1-4-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Light source',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Switching frequency',
                                'Type',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)']


class FiberOpticSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'fiber_optic_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/faseroptische_sensoren_2/lichtleiter/'
        self.payload['grp_id'] = 'A1-1-4-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Operating principle',
                                'Area of application',
                                'Light beam exit',
                                'Fiber core',
                                'Special design',
                                'Design',
                                'Type',
                                'Fiber sheathing material']


class ForkedObjectDetection(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'forked_object_detection'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/gabelsensoren/gabeln_fuer_objekterkennung/'
        self.payload['grp_id'] = 'A1-1-5-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Light source',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching frequency',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Mouth width',
                                'Mouth depth',
                                'Degree of protection']


class ForkedLabelDetection(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'forked_label_detection'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/gabelsensoren/gabeln_fuer_etikettenerkennung/'
        self.payload['grp_id'] = 'A1-1-5-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Principle of physics',
                                'Application',
                                'Label width',
                                'Label gap',
                                'Special design',
                                'Light source',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Switching frequency',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Mouth width',
                                'Mouth depth',
                                'Degree of protection']


class LightCurtain(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'light_curtains'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/lichtvorhaenge/'
        self.payload['grp_id'] = 'A1-1-6'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Operating principle',
                                'Application',
                                'Device type',
                                'Operating range',
                                'Operating range 2',
                                'Measurement field length',
                                'Beam spacing',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Switching frequency',
                                'Type of connection',
                                'Thread size',
                                'Type of connection 2',
                                'Thread size 2',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class LightSection3D(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'light_section_3D'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/3d_sensoren/lichtschnittsensoren/'
        self.payload['grp_id'] = '1340615756902_1340615756901'
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


class LaserScanner3D(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'laser_scanners_3d'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/3d_sensoren/laserscanner/'
        self.payload['grp_id'] = '1340277906161_1340277906160'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Special design',
                                'Measurement range',
                                'Supply voltage',
                                'Type',
                                'Type of connection',
                                'Thread size',
                                'Type of connection 2',
                                'Thread size 2',
                                'Type of connection 3',
                                'Thread size 3',
                                'Type of connection 4',
                                'Thread size 4',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class ContrastScanner(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'contrast_scanners'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/spezialsensoren/kontrasttaster/'
        self.payload['grp_id'] = 'A1-1-8-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Operating range',
                                'Light source',
                                'Light spot orientation',
                                'Type of light-spot geometry',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Switching element 2',
                                'Switching principle 2',
                                'Type',
                                'Type 2',
                                'Switching frequency',
                                'Type 3',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class LuminescenceSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'luminescence_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/spezialsensoren/lumineszenztaster/'
        self.payload['grp_id'] = 'A1-1-8-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Application',
                                'Operating range, white paper: 50 x 50 mm',
                                'Light source',
                                'Supply voltage',
                                'Switching element',
                                'Switching element 2',
                                'Switching frequency',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class ColorSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'color_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/spezialsensoren/farbsensoren/'
        self.payload['grp_id'] = 'A1-1-8-3'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Application',
                                'Operating range',
                                'Light source',
                                'Light spot orientation',
                                'Type of light-spot geometry',
                                'Supply voltage',
                                'Switching element',
                                'Switching element 2',
                                'Switching element 3',
                                'Switching frequency',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class DoubleSheetSensor(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'double_sheet_sensors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/spezialsensoren/doppelbogen_klebestellenkontrollen/'
        self.payload['grp_id'] = 'A1-1-8-4'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Principle of physics',
                                'Operating range',
                                'Special design',
                                'Application',
                                'Operating range',
                                'Supply voltage',
                                'Switching element',
                                'Switching principle',
                                'Function',
                                'Switching element 2',
                                'Switching principle 2',
                                'Function 2',
                                'Switching element 3',
                                'Switching element 4',
                                'Switching frequency',
                                'Type of connection',
                                'Thread size',
                                'Mouth width',
                                'Mouth depth',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Dimension (Ø x L)',
                                'Degree of protection']


class EdgeDetector(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'edge_detectors'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/schaltende_sensoren/spezialsensoren/kantendetektion_im_schuppenstrom/'
        self.payload['grp_id'] = 'A1-1-8-5'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Light source',
                                'Measurement range',
                                'Supply voltage',
                                'Type of connection',
                                'Thread size',
                                'Housing material',
                                'Dimension (W x H x L)',
                                'Degree of protection']