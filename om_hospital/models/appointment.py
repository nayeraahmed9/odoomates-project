from odoo import api, fields, models

class HospitalAppointment(models.Model):
    _name="hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description= "Hospital Appointment"
    _rec_name='ref'

    patient_id= fields.Many2one("hospital.patient", string="Patient")
    appointment_time= fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    gender = fields.Selection(related='patient_id.gender',readonly=False)
    booking_date= fields.Date(string="Booking Date",default=fields.Date.context_today)
    ref = fields.Char(string='Reference')
    prescription=fields.Html(string='Prescription')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Low'),
        ('2', 'High'),
        ('3', 'Very High')], string="Priority")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancelld', 'Cancelled')],default="draft", string="State",required=True,statusbar_visible="draft,in_consultation,done")
    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref