import logging,os

msg = os.getenv('test_env')

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

logger.info(msg)
