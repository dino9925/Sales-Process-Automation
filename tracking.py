from flask import Flask, request, send_file
import logging
from datetime import datetime
import io

app = Flask(__name__)

logging.basicConfig(filename='email_opens.log', level=logging.INFO)

@app.route('/track_open')
def track_open():
    email = request.args.get('email', 'unknown')
    logging.info(f"Email opened: {email} at {datetime.now()}")


    pixel = b'GIF89a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF!\xF9\x04' \
            b'\x01\x00\x00\x00\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'

    return send_file(
        io.BytesIO(pixel),
        mimetype='image/gif',
        download_name='pixel.gif',
        as_attachment=False
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
