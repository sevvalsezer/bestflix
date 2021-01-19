from django.contrib import admin
from BestApp.models import Media
from BestApp.models import MostPopular
from BestApp.models import Recent
from BestApp.models import User


# Register your models here.
admin.site.register(Media)
admin.site.register(MostPopular)
admin.site.register(Recent)
admin.site.register(User)
