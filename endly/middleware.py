# endly/middleware.py
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class Middleware:
    def __init__(self, app):
        self.app = app

    def pre_process(self, request):
        """Pre-process the request."""
        logger.info(f"Pre-processing request: {request.path}")

    def post_process(self, request, response):
        """Post-process the response."""
        logger.info(f"Post-processing response: {response}")