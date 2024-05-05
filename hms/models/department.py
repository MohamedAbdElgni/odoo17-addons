from odoo import fields, models, api


class Department(models.Model):
    _name = 'hms.department'
    _description = 'Hospital Department'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean(default=1)
    patient_id = fields.Many2many('hms.patient')
