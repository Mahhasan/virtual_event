# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualWebinarSchedule(models.Model):
    _name = 'virtual.webinar.schedule'
    _description = 'Virtual Webinar Schedule'

    name = fields.Char(string="Speaker")
    topic = fields.Char(string="Topic")
    time = fields.Char(string="time")
    virtual_webinar_id = fields.Many2one('virtual.event.webinar', string="Webinar")
