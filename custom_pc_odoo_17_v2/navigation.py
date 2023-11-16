```python
from odoo import models, fields

class NavigationMenu(models.Model):
    _name = 'custom_pc.navigation'
    _description = 'Navigation Menu'

    name = fields.Char(string='Menu Name', required=True)
    parent_id = fields.Many2one('custom_pc.navigation', string='Parent Menu')
    child_ids = fields.One2many('custom_pc.navigation', 'parent_id', string='Submenus')
    sequence = fields.Integer(string='Sequence')
    url = fields.Char(string='URL')

    def navigate(self):
        # This function will be used to navigate through the website
        pass

class UserAccount(models.Model):
    _name = 'custom_pc.user_account'
    _description = 'User Account Access'

    user_id = fields.Many2one('res.users', string='User')
    access_level = fields.Selection([
        ('user', 'User'),
        ('admin', 'Admin'),
    ], string='Access Level', default='user')

    def access_account(self):
        # This function will be used to access user account
        pass
```