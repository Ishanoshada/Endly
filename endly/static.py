# endly/static.py
import os

class StaticFileHandler:
    def __init__(self, static_dir="static"):
        self.static_dir = static_dir

    def serve_static(self, request):
        """
        Serve static files from the specified directory.

        :param request: The HTTP request object.
        """
        path = request.path.lstrip("/")
        file_path = os.path.join(self.static_dir, path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_path, "rb") as file:
                request.send_response(200)
                request.send_header("Content-type", "text/html")
                request.end_headers()
                request.wfile.write(file.read())
        else:
            request.send_response(404)
            request.send_header("Content-type", "text/plain")
            request.end_headers()
            request.wfile.write(b"404 Not Found")