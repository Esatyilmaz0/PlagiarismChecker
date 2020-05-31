from django.shortcuts import render
from user.models import UserProfile
import requests
# Create your views here.

def home(request):
    return render(request, template_name="index.html")

def pricing(request):
    return render(request, template_name="pricing.html")


def plagiarismCheck(request):
    if request.method == "POST":
        data = request.POST["data"]
        req = requests.post("https://www.prepostseo.com/apis/checkPlag", data={"key":"5219babae3754bf7f6dd261ed5286e33", "data":data})
        if request.user.is_authenticated:

            user = UserProfile.objects.get(user=request.user)
            if user.credit > 0:
                user.credit = user.credit - 1
                user.save()
                return render(request, template_name="plagiarismCheck.html", context={"data":req.json()})
        else:
            return render(request, template_name="plagiarismCheck.html", context={"data":req.json(), "content":data})

    return render(request, template_name="plagiarismCheck.html")