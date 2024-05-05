{
    'name': "HMS",
    'author': "Mohamed Abd-ElGani",
    'category': 'Management',
    'description': """Hospital Management System""",
    'version': '17.0.0.1.0',
    'depends': ['base',
                ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient.xml'
    ],

}
