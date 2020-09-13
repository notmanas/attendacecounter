from django.urls import path
from  . import views

urlpatterns = [
    path('', views.home , name = 'home' ),
    path('att/', views.selection_sheet , name = 'att' ),
    path('att/<int:pk>/', views.attendence_sheet , name = 'student' ),
    path('student_profile/', views.student_profile , name = 'student_profile' ),
]

'''path('att/<int:pk>/clone/', views.clone , name = 'clone' ),'''