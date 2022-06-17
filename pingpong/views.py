from rest_framework.views import APIView
from rest_framework.response import Response

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