from django.urls import path
from .views import All_grades, A_grades

urlpatterns = [
    path('', All_grades.as_view(), name='all_grades'),
    path('<str:student>/<str:subject>/', A_grades.as_view(), name='a_grades')
]