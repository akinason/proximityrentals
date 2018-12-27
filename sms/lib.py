from django.utils.http import urlencode

import requests

from globals import DEFAULT_SMS_SENDER
from proximityrentals import settings


def send_1s2u_sms(number, message, sender=None):
    number = str(number).replace(" ", "").replace("+", "")
    url = settings.ONE_S_2_U_SEND_URL
    username = settings.ONE_S_2_U_USERNAME
    password = settings.ONE_S_2_U_PASSWORD
    mno = number
    msg = message
    sid = sender if sender else DEFAULT_SMS_SENDER
    fl = 0
    mt = 0
    ipcl = "127.0.0.1"
    content = ''
    status_code = ''
    err = {}
    message_id = ""
    success = True
    params = {
        'username': username, 'password': password, 'msg': msg, 
        'Sid': sid, 'fl': fl, 'mt': mt, 'ipcl': ipcl, 'mno': mno
    }
    encoded_params = urlencode(params)
    try:
        response = requests.get(url=url, params=encoded_params)
        status_code = response.status_code
        try:
            message_id = response.content.decode('ascii')
        except AttributeError:
            message_id = response.content
        except Exception:
            message_id = response.content
    except Exception as err:
        status_code = 404
        success = False

    res = {'status_code': str(status_code), 'message_id': message_id, 'error': err, "success": success}
    return res


def format_number(number):
    # Formats the number following international standards. Returns a valid phone number or None

    return number
