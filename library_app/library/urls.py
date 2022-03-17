from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('books-json', views.books_json, name='book_list_json'),
    path('create/', views.BookCrateView.as_view(), name='book_create'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('<int:pk>/edit/', views.BookEditView.as_view(), name='book_edit'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    
    path('category/', views.CategoryListView.as_view(), name='category_list'),
    path('category/create/', views.CategoryCrateView.as_view(), name='category_create'),
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/edit/', views.CategoryEditView.as_view(), name='category_edit'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),
]