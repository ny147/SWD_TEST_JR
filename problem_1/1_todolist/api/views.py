from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response


class TaskList(APIView):
    def get(self,request):
        TK = Task.objects.all()
        serializer = TaskSerializer(TK,many=True)
        return Response(serializer.data)
    
    # return Response(queryset.data)
    def post(self,request):
        thisdata = request.data
        serializer = TaskSerializer(data = thisdata)
        if(serializer.is_valid()):
            serializer.save()
            res = {'msg' : 'Data has been created Successfully'}
            return Response(res)
        
class Taskone(APIView):
    def get(self,request,pk):
        tk = Task.objects.get(id=pk)
        serializer = TaskSerializer(tk)
        return Response(serializer.data)
    def delete(self,request,pk):
        tk = Task.objects.get(id=pk)
        tk.delete()
        return Response('Item successfully delete !')
    def put(self,request,pk):
        tk = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=tk,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)