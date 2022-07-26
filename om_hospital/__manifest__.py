{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'odoo-mates',
    'sequence': -100,
    'summary': 'hospital management system',
    'description': """This module contains all the common features of hospital management system.""",
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
    ],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}