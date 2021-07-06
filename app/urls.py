from django.urls import path

from .views import *


urlpatterns = [
    path('', HomePageView.as_view(), name='images'),
    path('image_details/<int:image_id>/', image_details_view, name='image_page'),
    path('add_image/', add_image_view, name='add_image')
]
