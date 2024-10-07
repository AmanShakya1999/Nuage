from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Department, Student, Course, AttendanceLog
from .serializers import UserSerializer, DepartmentSerializer, StudentSerializer, CourseSerializer, AttendanceLogSerializer


class UserView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST)

class DepartmentView(APIView):
    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST)

class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = StudentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST)

class CourseView(APIView):
    def get(self, request):
        try:
            courses = Course.objects.all()
            serializer = CourseSerializer(courses, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST) 

    def post(self, request):
        try:
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST)

class AttendanceLogView(APIView):
    def get(self, request):
        attendance_logs = AttendanceLog.objects.all()
        serializer = AttendanceLogSerializer(attendance_logs, many=True)
        return Response(serializer.data)

    def post(self, request):
        try:
            serializer = AttendanceLogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
             return Response({'error': 'Please try Again.'}, status=status.HTTP_400_BAD_REQUEST)
class MarkAttendanceView(APIView):
    def post(self, request):
        student_id = request.data.get('student_id')
        course_id = request.data.get('course_id')
        attendance_status = request.data.get('attendance_status')

        if student_id and course_id and attendance_status:
            try:
                student = Student.objects.get(id=student_id)
                course = Course.objects.get(id=course_id)
                attendance_log = AttendanceLog.objects.create(
                    student=student,
                    course=course,
                    attendance_status=attendance_status
                )
                serializer = AttendanceLogSerializer(attendance_log)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Student.DoesNotExist or Course.DoesNotExist:
                return Response({'error': 'Student or course not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)