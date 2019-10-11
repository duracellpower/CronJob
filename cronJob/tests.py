from django.test import TestCase
import requests

from cronJob.models import CronJob

URL = "http://127.0.0.1:8000/index"

PARAMS = {'title': '123456',
          'http': 'www.google.com',
          'benutzername': 'Test',
          'passwort': 'testpassword123',
          'ausführung': '2',
          'tagStunde': '16',
          'tagMinute': '15',
          'fehlgeschlagen': True,
          'speichern': True
}

requests.get(url=URL, params=PARAMS)

# db auslesen
success = False
entrys = CronJob.objects.all()
for entry in entrys:
    if entry.title == '123456':
        success = True
        break


if success:
    print("Test erfolgreich.")
else:
    print("Test failed")


