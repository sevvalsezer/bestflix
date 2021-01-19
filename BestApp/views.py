from django.shortcuts import render
from BestApp.models import MostPopular
from BestApp.models import MediaType
from BestApp.models import Recent
from .models import Post
from django.utils import timezone


def homePage(request):
    recentList = Recent.objects.all().filter(media__mediaType=MediaType.MOVIE.name)
    mostPopularMovieList = MostPopular.objects.all().filter(media__mediaType=MediaType.MOVIE.name)
    mostPopularTvShowList = MostPopular.objects.all().filter(media__mediaType=MediaType.TV_SHOW.name)
    return render(request, 'home-page.html',
                  context={'recentList': recentList, 'mostPopularMovieList': mostPopularMovieList,
                           'mostPopularTvShowList': mostPopularTvShowList})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})
