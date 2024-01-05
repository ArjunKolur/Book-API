from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allBooks=Book.objects.all().values()
        return Response({"message":"List of Books","Book List":allBooks})
    
    def post(self,request):
        print('Requested Data is:',request.data)
        serializer_obj=BookSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            Book.objects.create(id=serializer_obj.data.get("id"),
                            title=serializer_obj.data.get("title"),
                            author=serializer_obj.data.get("author"),
                            )
        
        book=Book.objects.all().filter(id=request.data["id"]).values()
        return Response({"message":"New Book is added!","Book List":book})
    

# Create your views here.
 