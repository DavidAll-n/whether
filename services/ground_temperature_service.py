from datetime import datetime
import json
import random

class GroundTemperatureService:
    def __init__(self, messageQueueService):
        self.messageQueueService = messageQueueService

    def poll(self):
        # Get data from sensor...
        data = { 'value': round(random.uniform(20.0, 100.0), 2), 'unit': 'f', 'readDateTime': datetime.now().strftime('%Y%m%d %H:%M:%S.000') }
        dataJson = json.dumps(data)
        print('Read value from ground temp sensor: ' + dataJson)
        self.messageQueueService.publish(data, 'test')