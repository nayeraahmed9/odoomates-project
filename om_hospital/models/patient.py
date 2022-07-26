from odoo import api, fields, models
from datetime import date
class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit=['mail.thread', 'mail.activity.mixin']
    _description="Hospital Patient"

    name= fields.Char(string='Name', required=False,tracking=True)
    ref= fields.Char(string='Reference')
    date_of_birth= fields.Date(string="Birth Of Date")
    age= fields.Integer(string='Age',compute="_compute_age",tracking=True)
    gender= fields.Selection(string='Gender',selection=[('male', 'Male'),('female', 'Female'), ],required=False,tracking=True)
    active= fields.Boolean(string="Active" ,default=True )
    appointment_id= fields.Many2one(comodel_name='hospital.appointment',string='Appointments',required=False)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            print("self.............",self)
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age=0
