from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='homepage'),
    path('auth', views.Authorized.as_view(), name='auth'),
    path('auth/<int:pk>', views.AuthDetailView.as_view(), name='auth.detail'),
    path('list', views.NotesListView.as_view(), name='notes.list'),
    path('list/<int:pk>', views.NotesDetailView.as_view(), name='notes.detail'),
    path('list/new', views.NotesNewView.as_view(), name='notes.new'),
    path('list/<int:pk>/edit', views.NotesEditView.as_view(), name='notes.edit'),
    path('list/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
    path('login/', views.LoginInterfaceView.as_view(),name='notes.login'),
    path('logout/', views.LogoutInterfaceView.as_view(),name='notes.logout'),
    path('signup/', views.SignUpView.as_view(),name='notes.signup'),
    #url(r'^(?P<postid>\d+)/preference/(?P<userpreference>\d+)/$', postpreference, name='postpreference'),
]

