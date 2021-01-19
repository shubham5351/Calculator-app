from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'cal/index.html')


def result(request):
    q = request.GET["query"]
    res = eval(q)
    context = {"result": res}
    return render(request, 'cal/result.html', context)
