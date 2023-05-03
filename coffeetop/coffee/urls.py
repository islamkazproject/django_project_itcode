from django.urls import path, include
from coffeetop.coffee import views
from coffeetop.coffee import templates
from coffeetop.coffee.views import staff

urlpatterns = [
    path('', staff, name='index'),
]