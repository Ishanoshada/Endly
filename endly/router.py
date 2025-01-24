# endly/router.py
import re
from collections import defaultdict
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class Router:
    def __init__(self):
        self.routes = defaultdict(dict)  # Store routes in a trie-like structure

    def add_route(self, path, handler):
        """
        Add a route to the router.

        :param path: The route path.
        :param handler: The handler function for the route.
        """
        logger.info(f"Registering route: {path} -> {handler.__name__}")
        # Convert dynamic route paths (e.g., '/user/<name>') to a regex pattern
        pattern = re.sub(r"<([^>]+)>", r"(?P<\1>[^/]+)", path)  # Named capture group
        compiled_pattern = re.compile(f"^{pattern}$")
        self.routes[path] = {
            "handler": handler,
            "pattern": compiled_pattern,
        }

    def scan_class(self, cls, base_path=""):
        """
        Scan a class for routes and register them.

        :param cls: The class to scan.
        :param base_path: The base path for all routes in the class.
        """
        for method_name in dir(cls):
            method = getattr(cls, method_name)
            if callable(method) and hasattr(method, "route_path"):
                full_path = f"{base_path}{method.route_path}"
                self.add_route(full_path, method)

    def handle_request(self, request):
        """
        Handle an incoming request.

        :param request: The HTTP request object.
        """
        path = request.path
        logger.info(f"Handling request: {path}")

        # Check if the path matches any registered route
        for route_path, route_info in self.routes.items():
            match = route_info["pattern"].match(path)
            if match:
                handler = route_info["handler"]
                try:
                    # Call the handler and get the response
                    response = handler()

                    # Determine the Content-Type based on the response type
                    if isinstance(response, dict):
                        content_type = "application/json"
                        response_data = json.dumps(response).encode()
                    elif isinstance(response, str):
                        content_type = "text/plain"
                        response_data = response.encode()
                    elif isinstance(response, bytes):
                        content_type = "application/octet-stream"
                        response_data = response
                    else:
                        content_type = "text/plain"
                        response_data = str(response).encode()

                    # Send the response
                    request.send_response(200)
                    request.send_header("Content-type", content_type)
                    request.end_headers()
                    request.wfile.write(response_data)

                except Exception as e:
                    # Log the error and return a 500 Internal Server Error
                    logger.error(f"Error processing request: {e}")
                    request.send_response(500)
                    request.send_header("Content-type", "text/plain")
                    request.end_headers()
                    request.wfile.write(b"500 Internal Server Error")
                return

        # If no route matches, return a 404 error
        logger.warning(f"Route not found: {path}")
        request.send_response(404)
        request.send_header("Content-type", "text/plain")
        request.end_headers()
        request.wfile.write(b"404 Not Found")

    def reset(self):
        """Reset the router by clearing all registered routes."""
        self.routes = defaultdict(dict)