from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import CVrecord
from .forms import PostCVrecord


# Create your views here.
def cv_home(request):

    if request.method == "POST":
        postData = request.POST.copy()
        postData["start_date"] = postData.get("start_date", timezone.now().strftime("%Y-%m-%d"))
        postData["end_date"] = postData.get("end_date", timezone.now().strftime("%Y-%m-%d"))

        form = PostCVrecord(postData)
        if form.is_valid():
            entry = form.save(commit=False)
            #post.author = request.user
            entry.save()
            return redirect('cv_home')

    education = CVrecord.objects.filter(record_type="education").order_by("-start_date")
    headInfo = CVrecord.objects.filter(record_type="headInfo")
    work = CVrecord.objects.filter(record_type="work").order_by("-start_date")

    data = {"education" : education, 
            "headInfo" : headInfo, 
            "work" : work}
    return render(request, "cv.html", data)


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


