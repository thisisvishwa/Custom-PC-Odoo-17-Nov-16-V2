```python
from odoo import models, fields

class ProductPages(models.Model):
    _name = 'product.pages'
    _description = 'Product Pages'

    product_id = fields.Many2one('product.product', string='Product')
    product_image = fields.Binary('Product Image')
    product_name = fields.Char('Product Name')
    product_description = fields.Text('Product Description')
    product_specs = fields.Text('Product Specifications')
    related_products = fields.Many2many('product.product', string='Related Products')
    reviews = fields.One2many('product.reviews', 'product_id', string='Reviews')

    def loadProductPage(self, product_id):
        product = self.env['product.product'].browse(product_id)
        self.product_id = product.id
        self.product_image = product.image
        self.product_name = product.name
        self.product_description = product.description_sale
        self.product_specs = product.attribute_line_ids.mapped('value_ids').mapped('name')
        self.related_products = product.related_products
        self.reviews = self.env['product.reviews'].search([('product_id', '=', product.id)])

class ProductReviews(models.Model):
    _name = 'product.reviews'
    _description = 'Product Reviews'

    product_id = fields.Many2one('product.product', string='Product')
    user_id = fields.Many2one('res.users', string='User')
    rating = fields.Selection([(str(num), num) for num in range(1, 6)], 'Rating')
    review = fields.Text('Review')

    def postReview(self, product_id, user_id, rating, review):
        self.create({
            'product_id': product_id,
            'user_id': user_id,
            'rating': rating,
            'review': review
        })
```