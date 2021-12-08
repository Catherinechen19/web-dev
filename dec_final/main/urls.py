from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('history/', views.history, name="history-page"),
    path('catalogue/', views.catalogue, name="catalogue-page"),
    path('request/', views.request, name="requests-page"),
    path('refund/', views.refund, name="refund-page"),
    path('registration/', views.registration, name="registration-page"),
    path('review/', views.review, name="review-page"),
    path('forum/', views.forum, name="forum-page"),
    path('discussion/<int:myid>/', views.discussion, name="discussion-page"),
]
