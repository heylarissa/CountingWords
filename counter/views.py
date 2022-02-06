from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

import re

def index(request):

    if request.method == 'POST':
 
        text = request.POST['texttocount']

        if len(text) > 0:
 
            regex = re.compile('[^\w\,\.\d]+')
            word = len(re.split(regex, text))

            i = True
 
            return render(request, 'counter/index.html',
                          {'word': word, 'error': False, 'text': text, 'i': i, 'on': 'active'})
 
        else:
            return render(request, 'counter/index.html',
                          {'word': '', 'error': True, 'text': text, 'i': False, 'on': 'active'})
 
    else:
        return render(request, 'counter/index.html', {'on': 'active'})
