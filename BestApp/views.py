from django.shortcuts import render
from BestApp.models import MostPopular
from BestApp.models import MediaType
from BestApp.models import Recent
from BestApp.models import Cast
from BestApp.forms import NewUserForm
from .models import Post
from django.utils import timezone


def homePage(request):
    recentList = Recent.objects.all().filter(media__mediaType=MediaType.MOVIE.name)
    mostPopularMovieList = MostPopular.objects.all().filter(media__mediaType=MediaType.MOVIE.name)
    mostPopularTvShowList = MostPopular.objects.all().filter(media__mediaType=MediaType.TV_SHOW.name)
    castList = Cast.objects.all()
    return render(request, 'home-page.html', context={'recentList': recentList, 'mostPopularMovieList': mostPopularMovieList, 'mostPopularTvShowList': mostPopularTvShowList, 'castList': castList})


def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return homePage(request)
        else:
            print('ERROR FORM IS INVALID!')

    return render(request, 'users.html', {'form': form})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def movies(request):
    return render(request, 'movies.html')

def seriesPage(request):
    return render(request, 'series.html')

def detail(request):
    return render(request, 'detail.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')