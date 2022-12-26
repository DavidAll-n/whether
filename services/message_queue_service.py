
class MessageQueueService:
    def __init__(self, messageQueueRepo):
        self.messageQueueRepo = messageQueueRepo
        self.messageQueueRepo.openConnection()
    
    def publish(self, data, routingKey):
        self.messageQueueRepo.publish(data, routingKey)