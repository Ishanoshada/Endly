# endly/app.py
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import os
import json
import logging
from .router import Router
from .middleware import Middleware
from .static import StaticFileHandler
from .errors import ErrorHandler

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

class App:
    def __init__(self, name, host="localhost", port=8000, static_dir="static"):
        """
        Initialize the App.

        :param name: Name of the application.
        :param host: Host address to bind the server (default: "localhost").
        :param port: Port to bind the server (default: 8000).
        :param static_dir: Directory to serve static files from (default: "static").
        """
        self.name = name
        self.host = host
        self.port = port
        self.static_dir = static_dir
        self.router = Router()
        self.middleware = Middleware(self)
        self.static_handler = StaticFileHandler(static_dir)
        self.error_handler = ErrorHandler()

    def group(self, base_path):
        """
        Decorator to register a class with routes under a common base path.

        :param base_path: Base path for all routes in the class.
        """
        def decorator(cls):
            logger.info(f"Scanning class: {cls.__name__}")
            self.router.scan_class(cls, base_path)
            return cls
        return decorator

    def run(self):
        """
        Start the server and handle requests.
        """
        class RequestHandler(BaseHTTPRequestHandler):
            router = self.router
            middleware = self.middleware
            static_handler = self.static_handler
            error_handler = self.error_handler

            def do_GET(self):
                """
                Handle GET requests.
                """
                try:
                    self.middleware.pre_process(self)
                    if self.path.startswith("/static/"):
                        self.static_handler.serve_static(self)
                    else:
                        self.router.handle_request(self)
                    self.middleware.post_process(self, "Response")
                except Exception as e:
                    logger.error(f"Error processing request: {e}")
                    self.error_handler.handle_500(self)

            def do_POST(self):
                """
                Handle POST requests.
                """
                try:
                    self.middleware.pre_process(self)
                    self.router.handle_request(self)
                    self.middleware.post_process(self, "Response")
                except Exception as e:
                    logger.error(f"Error processing request: {e}")
                    self.error_handler.handle_500(self)

        # Create the server
        server = ThreadedHTTPServer((self.host, self.port), RequestHandler)
        server.allow_reuse_address = True  # Allow reuse of the port
        logger.info(f"Server running on http://{self.host}:{self.port}")

        try:
            # Start the server
            server.serve_forever()
        except KeyboardInterrupt:
            logger.info("\nServer is shutting down...")
        finally:
            # Clean up
            server.server_close()
            self.router.reset()
            logger.info("Server closed.")