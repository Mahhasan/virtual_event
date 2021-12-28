# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualEvent(models.Model):
    _name = 'virtual.event'
    _description = 'Virtual Event'

    name = fields.Char(string="Name")
    company = fields.Char(string="Company")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    event_url = fields.Char(string="Event URL")

    virtual_event_stall_ids = fields.One2many('virtual.event.stall','virtual_event_id', string="Stall")
    virtual_event_sponsor_ids = fields.One2many('virtual.event.sponsor','virtual_event_id', string="Sponsor")
    virtual_event_webinar_ids = fields.One2many('virtual.event.webinar','virtual_event_id', string="Webinar")
