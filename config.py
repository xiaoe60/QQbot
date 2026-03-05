import os
import logging

class Config:
    def __init__(self):
        # QQ settings
        self.qq_bot_id = os.getenv('QQ_BOT_ID')
        self.qq_token = os.getenv('QQ_TOKEN')

        # go-cqhttp settings
        self.cqhttp_url = os.getenv('CQHTTP_URL')
        self.cqhttp_port = int(os.getenv('CQHTTP_PORT', 5700))

        # Deepseek settings
        self.deepseek_api_key = os.getenv('DEEPEEK_API_KEY')

        # Qwen API settings
        self.qwen_api_key = os.getenv('QWEN_API_KEY')

        # Logging setup
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler("app.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def log_config(self):
        self.logger.info("Config loaded with the following settings:")
        self.logger.info(f"QQ Bot ID: {self.qq_bot_id}")
        self.logger.info(f"CQHTTP URL: {self.cqhttp_url}")
        self.logger.info(f"Deepseek API Key: {self.deepseek_api_key}")
        self.logger.info(f"Qwen API Key: {self.qwen_api_key}")

