from odoo import models, fields,api

class vehiculo(models.Model):
    _name = 'vehiculo.vehiculo'
    _description = 'vehiculo'
    _order = 'modelo'

    name = fields.Char(string='Matricula')
    modelo = fields.Char('Modelo')

    construido = fields.Date('Fecha de construccion')
    descripcion = fields.Text('Descripcion')
    horaEntrada = fields.Datetime('Hora de Entrada')
    horaSalida = fields.Datetime('Hora de Entrada')
    consumo = fields.Float(string='Consumo (litros)')

    estadoTecnico = fields.Text(string='estado técnico')
    añosUso = fields.Integer(string='Años de uso')
    aparcamientoAsignada = fields.Selection([
        ('si', 'SI') ,('no', 'NO')
    ], string='aparcamientoAsignada')
    mantenimientoRealizados = fields.Selection([
        ('si', 'SI'),('no', 'NO')
    ], string='mantenimientoRealizados')

    aparcamiento_id = fields.Many2one("aparcamiento.aparcamiento", string='aparcamiento')
    mantenimientos_ids = fields.Many2many('mantenimientos.mantenimientos', string='Mantenimientos')
 

    total = fields.Integer(string='Total Checked', compute='checked', help='Total of checked')
    
    
    def action_test(self):
      var1 = self.env['mantenimientos.mantenimientos'].search([])
      var2 = self.env['mantenimientos.mantenimientos'].search_count([])
      var3 = self.env['mantenimientos.mantenimientos'].search_count([('tipo','=','mecanica'),('tipo','=','pintura'),('tipo','=','lavado')])
      print(var1, var2, var3)
    
    
    def checked(self):
      count = 0
      for record in self.mantenimientos_ids:
        if record.tipo:
          count = count + 1
      self.total = count


    