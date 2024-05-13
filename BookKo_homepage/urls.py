from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("BookKO/", views.home_page2, name="userlog_page"),
    path("Cart/", views.cart, name="cart"),
    path("Settings/", views.user_settings, name="settings"),
    path("userlogout", views.log_out, name="logout"),
    path("Addcart/", views.updatecart, name="updatecart"),
    path("book_id/<int:bookID>/", views.book_ID, name="book_id"),
    path("search_book", views.search_book, name="search_book"),
    path("genre_search/<str:genreID>", views.genre_search, name="genre_search"),
]
