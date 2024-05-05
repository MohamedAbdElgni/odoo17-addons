from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient _model'

    name = fields.Char(compute='_compute_name', readonly=True, default='New Patient')
    first_name = fields.Char(required=1)
    last_name = fields.Char(required=1)
    birth_date = fields.Date(required=1)
    history = fields.Html()
    cr_ratio = fields.Float(required=1)
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')], required=1)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')], required=1)
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text(required=1)
    age = fields.Integer(compute="_compute_age", readonly=True)
    department_id = fields.Many2one('hms.department', default=1)
    department_capacity = fields.Integer(related="department_id.capacity")

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for rec in self:
            rec.name = f'{rec.first_name} {rec.last_name}'.title()

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = relativedelta(fields.Date.today(), rec.birth_date).years
            else:
                rec.age = 0
