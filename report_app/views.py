from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'graph/index.html')


def graphpage(request):
    word = request.GET.get('chk','')
    if word == "CCTV":
        return render(request,'graph/living.html',{'word':word})

