from odoo import models, fields, api

class Mantenimientos(models.Model):
    _name = 'mantenimientos.mantenimientos'
    _description = 'mantenimientos'
    _order = 'fechaSolicitud'

    fechaSolicitud = fields.Date(string='Fecha de solicitud')
    costo = fields.Float(string='Costo total ')
    descripcion = fields.Text(string='Descripción')    
    tipo = fields.Selection(string='Lista de mantenimiento', selection=[('lavado', 'lavado precio: 150'), ('pintura', 'pintura precio: 345'), ('mecanica', 'mecanica precio: 890')])
   
    vehiculo_ids = fields.Many2many('vehiculo.vehiculo', string='Vehiculo')
    
    total = fields.Integer(string='Total Checked', compute='checked', help='Total of checked')
    
    def action_test(self):
        var1 = self.env['vehiculo.vehiculo'].search([])
        var2 = self.env['vehiculo.vehiculo'].search_count([])
        var3 = self.search([('tipo','=','mecanica'),('tipo','=','pintura'),('tipo','=','lavado')])
        print(var1, var2, var3)
    