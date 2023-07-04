from odoo import models, fields
class aparcamiento(models.Model):
    _name = 'aparcamiento.aparcamiento'
    _description = 'aparcamiento'

    name = fields.Char(string='Name')
    cant_plazas = fields.Integer(string='cantidad de plazas')
    cant_vehiculo_estacionados = fields.Integer(string='vehículos estacionados')

    vehiculo_ids = fields.One2many('vehiculo.vehiculo', 'aparcamiento_id', string='Vehiculos')