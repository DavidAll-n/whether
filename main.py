from time import sleep
from repositories.rabbit_mq_repository import RabbitMQRepository
from services.message_queue_service import MessageQueueService
from services.ground_temperature_service import GroundTemperatureService
from services.htp_service import HTPService
from services.config_service import ConfigService

def main():
    configService = ConfigService()
    configService.loadConfig()
    repo = RabbitMQRepository(
        configService.RabbitMq['host'],
        configService.RabbitMq['port'],
        configService.RabbitMq['user'],
        configService.RabbitMq['password'],
        'test')
    messageService = MessageQueueService(repo)
    groundTempService = GroundTemperatureService(messageService)
    htpService = HTPService(messageService)

    while True:
        groundTempService.poll()
        sleep(10)
        htpService.poll()
        sleep(10)

main()