# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualEventStall(models.Model):
    _name = 'virtual.event.stall'
    _description = 'Virtual Event Stall'

    name = fields.Char(string="Company")
    document = fields.Binary(string="Document")
    gallery = fields.Binary(string="Gallery")
    virtual_event_id = fields.Many2one('virtual.event', string="Event")

