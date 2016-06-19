# -*- coding: utf-8 -*-
from openerp import http

# class ConnecteurSeguinus(http.Controller):
#     @http.route('/connecteur_seguinus/connecteur_seguinus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/connecteur_seguinus/connecteur_seguinus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('connecteur_seguinus.listing', {
#             'root': '/connecteur_seguinus/connecteur_seguinus',
#             'objects': http.request.env['connecteur_seguinus.connecteur_seguinus'].search([]),
#         })

#     @http.route('/connecteur_seguinus/connecteur_seguinus/objects/<model("connecteur_seguinus.connecteur_seguinus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('connecteur_seguinus.object', {
#             'object': obj
#         })