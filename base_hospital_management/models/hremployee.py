from odoo import models, fields

class Employee(models.Model):
    _inherit = 'hr.employee'

    price = fields.Float(string='Consultation Price')
