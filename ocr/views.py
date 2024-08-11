import easyocr
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def text_recognition(file):
    reader = easyocr.Reader(['ru', 'en'])
    result = reader.readtext(file)

    return result


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            text_recognition(request.FILES["file"])
            return HttpResponseRedirect("/success/url/")
    else:
        form = UploadFileForm()
    return render(request, "index.html", {"form": form})
