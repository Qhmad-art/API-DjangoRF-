from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework .mixins import ListModelMixin
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import UpdateModelMixin,DestroyModelMixin
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



##################             Generic API      ###########################

# GET  --->> If we want to Get one student's Data then Use Retrieve instead of List
class StudentList(GenericAPIView, ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# POST
class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
# UPDATE/PUT
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
# Delete
class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    ############   GET and POST    #############


class StudentGetCreate(ListModelMixin, CreateModelMixin, GenericAPIView):
      queryset = Student.objects.all()
      serializer_class = StudentSerializer

    
      def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

      def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)   
       
    ###############  UPDATE and  DELETE   #################


    
class StudentUpdateDelete(UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    

    # Handle PUT requests to update a Student
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # Handle DELETE requests to delete a book
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

