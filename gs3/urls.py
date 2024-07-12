
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/<int:id>', views.student_detail),
    path('student/', views.student_data),
]
