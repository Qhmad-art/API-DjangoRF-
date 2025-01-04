from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer
from .models import Student
class StudentView(APIView):
    def get(self, request,pk=None ,format=None):
        if pk is not None:
            student = Student.objects.filter(id=pk).first()
            if student is None:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
    def put(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    def delete(self,request):
        student = Student.objects.get('id')
        student.delete()
        return Response({"message": "Student deleted"}, status=204)
    