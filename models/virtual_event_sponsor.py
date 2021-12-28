# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualEventSponsor(models.Model):
    _name = 'virtual.event.sponsor'
    _description = 'Virtual Event Sponsor'

    name = fields.Char(string="Company")
    type = fields.Char(string="Type")
    description = fields.Char(string="Description")
    virtual_event_id = fields.Many2one('virtual.event', string="Event")
