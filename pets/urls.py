from django.urls import path
from .views import PetView, PetListView, IndexPageView,ContactsView


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('pets/', PetListView.as_view(), name='pets'),
    path('pets/<str:pk>', PetView.as_view()),
    path('contats/', ContactsView.as_view(), name='contacts'),
]