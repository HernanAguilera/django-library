from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('create/', views.BookCrateView.as_view(), name='book_create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/edit/', views.BookEditView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]