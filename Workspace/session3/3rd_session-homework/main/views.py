from django.shortcuts import render


# introduce view 함수
def showintroduce(request):
    return render(request, 'main/introduce.html')

# activities view 함수
def showactivities(request):
    return render(request, 'main/activities.html')

# contact view 함수
def showfavorite(request):
    return render(request, 'main/favorite.html')

# contact view 함수
def showcontact(request):
    return render(request, 'main/contact.html')
