from django.urls import path

from ep_190623.my_music_app.views import index_with_profile, index_no_profile, \
    add_album, album_details, \
    edit_album, delete_album, profile_details, delete_profile

"""
•	http://localhost:8000/ - home page
•	http://localhost:8000/album/add/ - add album page
•	http://localhost:8000/album/details/<id>/ - album details page
•	http://localhost:8000/album/edit/<id>/ - edit album page
•	http://localhost:8000/album/delete/<id>/ - delete album page
•	http://localhost:8000/profile/details/ - profile details page
•	http://localhost:8000/profile/delete/ - delete profile page
"""


urlpatterns = [
    path('', index_with_profile, name='index with profile'),
    path('no-profile/', index_no_profile, name='index no profile'),

    path('album/add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
