from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/<int:pk>', views.StudentView.as_view()),
    path("studentlist/", views.StudentList.as_view()),
    path('studentcreate/', views.StudentCreate.as_view()),
    path('studentupdate/', views.StudentUpdate.as_view()),
   
    ]