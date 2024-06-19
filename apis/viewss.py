from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework.authtoken.models import Token
# Create yofrur views here.
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import *
from .serializer import *



@api_view(['GET'])
def home(request):
    student = Students.objects.all()
    serial = Stundentserial(student,many = True)

    return Response({
        'status':200,
        'payload' : serial.data
    })

@api_view(['POST'])
def post(request):
    data = request.data
    serial  = Stundentserial(data = request.data)
    if not serial.is_valid():
        return Response({
            'status':403,
            'message': 'kya gunda banega re tu'
        })
    serial.save()
    return Response({
     'status':200,
        'payload' : serial.data,
        'message': 'its working'
    })

class useregister(APIView):

    
    def post(self,request):
        serializer = Userserial(data=request.data)
        print((serializer))
        if not serializer.is_valid():
            return Response({
            'status':403,
            'error':serializer.error_messages,
            'message': 'kya gunda banega re tu'
        })
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        token , _ = Token.objects.get_or_create(user=user)

        return Response({
        'status':200,
        'payload' : serializer.data,
        'message': 'its working',
        'token':str(token)
    })
    
    


@api_view(['PATCH'])
def Update(request,id):
    try:
        student = Students.objects.get(id=id)
        serial  = Stundentserial(student , data = request.data,partial= True)
        if not serial.is_valid():
                return Response({
            'status':403,
            'message': 'kya gunda banega re tu'
        })
        serial.save()
        return Response({
        'status':200,
        'payload' : serial.data,
        'message': 'its working'
    })

    except Exception as e:
        return Response({'status':403})
    

 
@api_view(['DELETE'])
def delhi(request,id):
    try:
        student = Students.objects.get(id=id)
        student.delete()
       
        return Response({
        'status':200,
       
        'message': 'its working'
    })

    except Exception as e:
        return Response({'status':403})   