# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Room(models.Model):
    _name = 'connecteur_seguinus.room'
    name=fields.Char(string="chambre",required=True)
    petits_lits=fields.Integer()
    grands_lits=fields.Integer()
    description=fields.Text()

class Booking(models.Model):
    _name='connecteur_seguinus.booking'
    name=fields.Char(string="booking",required=True)
    dateDebut=fields.Date()
    dateFin = fields.Date()
    room_ids=fields.Many2many('connecteur_seguinus.room',string="chambres")
    
# class connecteur_seguinus(models.Model):
#     _name = 'connecteur_seguinus.connecteur_seguinus'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100