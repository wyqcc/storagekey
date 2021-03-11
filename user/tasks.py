from storagekey.celery import app
from tools.sms import WangYongQi
from django.conf import settings


@app.task
def send_sms(phone, code):
    x = WangYongQi(settings.SMS_ACCOUNT_ID,
                   settings.SMS_ACCOUNT_TOKEN,
                   settings.SMS_APP_ID,
                   settings.SMS_TEMPLATE_ID)
    res = x.run(phone, code)
    return res
