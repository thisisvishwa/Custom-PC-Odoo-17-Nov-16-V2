```python
from odoo import models, fields, api

class CustomizationTools(models.Model):
    _name = 'custom.pc.builder'
    _description = 'Custom PC Builder'

    name = fields.Char('Name')
    components = fields.Many2many('product.template', string='Components')
    compatibility = fields.Text(compute='_compute_compatibility')
    power_requirements = fields.Text(compute='_compute_power_requirements')
    estimated_performance = fields.Text(compute='_compute_estimated_performance')

    @api.depends('components')
    def _compute_compatibility(self):
        for record in self:
            # Add logic to calculate compatibility based on selected components
            record.compatibility = "Compatible"

    @api.depends('components')
    def _compute_power_requirements(self):
        for record in self:
            # Add logic to calculate power requirements based on selected components
            record.power_requirements = "500W"

    @api.depends('components')
    def _compute_estimated_performance(self):
        for record in self:
            # Add logic to calculate estimated performance based on selected components
            record.estimated_performance = "High Performance"

    def add_component(self, component):
        self.components = [(4, component.id)]

    def remove_component(self, component):
        self.components = [(3, component.id)]
```