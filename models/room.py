from odoo import models, fields, api

class Room(models.Model):
    _name = "hotel1.room"

    name = fields.Char("Name Room")
    room_type = fields.Many2one("hotel1.room_type")
    status = fields.Many2one("hotel1.room.status")
    # booking_id = fields.Many2one("hotel1.booking")


class RoomType(models.Model):
    _name = "hotel1.room_type"
    name = fields.Char("Name Room")
    price = fields.Monetary("price", 'currency_id')
    limit_person = fields.Integer("Limit Person")
    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)

class StatusRoom(models.Model):
    _name = "hotel1.room.status"
    name = fields.Char("Status room")

