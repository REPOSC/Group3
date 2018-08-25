import sys
from django.test import TestCase, Client
sys.path.append("..")
from server.debug import debug


class SendviewsTestCase(TestCase):
    def setUp(self):
        # self.device = Device(hostname="CN-BJ-0000-00",mac="ff:ff:ff:ff:ff:ff").save()
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

    def test_getbook(self):
        self.audio_file = open('test.m4a', 'rb')
        self.image_file = open('test.jpg', 'rb')
        rep = self.client.post('/get_book', {
            'bookname': 'sleep',
            'level': 1,
            'introduction': 'a book.',
            'persual': 'false',
            'guides': ['1', '2', '3'],
            'knowledges': ['11', '22', '33', '44'],
            'word_text': ['111', '222'],
            'word_audio': [self.audio_file, self.audio_file],
            'book_english_text': ['au', 'bu'],
            'book_chinese_text': ['au_ch', 'bu_ch'],
            'book_audio': [self.audio_file, self.audio_file],
            'book_picture': [self.image_file, self.image_file],
            'first_game_text': ['apple', 'banana'],
            'first_game_picture': [self.image_file, self.image_file],
            'second_game_text': 'return',
            'second_game_answer': '3',
            'second_game_picture': [self.image_file, self.image_file, self.image_file, self.image_file]
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')

    def test_changeprocess(self):
        self.test_createstudent()
        self.test_getbook()
        rep = self.client.post('/change_process', {
            'username': '10000001',
            'booknumber': 1,
            'process': 0.1
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'true')

    def test_getprocess(self):
        self.test_changeprocess()
        rep = self.client.post('/get_process', {
            'username': '10000001',
            'booknumber': 1,
        })
        self.assertContains(rep, '0.1')
        rep = self.client.post('/get_process', {
            'username': '10000002',
            'booknumber': 1,
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, '0')

    def test_firstfunction(self):
        self.test_getbook()
        rep = self.client.post('/get_first_function', {
            'book_id': 1,
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, '222')
        self.assertContains(rep, '33')

    def test_secondfunction(self):
        self.test_getbook()
        rep = self.client.post('/get_second_function', {
            'book_id': 1,
        })
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, '2')

    def test_getbooks(self):
        self.test_changeprocess()
        rep = self.client.post('/get_books', {
            'id': '10000001',
            'level': 0
        })
        self.assertContains(rep, '0.1')
        self.assertContains(rep, 'sleep')
        self.assertContains(rep, 'false')

    def test_getpagetexts(self):
        self.test_getbook()
        rep = self.client.post('/get_page_texts', {
            'book_id': 1,
            'book_page': 1
        })
        self.assertContains(rep, 'bu_ch')

    def test_getfirstgametexts(self):
        self.test_getbook()
        rep = self.client.post('/get_first_game_texts', {
            'book_id': 1
        })
        self.assertContains(rep, 'apple')
        self.assertContains(rep, 'banana')
