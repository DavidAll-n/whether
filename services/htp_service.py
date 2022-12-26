from datetime import datetime
import json
import random

class HTPService:
    def __init__(self, messageQueueService):
        self.messageQueueService = messageQueueService
    
    def poll(self):
        # Get data from sensor...
        data = {
            'humidity': { 'value': round(random.uniform(0.0, 100.0), 2), 'unit': '%', 'readDateTime': datetime.now().strftime('%Y%m%d %H:%M:%S.000') },
            'pressure': { 'value': round(random.uniform(900.0, 5000.0), 2), 'unit': 'pa', 'readDateTime': datetime.now().strftime('%Y%m%d %H:%M:%S.000') },
            'temperature': { 'value': round(random.uniform(20.0, 100.0), 2), 'unit': 'f', 'readDateTime': datetime.now().strftime('%Y%m%d %H:%M:%S.000') },
        }
        dataJson = json.dumps(data)
        print('Read value from HTP sensor: ' + dataJson)
        self.messageQueueService.publish(data, 'test')