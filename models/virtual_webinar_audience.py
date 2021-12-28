# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VirtualWebinarAudience(models.Model):
    _name = 'virtual.webinar.audience'
    _description = 'Virtual Webinar Audience'

    name = fields.Char(string="Name")
    organisation = fields.Char(string="Organisation")
    email = fields.Char(string="email")
    virtual_webinar_id = fields.Many2one('virtual.event.webinar', string="Webinar")
