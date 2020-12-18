from django.urls import path
from managebook import views

urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('bf/', views.BookFieldList.as_view(), name='book_field_list'),
]