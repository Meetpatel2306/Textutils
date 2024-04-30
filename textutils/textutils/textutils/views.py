from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcounter=request.POST.get('charcounter','off')

    if removepunc=="on":
        # analyzed=djtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+ char

        params={'purpose':"remove punchhhhhh",'analyzed_text':analyzed}
        # return HttpResponse("remove punc")
        # return render(request,'analyze.html',params)
        djtext=analyzed

    if (fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed+char.upper()
        params={'purpose':"change to upper case",'analyzed_text':analyzed}
        # return render(request,'analyze.html',params)
        djtext=analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': "remove new line", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    if (spaceremove == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" "and djtext[index]==" ":
                pass
            else:
                analyzed=analyzed+char
        params = {'purpose': "remove space", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext=analyzed

    if(charcounter == "on"):
        analyzed = ""
        for char in djtext:
            if char in djtext:
                djtext[char] = djtext.get(char, 0) + 1
            else:
                djtext[char] = 1
                analyzed=analyzed+char
        params = {'purpose': "count character", 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if (removepunc != "on" and newlineremover != "on" and spaceremove != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)
