from django.urls import path
from news.views import post_detail_view, post_list_view


urlpatterns = [
    path('', post_list_view, name='posts_list_url'),
    path('<int:id>/', post_detail_view, name='post_detail_url'),
]