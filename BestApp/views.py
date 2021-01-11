from django.shortcuts import render


def homePage(request):
    return render(request, 'home-page.html')

def movies(request):
    return render(request, 'movies.html')

def seriesPage(request):
    return render(request, 'series.html')

def detail(request):
    return render(request, 'detail.html')