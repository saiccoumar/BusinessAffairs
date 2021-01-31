import logging
import webview
import os
from contextlib import redirect_stdout
from io import StringIO
from server import server

logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # server.run(port=8000,debug=True)
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window('Business Affairs',server, min_size=(1000, 700))
        webview.start(debug=True)
