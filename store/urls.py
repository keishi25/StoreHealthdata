from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberCreateList.as_view(), name='create'),
    path('<int:pk>/', views.MemberDetail.as_view(), name='detail'),
    #path('create/', views.MemberCreateList.as_view(), name='create'),
    path('<int:pk>/update/', views.MemberUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', views.MemberDelete.as_view(), name='delete'),
]