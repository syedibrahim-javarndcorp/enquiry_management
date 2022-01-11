from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ems.models import Ems, Review
from .serializers import EmsSerializer


@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': '/api/enquiry'},
        {'GET': '/api/enquiry/id'},
        {'POST': '/api/enquiry/id/vote'},

    ]
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_ems(request):
    project = Ems.objects.all()
    serializer = EmsSerializer(project, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_enquiry(request, pk):
    project = Ems.objects.get(id=pk)
    serializer = EmsSerializer(project, many=False)
    return Response(serializer.data)


