from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
@renderer_classes([JSONRenderer])
def plans_list(request):
    plans = [
        {"id": 1, "name": "Free", "price": "0"},
        {"id": 2, "name": "Pro", "price": "10"}
    ]
    return Response(plans)
