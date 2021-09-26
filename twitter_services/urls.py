from django.urls import path
from .views import retrieve_index_page, create_view, delete_view

urlpatterns = [
    path('', retrieve_index_page, name="index_page"),  # index page request
    path('create/', create_view, name="create_tweet"),  # create tweet request
    path('delete/', delete_view, name="delete_tweet"),  # delete tweet request
]
