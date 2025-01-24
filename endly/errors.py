# endly/errors.py
class ErrorHandler:
    @staticmethod
    def handle_404(request):
        """
        Handle 404 Not Found errors.

        :param request: The HTTP request object.
        """
        request.send_response(404)
        request.send_header("Content-type", "text/plain")
        request.end_headers()
        request.wfile.write(b"404 Not Found")

    @staticmethod
    def handle_500(request):
        """
        Handle 500 Internal Server Errors.

        :param request: The HTTP request object.
        """
        request.send_response(500)
        request.send_header("Content-type", "text/plain")
        request.end_headers()
        request.wfile.write(b"500 Internal Server Error")