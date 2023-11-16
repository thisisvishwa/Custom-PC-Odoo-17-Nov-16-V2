```python
from .components import productComponents
from .offers import applyOffer

class Pricing:
    def __init__(self):
        self.total_price = 0
        self.selected_components = []

    def add_component(self, component_id):
        component = productComponents.get(component_id)
        if component:
            self.selected_components.append(component)
            self.update_price()

    def remove_component(self, component_id):
        component = next((c for c in self.selected_components if c['id'] == component_id), None)
        if component:
            self.selected_components.remove(component)
            self.update_price()

    def update_price(self):
        self.total_price = sum(c['price'] for c in self.selected_components)
        self.total_price = applyOffer(self.selected_components, self.total_price)
        self.send_price_update()

    def send_price_update(self):
        message = {
            'type': 'priceUpdateMessage',
            'data': {
                'totalPrice': self.total_price,
                'selectedComponents': self.selected_components
            }
        }
        # Send message to frontend

pricing = Pricing()
```
This Python code defines a `Pricing` class that maintains the total price and selected components for a custom PC. The `add_component` and `remove_component` methods allow components to be added or removed, updating the total price each time. The `update_price` method calculates the total price of the selected components and applies any applicable offers. The `send_price_update` method prepares a message to be sent to the frontend with the updated price and selected components.