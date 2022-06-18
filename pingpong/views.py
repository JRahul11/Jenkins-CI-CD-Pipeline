from rest_framework.views import APIView
from rest_framework.response import Response

class Welcome(APIView):
    
    def get(self, request):
        return Response("Welcome to Jenkins CI/CD Pipeline by Rahul J")

class PingPong(APIView):

    def post(self, request):
        
        input = request.data['input']
        
        if input == 'ping':
            context = {'output': 'pong'}
        elif input == 'pong':
            context = {'output': 'ping'}
        else:
            context = {'output': 'pongping'}
        return Response(context)