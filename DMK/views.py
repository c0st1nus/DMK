from django.shortcuts import render
import g4f
# Create your views here.
def home(request):
    return render(request, 'DMK/pl1.html')

def test(request):
    return render(request, 'DMK/test.html')