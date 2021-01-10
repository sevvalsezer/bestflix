from django.shortcuts import render


def homePage(request):
    return render(request, 'home-page.html')

def movies(request):
    return render(request, 'movies.html')
