import http.server
import webbrowser
import os

PORT = 5500
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

os.chdir(DIRECTORY)

handler = http.server.SimpleHTTPRequestHandler
print(f"✅ Serving portfolio at http://localhost:{PORT}")
print("Press Ctrl+C to stop the server.")

webbrowser.open(f"http://localhost:{PORT}/index.html")

with http.server.HTTPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
