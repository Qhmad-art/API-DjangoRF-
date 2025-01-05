from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
from api import views
router.register('modelview',views.StudentModelViewSet,basename="Studet")


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentapi/<int:pk>', views.StudentView.as_view()),
    path("studentlist/", views.StudentList.as_view()),
    path('studentcreate/', views.StudentCreate.as_view()),
    path('studentupdate/', views.StudentUpdate.as_view()),
    path('gpstudent/',views.StudentGetCreate.as_view()),
    path('udstudent/<int:pk>/',views.StudentUpdateDelete.as_view()),
    path('',include(router.urls))
   
    ]