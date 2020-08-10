from django.test import TestCase
from .models import CVrecord
from datetime import datetime, date
from .forms import PostCVrecord




# Create your tests here.
class CVPageTest(TestCase):
    
    def test_display_template(self):
        responce = self.client.get("/cv/")
        self.assertTemplateUsed(responce, "cv.html")

    def test_can_save_education_POST_request(self):
        responce = self.client.post("/cv/", data = {
            "record_type" : "education",
            "name" : "St Georges",
            "details" : "GCSEs: A*A*A*AABCD",
            "start_date" :  "2010-01-01",
            "end_date" :  "2010-01-01"})

        #form = PostCVrecord({
       #     "record_type" : "education",
       #     "name" : "St Georges",
       #     "details" : "GCSEs: A*A*A*AABCD",
       #     "start_date" :  "2010-01-01",
       #     "end_date" :  "2010-01-01"})

       # if form.is_valid():
       #     post = form.save(commit=False)
       #     post.save()

        self.assertEqual(CVrecord.objects.count(), 1)
        new_item = CVrecord.objects.first()
        self.assertEqual(new_item.name, "St Georges")
