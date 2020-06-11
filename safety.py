from params_ import *


class SafetyLightCurtains(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_light_curtains'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/optoelektronische_sicherheits_sensoren/sicherheits_lichtvorhaenge/'
        self.payload['grp_id'] = 'A1-3-1-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Device type',
                                'Application',
                                'Functions',
                                'Type',
                                'SIL',
                                'Category',
                                'Resolution',
                                'Protective field height',
                                'Supply voltage',
                                'Number of safety-related switching outputs (OSSDs)',
                                'Type 2',
                                'Switching element',
                                'Switching element 2',
                                'Dimension (Ø x L)',
                                'Degree of protection']


class SafetyLightCurtainsMultiple(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_light_curtains_multiple'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/optoelektronische_sicherheits_sensoren/mehrstrahl_sicherheits_lichtschranken/'
        self.payload['grp_id'] = 'A1-3-1-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Device type',
                                'Functions',
                                'Type',
                                'SIL',
                                'Category',
                                'Operating range',
                                'Number of beams',
                                'Beam spacing',
                                'Supply voltage',
                                'Number of safety-related switching outputs (OSSDs)',
                                'Type 2',
                                'Switching element',
                                'Switching element 2',
                                'Dimension (Ø x L)',
                                'Degree of protection']


class SingleBeamSafety(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'single_beam_safety'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/optoelektronische_sicherheits_sensoren/einstrahl_sicherheits_lichtschranken/'
        self.payload['grp_id'] = 'A1-3-1-3'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Functions',
                                'Type',
                                'SIL',
                                'Category',
                                'Operating range',
                                'Supply voltage',
                                'Number of safety-related switching outputs (OSSDs)',
                                'Type 2',
                                'Switching element',
                                'Switching element 2',
                                'Design',
                                'Thread size',
                                'Dimension (Ø x L)',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class SafetyLaserScanner(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_laser_scanner'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/optoelektronische_sicherheits_sensoren/sicherheits_laserscanner/'
        self.payload['grp_id'] = 'A1-3-1-4'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Functions',
                                'Type',
                                'SIL',
                                'Category',
                                'Operating range',
                                'Number of field pairs',
                                'Supply voltage',
                                'Number of safety-related switching outputs (OSSDs)',
                                'Type 2',
                                'Switching element',
                                'Switching element 2',
                                'Switching element 3',
                                'Switching element 4',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class SafetySensorsSet(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_sensors_set'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/optoelektronische_sicherheits_sensoren/sicherheits_lichtschranken_sets/'
        self.payload['grp_id'] = 'A1-3-1-5'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Special design',
                                'Functions',
                                'Type',
                                'SIL',
                                'Category',
                                'Operating range',
                                'Number of beams',
                                'Beam spacing',
                                'Type of muting sensors',
                                'Number of muting sensors']


class SafetySwitches(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_switches'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/sichere_zuhaltungen_schalter_und_naeherungssensoren/sicherheits_schalter/'
        self.payload['grp_id'] = 'A1-3-2-1'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Usage category at DC 13',
                                'Usage category at AC 15',
                                'Contact allocation',
                                'Design',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class SafetyLockingDevices(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_locking_devices'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/sichere_zuhaltungen_schalter_und_naeherungssensoren/sicherheits_zuhaltungen/'
        self.payload['grp_id'] = 'A1-3-2-2'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Usage category at DC 13',
                                'Usage category at AC 15',
                                'Contact allocation',
                                'Design',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class SafetyCommandDevices(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_command_devices'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/sichere_zuhaltungen_schalter_und_naeherungssensoren/sicherheits_befehlsgeraete/'
        self.payload['grp_id'] = 'A1-3-2-3'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Functions',
                                'Usage category at DC 13',
                                'Usage category at AC 15',
                                'Contact allocation',
                                'Switch type',
                                'Switching principle',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class MagneticallyCodedSensors(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_command_devices'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/sichere_zuhaltungen_schalter_und_naeherungssensoren/magnetcodierte_sensoren/'
        self.payload['grp_id'] = 'A1-3-2-4'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Functions',
                                'Usage category at DC 13',
                                'Usage category at AC 15',
                                'Contact allocation',
                                'Contact type',
                                'Switch type',
                                'Switching principle',
                                'Design',
                                'Thread size',
                                'Dimension',
                                'Dimension (W x H x L)',
                                'Degree of protection']


class SafetyTransponders(Product):
    def __init__(self):
        Product.__init__(self)
        self.file_name = 'safety_transponders'
        self.product_url = 'http://www.leuze.de/en/deutschland/produkte/produkte_fuer_die_arbeitssicherheit/sichere_zuhaltungen_schalter_und_naeherungssensoren/sicherheits_transponder_2/'
        self.payload['grp_id'] = '1358347057387'
        self.characteristics = ['Model',
                                'Article',
                                'Series',
                                'Application',
                                'Code type',
                                'SIL',
                                'Category',
                                'Supply voltage',
                                'Number of digital switching inputs',
                                'Number of safety-related switching outputs (OSSDs)',
                                'Number of digital switching outputs',
                                'Switching element',
                                'Switching element 2',
                                'Dimension (W x H x L)',
                                'Degree of protection']