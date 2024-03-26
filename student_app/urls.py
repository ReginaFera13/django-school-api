from django.urls import path
from .views import All_students, A_students

urlpatterns = [
    path('', All_students.as_view(), name='all_students'),
    path('<int:id>/', A_students.as_view(), name='a_student'),
    path('add_subject/<int:id>/<int:subject_id>/', A_students.as_view(), name='add_subject')
]