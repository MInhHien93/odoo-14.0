from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError


class MyPet(models.Model):
    _name = "my.pet"
    _description = "My Pet Description"

    name = fields.Char('Pet Name', required=True)
    nickname = fields.Char('Nickname')
    description = fields.Text('My pet description')
    age = fields.Integer('Age', required=1)
    weight = fields.Float('Weight')
    dob = fields.Date('Dob', required=False)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string='Gender', default='male')
    pet_image = fields.Binary('Pet Image', attachment=True, help='Pet Image')
    basic_price = fields.Float('Basic Price', default=0)
    owner_id = fields.Many2one('res.partner', string='Owner')
    product_ids = fields.Many2many(comodel_name='product.product',
                                   string='Related Products',
                                   relation='pet_product_rel',
                                   column1='col_pet_id',
                                   column2='col_product_id', )
