from django.urls import path, include
from . import views

# the routes will be defined here
urlpatterns = [
    # empty string is root path
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # records
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_details, name='details'),
    path('records/create/', views.RecordCreate.as_view(), name='records_create'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),

    # add track or artist on record
    path('records/<int:record_id>/add_track/', views.add_track, name='add_track'),
    path('records/<int:record_id>/add_photo/', views.add_photo, name='add_photo'),
    path('records/<int:record_id>/assoc_artist/<int:artist_id>', views.assoc_artist, name='assoc_artist'),

    # artists
    path('artists/', views.ArtistList.as_view(), name='artists_index'),
    path('artists/<int:pk>/', views.ArtistDetail.as_view(), name='artists_detail'),
    path('artists/create/', views.ArtistCreate.as_view(), name='artists_create'),
    path('artists/<int:pk>/update/', views.ArtistUpdate.as_view(), name='artists_update'),
    path('artists/<int:pk>/delete/', views.ArtistDelete.as_view(), name='artists_delete'),

    #auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup')
]