# -*- coding: utf-8 -*-
# from odoo import http


# class VirtualEvent(http.Controller):
#     @http.route('/virtual_event/virtual_event', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/virtual_event/virtual_event/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('virtual_event.listing', {
#             'root': '/virtual_event/virtual_event',
#             'objects': http.request.env['virtual_event.virtual_event'].search([]),
#         })

#     @http.route('/virtual_event/virtual_event/objects/<model("virtual_event.virtual_event"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('virtual_event.object', {
#             'object': obj
#         })
