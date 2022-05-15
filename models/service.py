from odoo import models, fields, api

class Service(models.Model):
    _name = "hotel1.service"
    name = fields.Char("Name Service")
    service_type = fields.Many2one("hotel1.service_type")
    price = fields.Monetary("Price", 'currency_id')
    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)
    description = fields.Char("Description")




class ServiceType(models.Model):
    _name = "hotel1.service_type"

    name = fields.Char("Service Type Name")
    description = fields.Char("Description")





