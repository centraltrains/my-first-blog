from django.test import TestCase


# Create your tests here.
class CVPageTest(TestCase):
    
    def test_display_template(self):
        responce = self.client.get("/cv/")
        self.assertTemplateUsed(responce, "cv.html")