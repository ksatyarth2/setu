from django.shortcuts import render
from helperapp.text_to_speech import say

def index(request):
    message = ""
    return render(request, 'helperapp/index.html', {"message" : message})

def auth(request):
    aadhar = request.POST.get('aadhar')
    phone = request.POST.get('phone')
    if aadhar == '315486929673' and phone == '9759644218':
        message = "success"
        say("saphal pravesh")
        return render(request, 'helperapp/search.html', {'schemes' : ""})
    else:
        message = "failed login"
        say("asaphal pravesh")
        return render(request, "helperapp/index.html", {"message" : message})