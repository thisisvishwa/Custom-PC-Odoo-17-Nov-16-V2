```python
from .components import productComponents
from .pricing import updatePrice

class PCBuilder:
    def __init__(self):
        self.selected_components = {}
        self.total_price = 0

    def add_component(self, category, component):
        if category in productComponents and component in productComponents[category]:
            self.selected_components[category] = component
            self.total_price = updatePrice(self.selected_components)
            return True
        return False

    def remove_component(self, category):
        if category in self.selected_components:
            del self.selected_components[category]
            self.total_price = updatePrice(self.selected_components)
            return True
        return False

    def get_selected_components(self):
        return self.selected_components

    def get_total_price(self):
        return self.total_price

pcBuilder = PCBuilder()

def buildPC(category, component):
    if pcBuilder.add_component(category, component):
        return {
            'message': 'Component added successfully',
            'selected_components': pcBuilder.get_selected_components(),
            'total_price': pcBuilder.get_total_price()
        }
    else:
        return {
            'message': 'Failed to add component',
            'selected_components': pcBuilder.get_selected_components(),
            'total_price': pcBuilder.get_total_price()
        }
```