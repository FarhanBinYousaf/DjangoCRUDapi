from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/',views.student_detail),
    path('stucreate/',views.student_create),
]
