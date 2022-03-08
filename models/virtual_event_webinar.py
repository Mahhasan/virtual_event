# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualEventWebinar(models.Model):
    _name = 'virtual.event.webinar'
    _description = 'Virtual Event Webinar'

    name = fields.Char(string="Webinar Title")
    duration = fields.Char(string="Duration")
    start_time = fields.Datetime(string="Start Time")
    guest = fields.Char(string="Guest")
    virtual_event_id = fields.Many2one('virtual.event', string="Event")

    virtual_webinar_guest_ids = fields.One2many('virtual.webinar.guest', 'virtual_webinar_id', string="Guest")
    virtual_webinar_audience_ids = fields.One2many('virtual.webinar.audience', 'virtual_webinar_id', string="Audience")
    virtual_webinar_schedule_ids = fields.One2many('virtual.webinar.schedule', 'virtual_webinar_id', string="Schedule")