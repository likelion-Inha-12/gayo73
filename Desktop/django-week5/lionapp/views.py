import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer  # PostSerializer를 가져오기
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

from .models import *

@swagger_auto_schema(
        method="POST", 
        tags=["첫번째 view"],
        operation_summary="post 생성", 
        operation_description="post를 생성합니다.",
        responses={
            201: '201에 대한 설명', 
            400: '400에 대한 설명',
            500: '500에 대한 설명'
        }
)

@authentication_classes([JWTAuthentication])
@api_view(['POST'])
def create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        title = data.get('title')
        content = data.get('content')

        post = Post(
            title = title,
            content = content
        )
        post.save()
        return JsonResponse({'message':'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다.'})

@authentication_classes([JWTAuthentication])
@api_view(['GET'])
def get_post(request, pk):
    if request.method == 'GET':
        post = get_object_or_404(Post, pk=pk)
        data = {
            'id': post.pk,
            'title': post.title,
            'content': post.content,
            'message': 'succeed'
        }
        return JsonResponse(data, status=200)
    else:
        return JsonResponse({'message':'GET 요청만 허용됩니다.'})

@authentication_classes([JWTAuthentication])
@api_view(['DELETE'])
def delete_post(request, pk):
    if request.method == 'DELETE':
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        data = {
            "message" : f"id: {pk} 포스트 삭제 완료"
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'message':'DELETE 요청만 허용됩니다.'})

@authentication_classes([JWTAuthentication])
@api_view(['POST'])
def create_post_v2(request):
    post = Post(
        title = request.data.get('title'),
        content = request.data.get('content')
    )
    post.save()

    message = f"id: {post.pk}번 포스트 생성 성공"
    return api_response(data = None, message = message, status = status.HTTP_201_CREATED)

@authentication_classes([JWTAuthentication])
@api_view(['GET'])
def api_response(data, message, status):
    response = {
        "message": message,
        "data": data
    }
    return Response(response, status=status)

class PostApiView(APIView):
    authentication_classes = [JWTAuthentication]
    def get_object(self, pk):
        post = get_object_or_404(Post, pk=pk)
        return post

    def get(self, request, pk):
        post = self.get_object(pk)

        postSerializer = PostSerializer(post)
        message = f"id: {post.pk}번 포스트 조회 성공"
        return api_response(data = postSerializer.data, message = message, status = status.HTTP_200_OK)
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        
        message = f"id: {pk}번 포스트 삭제 성공"
        return api_response(message = message, status = status.HTTP_200_OK)
    