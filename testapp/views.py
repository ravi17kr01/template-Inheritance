from django.shortcuts import render

def home_views(request):
    return render(request, 'testapp/home.html')

def movie_views(request):
    return render(request, 'testapp/movies.html')

def sports_views(request):
    return render(request, 'testapp/sports.html')

def politics_views(request):
    return render(request, 'testapp/politics.html')
