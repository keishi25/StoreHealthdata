from django.urls import path
from store.views import AuthorCreate, MyListView,AuthorUpdate

urlpatterns = [
    path('post', AuthorCreate.as_view(), name='post'),
    path('<int:pk>/list', MyListView.as_view(), name='list'),
    path('<int:pk>/update', AuthorUpdate.as_view(), name='update')
]