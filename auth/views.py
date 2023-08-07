from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def login_view(request):
    if request.method == 'GET':
        user = request.user
        if user.is_authenticated:
            return Response({'status': 'success', 'msg': f'Hi {user.username}'})
        return Response({'status': 'success', 'msg': 'Please login first'})

    elif request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'status': 'error', 'msg': 'Invalid username or password'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return Response({'status': 'success', 'msg': 'Login success'})
            else:
                return Response({'status': 'error', 'msg': 'Invalid username or password'},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'status': 'error', 'msg': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
