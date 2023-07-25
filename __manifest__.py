{
    'name': 'doctor',
    'version': '1.0',
    'category': 'General',
    'summary': 'Módulo para processamento e gerenciamento das informações referentes ao ProDoctor',
    'author': ['Marcelo Barbosa dos Santos'],
    'depends': ['base'],
    'data': [
        'views\doctor_view.xml',
        'wizard\doctor_wizard_view.xml',
        'security/ir.model.access.csv',
        'security/doctor_security.xml',
    ],
    'installable': True,
    'application': True,
}
