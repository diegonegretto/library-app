from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')
        self.resp2 = self.client.get('/', follow=True)
    
    def test_302_response(self):
        self.assertEqual(self.resp.status_code, 302)
    
    def test_200_response(self):
        self.assertEqual(self.resp2.status_code, 200)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp2, 'books.html')
        self.assertTemplateUsed(self.resp2, 'base.html')
        