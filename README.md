# Endly

Endly is a lightweight Python web framework for building fast and scalable backend applications. It provides a simple and intuitive API for defining routes, handling requests, and serving static files.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Basic Example](#basic-example)
    - [Serving Static Files](#serving-static-files)
    - [Middleware](#middleware)
    - [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)
- [Project Structure](#project-structure)
- [Future Updates](#future-updates)

## Features

- **Routing**: Define routes with dynamic parameters.
- **Static File Serving**: Serve static files from a specified directory.
- **Middleware**: Add pre-processing and post-processing middleware.
- **JSON Support**: Automatically serialize Python dictionaries to JSON responses.
- **Error Handling**: Custom error handlers for 404 and 500 errors.
- **Concurrency**: Handle multiple requests concurrently using threading.
- **Logging**: Built-in logging for debugging and monitoring.

## Installation

You can install Endly using pip:

```bash
pip install endly
```

For development installation:

```bash
# Clone the repository
git clone https://github.com/yourusername/endly.git
cd endly

# Install in development mode
pip install -e .
```

To verify installation:
```python
import endly
```

## Usage

### Basic Example

```python
from endly import App, route

# Create the app
app = App(__name__, host="0.0.0.0", port=8080)

# Define routes
@app.group('/api')
class UserRoutes:
        @route('/home')
        def home():
                return "Hello, World!"

        @route('/user/<name>')
        def user(name):
                return {"message": f"Hello, {name}!"}

# Run the server
app.run()
```

### Serving Static Files

1. Create a `static` directory and add an `index.html` file:
     ```html
     <!-- static/index.html -->
     <!DOCTYPE html>
     <html>
     <head>
             <title>Static File</title>
     </head>
     <body>
             <h1>Hello from a static file!</h1>
     </body>
     </html>
     ```

2. Update `main.py` to serve static files:
     ```python
     from endly import App, route

     # Create the app with static file support
     app = App(__name__, host="0.0.0.0", port=8080, static_dir="static")

     # Define routes
     @app.group('/api')
     class UserRoutes:
             @route('/home')
             def home():
                     return "Welcome to the Home Page!"

     # Run the server
     app.run()
     ```

3. Visit `http://localhost:8080/static/index.html` to view the static file.

### Middleware

Add middleware for pre-processing and post-processing requests:

```python
from endly import App, route

# Create the app
app = App(__name__, host="0.0.0.0", port=8080)

# Define routes
@app.group('/api')
class UserRoutes:
        @route('/home')
        def home():
                return "Welcome to the Home Page!"

# Run the server
app.run()
```

Middleware logs:
```
Pre-processing request: /api/home
Post-processing response: Response
```

### Error Handling

Custom error handlers for 404 and 500 errors:

```python
from endly import App, route

# Create the app
app = App(__name__, host="0.0.0.0", port=8080)

# Define routes
@app.group('/api')
class UserRoutes:
        @route('/home')
        def home():
                return "Welcome to the Home Page!"

# Run the server
app.run()
```

Test error handling:
- Visit `http://localhost:8080/invalid` → Returns `404 Not Found`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

### **Project Structure**

Here's the recommended project structure:

```
endly/
│
├── endly/
│   ├── __init__.py
│   ├── app.py
│   ├── router.py
│   ├── middleware.py
│   ├── static.py
│   ├── errors.py
│   └── logging.py
│
├── main.py
├── README.md
├── LICENSE
```

## Future Updates

Here's what's coming in future releases:

- Authentication middleware and JWT support
- Database integration (SQLAlchemy, MongoDB)
- WebSocket support for real-time applications
- Rate limiting and request throttling
- API documentation generator
- GraphQL integration
- Docker containerization support
- Testing utilities and fixtures
- Performance optimization tools
- CLI tool for project scaffolding

