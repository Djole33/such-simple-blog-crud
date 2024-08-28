from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('post-details/<int:pk>', views.post_details, name='post-details'),
   path('add-post/', views.add_post, name='add-post'),
   path('update-post/<int:pk>', views.update_post, name='update-post'),
   path('delete-post/<int:pk>', views.delete_post, name='delete-post'),
]
