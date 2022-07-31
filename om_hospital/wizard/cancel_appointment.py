# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    appointment_id = fields.Many2one('hospital.appointment',string="Appointments")
    reason = fields.Text(string="Reason")

    def action_cancel(self):
        return