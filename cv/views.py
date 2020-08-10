from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CVrecord
from .forms import PostCVrecord


# Create your views here.
def cv_home(request):

    if request.method == "POST":
        form = PostCVrecord(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.author = request.user
            post.save()
            return redirect('cv_home')

    eduLog = CVrecord.objects.filter(record_type="education")
    return render(request, "cv.html", {"eduLog" : eduLog})

