```python
from odoo import models, fields

class MediaContent(models.Model):
    _name = 'custom_pc_odoo_17_v2.media_content'
    _description = 'Media Content for Products'

    name = fields.Char('Media Content Name', required=True)
    product_id = fields.Many2one('custom_pc_odoo_17_v2.product', 'Related Product')
    media_type = fields.Selection([
        ('image', 'Image'),
        ('video', 'Video'),
        ('360_view', '360 Degree View'),
    ], 'Media Type', required=True)
    media_file = fields.Binary('Media File', required=True)

    def loadMediaContent(self, product_id):
        media_content = self.search([('product_id', '=', product_id)])
        media_content_list = []
        for content in media_content:
            media_content_list.append({
                'name': content.name,
                'media_type': content.media_type,
                'media_file': content.media_file
            })
        return media_content_list
```