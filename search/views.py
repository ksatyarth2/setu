from django.shortcuts import render
from helperapp.main import execute
from helperapp.text_to_speech import say

# Create your views here.
def search(request):
    schemes = execute()
    say('vibhinn upalabdh yojanaen hain')
    for scheme in schemes:
        say(scheme)
    schemes = [scheme.rstrip('\n') for scheme in schemes]
    return render(request, 'helperapp/search.html', {'schemes' : schemes})
    

