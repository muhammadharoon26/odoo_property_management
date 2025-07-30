from odoo import models, fields


class Property(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char("Title", required=True)
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    state = fields.Selection(
        [
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Real Estate Property Type"

    name = fields.Char("Name", required=True)
