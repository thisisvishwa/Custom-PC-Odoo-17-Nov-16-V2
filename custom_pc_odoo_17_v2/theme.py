```python
from odoo import models, fields

class Theme(models.Model):
    _name = 'custom_pc_odoo_17_v2.theme'
    _description = 'Theme for the Custom PC Building Module'

    name = fields.Char(string='Theme Name', required=True)
    color_primary = fields.Char(string='Primary Color', default='#000000')  # Black
    color_secondary = fields.Char(string='Secondary Color', default='#FF0000')  # Red
    color_tertiary = fields.Char(string='Tertiary Color', default='#808080')  # Gray

    def applyTheme(self):
        """
        Function to apply the selected theme to the website.
        """
        # This is a placeholder function. In a real-world application, this function would contain
        # the logic to apply the selected theme (colors, fonts, etc.) to the website.
        pass

    def themeUpdateMessage(self):
        """
        Function to send a message to the user when the theme is updated.
        """
        # This is a placeholder function. In a real-world application, this function would contain
        # the logic to send a message to the user when the theme is updated.
        pass
```