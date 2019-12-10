from django.urls import path

from . import views
app_name='rating'

urlpatterns=[
 path('list/',views.MovieRatingAPIView.as_view(),name='list'),

   
]