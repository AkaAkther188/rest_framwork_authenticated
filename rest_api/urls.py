from django.urls import path
from .views import get_data, create_student, update_student, delete_student
urlpatterns = [
    path("get/student/",  get_data),
    path("create/student/",  create_student),
    path("update/student/<int:id>/",  update_student),
    path("delete/student/<int:id>/",  delete_student),
]
