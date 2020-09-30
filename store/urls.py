from django.urls import path
from store.views import AuthorCreate, MyListView

urlpatterns = [
    path('post', AuthorCreate.as_view()),
    path('<int:pk>/list', MyListView.as_view(), name='list')
]