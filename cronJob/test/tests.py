from django.test import SimpleTestCase
from django.urls import reverse, resolve

from cronJob.views import index, userLogin, userAuthentification, userLogout, home

# mit Unterstützung von Mike, nachdem mein vorheriges Test-Projekt leider nicht ging (siehe views.py zu unterst)

class UrlTest(SimpleTestCase):

    def testIndex(self):
        url = reverse('homepage')
        self.assertEqual(resolve(url).func, index)

    def testLogin(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, userLogin)

    def testRegister(self):
        url = reverse('authentification')
        self.assertEqual(resolve(url).func, userAuthentification)

    def testLogout(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, userLogout)

    def testHome(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)


