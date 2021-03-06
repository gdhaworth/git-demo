from example import app

from time import sleep
from datetime import datetime

@app.route('/process')
def process():
    """
    Does a lot of processing.
    """
    sleep(3)
    return 'Processing Complete!'

@app.route('/time')
def time():
    """
    Gets the current time.
    """
    return datetime.now().strftime('%d/%m/%y %H:%M')
