from django.urls import path

from . import views

app_name = 'review'

urlpatterns = [
    path('', views.add_review, name='review'),

]