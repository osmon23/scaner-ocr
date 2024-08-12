import pytesseract
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from PIL import Image


def text_recognition(file):
    img = Image.open(file)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, lang='rus', config=custom_config)

    return text


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            result = text_recognition(request.FILES["file"])
            return HttpResponse(result)
    else:
        form = UploadFileForm()
    return render(request, "index.html", {"form": form})
