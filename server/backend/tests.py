from django.test import TestCase, Client
import sys
sys.path.append("..")
from server import debug


class SendviewsTestCase(TestCase):
    def setUp(self):
        #self.device = Device(hostname="CN-BJ-0000-00",mac="ff:ff:ff:ff:ff:ff").save()
        self.client = Client()
        self.tmp_pwd = None

    def test_addmanager(self):
        rep = self.client.post("/add_manager", {
            "username": "abcdef",
            "password": "123456",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, "100001")
        self.assertContains(rep, "123456")

        rep = self.client.post("/add_manager", {
            "username": "abcdef",
            "password": "123456",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, "100002")
        self.assertContains(rep, "123456")

    def test_authmanager(self):
        self.test_addmanager()
        rep = self.client.post('/auth_manager', {
            "id": "100009",
            "password": "222222",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'error')
        rep = self.client.post('/auth_manager', {
            "id": "100001",
            "password": "123456",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'right')

    def test_changemanager(self):
        self.test_addmanager()
        rep = self.client.post('/change_manager', {
            "username": "100009",
            "password": "222222",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'false')
        rep = self.client.post('/change_manager', {
            "username": "100001",
            "password": "222222",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')

    def test_delmanager(self):
        self.test_addmanager()
        rep = self.client.post('/change_manager', {
            "username": "100009",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'false')
        rep = self.client.post('/change_manager', {
            "username": "100001",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')

    def test_createstudent(self):
        rep = self.client.post('/create_student', {"number": 3})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, '10000001')
        self.assertContains(rep, '10000002')
        self.assertContains(rep, '10000003')

    def test_changepassword(self):
        self.test_createstudent()
        rep = self.client.post('/change_password', {
            "username": "10000001",
            "password": "123456"
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')
        rep = self.client.post('/change_password', {
            "username": "10000009",
            "password": "123456"
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'false')

    def test_authstudent(self):
        self.test_changepassword()
        rep = self.client.post('/auth_student', {
            "id": "100001",
            "password": "222222",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'error')
        rep = self.client.post('/auth_student', {
            "id": "10000001",
            "password": '123456',
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'right')

    def test_getmanagers(self):
        self.test_createstudent()
        self.test_addmanager()
        rep = self.client.post('/get_managers', {})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, '100001')
        self.assertContains(rep, '100002')
        self.assertNotContains(rep, '10000001')
        self.assertNotContains(rep, '10000002')
        self.assertNotContains(rep, '10000003')

    def test_putmessage(self):
        rep = self.client.post('/put_message', {"content": "hello world"})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')

    def test_setlevel(self):
        self.test_createstudent()
        self.test_addmanager()
        rep = self.client.post('/set_level', {
            "username": "10000001",
            "values": "3",
            "values": "4",
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')
        rep = self.client.post('/set_level', {
            "content": "100001",
            "values": "1"
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'false')
