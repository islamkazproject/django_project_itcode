from django.contrib import admin
from django.urls import path

from coffee.views import index, employer_of_the_month, add_employer, staff


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('employerofthemonth/', employer_of_the_month, name='employer'),
    path('addemployer/', add_employer, name='add'),
    path('staff/', staff, name='staff'),
]
