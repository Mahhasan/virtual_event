# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualWebinarGuest(models.Model):
    _name = 'virtual.webinar.guest'
    _description = 'Virtual Webinar Guest'

    name = fields.Char(string="Name")
    organisation = fields.Char(string="Organisation")
    email = fields.Char(string="email")
    virtual_webinar_id = fields.Many2one('virtual.event.webinar', string="Webinar")
