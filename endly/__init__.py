# endly/__init__.py
"""
Endly - A lightweight Python web framework for building fast and scalable backend applications.
This module serves as the main entry point for the Endly framework, providing core functionality
for building web applications. It exposes the main components needed to create and run a web server.
Key Components:
    - App: The main application class for creating web servers
    - route: A decorator for registering route handlers
Example:
    app = App(__name__, host="0.0.0.0", port=8080)
    @app.group('/api')
    class UserRoutes:
        @route('/home')
        def home():
            return "Hello, World!"
    app.run()
Dependencies:
    - Standard library only (no external dependencies)
For more information, visit:
    https://github.com/ishanoshada/endly
"""
from .app import App
from .decorators import route
from endly import App, route

__author__ = "Ishan Oshada"
__email__ = "ishan.kodithuwakku.offical@gmail.com"
__version__ = "0.1.1"
__license__ = "MIT"

