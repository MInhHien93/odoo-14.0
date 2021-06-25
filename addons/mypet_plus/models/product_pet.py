from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class ProductPet(models.Model):
    _name = 'product.pet'
    _inherits = {'my.pet': 'my_pet_id'}
    _description = 'Product Pet'

    my_pet_id = fields.Many2one(
        'my.pet', 'My Pet',
        auto_join=True, index=True, ondelete='cascade', required=True)

    pet_type = fields.Selection([
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('vip', 'VIP'),
        ('cute', 'Cute'),
    ], string='Type', default='basic')

    pet_color = fields.Selection([
        ('black', 'Back'),
        ('white', 'White'),
        ('yellow', 'Yellow'),
        ('pink', 'Pink'),
    ], string='Color', default='black')

    bonus_price = fields.Float('Bonus Price', default=0)
    final_price = fields.Float('Final Price', compute='_compute_field_value')

    def _compute_field_value(self):
        for record in self:
            record.final_price = record.basic_price + record.bonus_price


