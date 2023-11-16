```python
class DeveloperDocumentation:
    def __init__(self):
        self.documentation = {
            "codebase": "The codebase is structured into multiple files each handling a specific functionality of the application. Refer to the respective python files for detailed code.",
            "APIs": "The application uses various APIs for payment gateways, shipping services, and CRM integration. Refer to payment_gateways.py, shipping_services.py, and crm_integration.py for the implementation.",
            "moduleArchitecture": "The application is modular with each module handling a specific functionality. The modules interact with each other to provide a seamless user experience."
        }

    def get_documentation(self, topic):
        return self.documentation.get(topic, "Topic not found in documentation")

developerDocumentation = DeveloperDocumentation()

# Get documentation on codebase
print(developerDocumentation.get_documentation("codebase"))

# Get documentation on APIs
print(developerDocumentation.get_documentation("APIs"))

# Get documentation on module architecture
print(developerDocumentation.get_documentation("moduleArchitecture"))
```