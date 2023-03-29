from django.urls import path
from blog import views
urlpatterns = [
    path('',views.index,name='index'),
    path('detail/<int:post_id>',views.detail,name='detail')


]
