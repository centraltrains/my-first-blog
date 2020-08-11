from django.test import TestCase
from .models import CVrecord
from datetime import datetime, date
from .forms import PostCVrecord

testData = {
            "record_type" : "education",
            "name" : "St Georges",
            "details" : "GCSEs: A*A*A*AABCD",
            "start_date" :  "2010-01-01",
            "end_date" :  "2010-01-01"}


# Create your tests here.
class CVPageTest(TestCase):
    
    def test_display_template(self):
        responce = self.client.get("/cv/")
        self.assertTemplateUsed(responce, "cv.html")

    def test_can_save_education_POST_request(self):
        responce = self.client.post("/cv/", data = testData)

        self.assertEqual(CVrecord.objects.count(), 1)
        new_item = CVrecord.objects.first()
        self.assertEqual(new_item.name, "St Georges")

    def test_edit_page_GET_request(self):
        responce = self.client.post("/cv/", data = testData)
        responce = self.client.get("/cv/1/edit")
        self.assertTemplateUsed(responce, "edit.html")

    def test_edit_page_GET(self):
        form = PostCVrecord(testData)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()

        responce = self.client.get("/cv/1/edit")
        self.assertTemplateUsed(responce, "edit.html")

    def test_edit_page_POST(self):
        responce = self.client.post("/cv/", testData)

        responce = self.client.post("/cv/1/edit", data = {"record_type" : "education",
            "name" : "St Georges",
            "details" : "GCSEs: None",
            "start_date" :  "2010-01-01",
            "end_date" :  "2010-01-01"})

        eddited_item = CVrecord.objects.first()
        self.assertEqual(eddited_item.details, "GCSEs: None")

        
