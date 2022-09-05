from odoo import fields, models


class Session(models.Model):
    _name = "openacademy.session"
    _description = 'Open Academy Session'

    name = fields.Char()
    start_date = fields.Date()
    duration = fields.Float()
    seats = fields.Integer('Number of Seats')
    instructor_id = fields.Many2one('res.partner', 'Instructor')
    course_id = fields.Many2one('openacademy.course', 'Course')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')