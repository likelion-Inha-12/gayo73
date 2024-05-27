from django.shortcuts import render
from rest_framework.response import Response
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'  # 여기서 'index.html'은 해당 뷰에 사용할 템플릿 파일명입니다.
# Create your views here.
def api_response(data, message, status):
    response = {
        "message":message,
        "data":data
    }
    return Response(response, status=status)

# views.py

