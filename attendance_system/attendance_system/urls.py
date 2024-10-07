from django.urls import path
from ams.views import UserView, DepartmentView, StudentView, CourseView, AttendanceLogView, MarkAttendanceView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('departments/', DepartmentView.as_view()),
    path('students/', StudentView.as_view()),
    path('courses/', CourseView.as_view()),
    path('attendance-logs/', AttendanceLogView.as_view()),
    path('mark-attendance/', MarkAttendanceView.as_view()),
]