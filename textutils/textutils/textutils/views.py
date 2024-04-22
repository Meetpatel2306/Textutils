# from django.http import HttpResponse
# from django.shortcuts import render
#
# # # video 9 text box banavanu and button tag and button dabao to charcounter page khule
# def index(request):
#     return render(request,'index.html')


# video 9
# def charcounter(request):
#     print(request.GET.get('text','default'))#text=text mate ,default=kai na lakhie to default lai le
#     return HttpResponse('''charcounter <br><a href="http://127.0.0.1:8000/"> back to home</a>''')

# templates and index page with adding parameters video 8
# def index(request):
#     a={'name':"meet patel",'place':"ahmedabad",'age':20 }
#     return render(request,'index.html',a)

# code for video 6
# def index(request):
#     #youtube video access link
#     return HttpResponse('''<h1> meet patel </h1> <a href="https://youtu.be/AepgWsROO4k?si=WgRO23DcMnxvnaJv">Django code with harry video 6 is here</a>''' )
# def about(request):
#     return HttpResponse("my name is meet patel")

# back button video 7
# def index(request):
#     return HttpResponse("home page this is meet patel ")
# def removepunc(request):
#     return HttpResponse('''remove punc page <br><a href="http://127.0.0.1:8000/"> back to home</a>''')
# def capitalizefirst(request):
#     return HttpResponse('''capital first<br><a href="http://127.0.0.1:8000/"> back to home</a>''')
# def newlineremove(request):
#     return HttpResponse('''new line remover page <br><a href="http://127.0.0.1:8000/">back to home </a>''' )
# def spaceremover(request):
#     return HttpResponse('''space remover<br><a href="http://127.0.0.1:8000/"> back to home</a>''')
# def charcounter(request):
#     return HttpResponse('''charcounter <br><a href="http://127.0.0.1:8000/"> back to home</a>''')


from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

# def exercise1(request):
#     a='''<h1>Navigation Bar <br></h1>
#             <a href="https://www.flipkart.com/">Flipkart</a>
#             <br>
#             <a href="https://www.instagram.com/">instagram</a>
#             <br>
#             <a href="https://www.facebook.com/">facebook</a>
#             <br>
#             <a href="https://www.whatsapp.com/">whatsapp</a>'''
#     return HttpResponse(a)

# video 10
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
