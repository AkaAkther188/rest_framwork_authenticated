from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404




@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_data(request):
    student = Student.objects.filter(user=request.user)
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)  
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_student(request, id):
    student = get_object_or_404(Student, id=id, user=request.user)
    serializer = StudentSerializer(student, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_student(request, id):
    student = get_object_or_404(Student, id=id, user=request.user)
    student.delete()
    return Response({"message": "Deleted successfully"}, status=204)




#class StudentList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    #def get(self, request, format=None):
        #student = Student.objects.all()
        #serializer = StudentSerializer(student, many=True)
        #return Response(serializer.data)

    #def post(self, request, format=None):
        #serializer = StudentSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)