from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def generatedpassword(request):

    length = int(request.GET.get("length"))
    characters =  [chr(x) for x in range(97,123)]

    if request.GET.get('uppercase'):
        characters.extend( [chr(x).upper() for x in range(97,123)])
    if request.GET.get('numbers'):
        characters.extend([chr(x) for x in range(48, 58)])
    if request.GET.get('special characters'):
        characters.extend([chr(x)  for x in range(33, 127) if (chr(x).isalpha(), chr(x).isdigit()) == (False, False)])

    return render(request, 'generator/password.html', {'password':  ''.join(random.choice(characters) for y in range(length+1))})