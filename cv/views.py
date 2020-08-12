from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import CVrecord
from .forms import PostCVrecord


# Create your views here.
def cv_home(request):

    if request.method == "POST":
        form = PostCVrecord(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            #post.author = request.user
            entry.save()
            return redirect('cv_home')

    eduLog = CVrecord.objects.filter(record_type="education")
    return render(request, "cv.html", {"eduLog" : eduLog})


def cv_edit(request, pk):
    savedEntry = get_object_or_404(CVrecord, pk=pk)

    if request.method == "POST":
        form = PostCVrecord(request.POST, instance = savedEntry)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect("cv_home")

    form = PostCVrecord(instance=savedEntry)


    return render(request, "edit.html", {"entry" : savedEntry, "form" : form})

def cv_delete(request, pk):
    savedEntry = get_object_or_404(CVrecord, pk=pk)
    savedEntry.delete()

    return redirect("cv_home")


