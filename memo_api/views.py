from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Memo
from .serializers import MemoSerializer

@api_view(['GET', 'POST'])
def memo_list(request):
    if request.method == 'GET':
        memos = Memo.objects.all().order_by('-created_at')
        serializer = MemoSerializer(memos, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = MemoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def memo_detail(request, pk):
    memo = Memo.objects.get(id=pk)

    if request.method == 'PUT':
        serializer = MemoSerializer(memo, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    if request.method == 'DELETE':
        memo.delete()
        return Response({"message": "deleted"})
