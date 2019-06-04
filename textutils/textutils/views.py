from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')

    remove = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremove', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount','off')
    analyzed=""
    if remove == 'on' and djtext != "":
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext = analyzed

    if fullcap == 'on' and djtext != "":
        analyzed = djtext.upper()
        params={'purpose':'Conversion to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed


    if newlineremover == 'on' and djtext != "":
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params ={'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        djtext = analyzed


    if charcount == 'on' and djtext != "":
        analyzed = f"The number of charcters in {djtext} is "+ str(len(djtext))
        params = {'purpose': 'Counts Number of characters', 'analyzed_text': analyzed}
    
    if remove != "on" and fullcap != "on" and newlineremover != "on" and charcount != "on":
        return HttpResponse("Error")
    
    return render(request, 'analyze.html',params)
    
def navigation(request):
    return render(request, 'navbar.html')