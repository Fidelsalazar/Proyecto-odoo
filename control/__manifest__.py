{
    'name': 'Control de Vehiculos',
    'version': '11.0',
    'description': 'Sistema de gestión para el Control del Vehiculo',
    'summary': '',
    'author': 'Daniela de Concepcion y Fidel Alejandro',
    'website': '',
    'license': '',
    'category': 'Adminstration',
    'auto_install': False,
    'application': True,
   'depends': [
    'base',
  ],
  'data': [
    'views/menu.xml',
    'views/aparcamiento.xml',
    'views/vehiculo.xml',
    'views/mantenimientos.xml',
    'security/access.xml',
  ],
  'installable': True,
}