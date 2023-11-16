```python
from odoo import models, fields

class ReviewSchema(models.Model):
    _name = 'review.schema'
    _description = 'Review Schema'

    product_id = fields.Many2one('product.schema', string='Product')
    user_id = fields.Many2one('user.schema', string='User')
    rating = fields.Integer(string='Rating')
    review = fields.Text(string='Review')

class Review(models.Model):
    _name = 'review'
    _description = 'Product Review'

    review_data = fields.Many2one('review.schema', string='Review Data')

    def postReview(self, product_id, user_id, rating, review):
        review_data = self.env['review.schema'].create({
            'product_id': product_id,
            'user_id': user_id,
            'rating': rating,
            'review': review
        })
        self.write({'review_data': review_data.id})

    def getReviews(self, product_id):
        reviews = self.env['review.schema'].search([('product_id', '=', product_id)])
        return reviews
```