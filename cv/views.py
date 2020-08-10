from django.shortcuts import render, redirect, get_object_or_404
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


def cv_edit(request, pk):
    entry = get_object_or_404(CVrecord, pk=pk)

    form = PostCVrecord(instance=entry)


    return render(request, "edit.html", {"entry" : entry, "form" : form})

