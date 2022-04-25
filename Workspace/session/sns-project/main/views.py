from django.shortcuts import render

# Create your views here.
def showmain(request):
    return render(request, 'main/mainpage.html')

def activities(request):
    return render(request, 'main/activities.html')

def favorite(request):
    return render(request, 'main/favorite.html')

def contact(request):
    return render(request, 'main/contact.html')