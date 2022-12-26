import json

class ConfigService:
    def __init__(self):
        self.RabbitMq = None

    def loadConfig(self):
        configFile = open('settings.json')
        configData = json.load(configFile)
        self.RabbitMq = configData['rabbitmq']
