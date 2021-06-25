from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class MyPetPlus(models.Model):
    _name = "my.pet"
    _inherit = "my.pet"
    _description = "Extend mypet model"

    toy = fields.Char('Pet Toy', required=False)

    age = fields.Integer('Age', required=2)
    gender = fields.Selection(selection_add=[('sterilization', 'Sterilization')])
