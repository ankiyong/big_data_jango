from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'graph/index.html')


def graphpage(request):
    word = request.GET.get('chk','')
    return render(request,f'graph/{word}.html',{'word':word})


def chart(request):
    word = request.GET.get('chart','')
    return render(request,'graph/population1.html')

def livingchart(request):
    word = request.GET.get('chart','')
    return render(request,'graph/living1.html')

def safechart(request):
    word = request.GET.get('chart','')
    return render(request,'graph/safety1.html')

def societychart(request):
    word = request.GET.get('chart','')
    return render(request,'graph/society1.html')
