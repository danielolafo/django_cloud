from rest_framework.views import APIView
from django.http import HttpResponse

class Stock(APIView):

    def get(self, request):
        return HttpResponse('MESSAGE')