from django.shortcuts import render
from BestApp.models import MostPopular
from BestApp.models import MediaType
from BestApp.models import Recent
from BestApp.forms import NewUserForm


def homePage(request):
    recentList = Recent.objects.all().filter(media__mediaType=MediaType.MOVIE.name)
    mostPopularMovieList = MostPopular.objects.all().filter(media__mediaType=MediaType.MOVIE.name)
    mostPopularTvShowList = MostPopular.objects.all().filter(media__mediaType=MediaType.TV_SHOW.name)
    return render(request, 'home-page.html', context={'recentList': recentList, 'mostPopularMovieList': mostPopularMovieList, 'mostPopularTvShowList': mostPopularTvShowList})


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