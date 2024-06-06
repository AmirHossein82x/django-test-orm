from django.shortcuts import render

# Create your views here.



def show(request):
    query = None
    return render(request, "store/index.html")