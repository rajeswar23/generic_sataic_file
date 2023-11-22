from django.shortcuts import render

# Create your views here.
def mummy(request):
    return render(request,'mummy.html')