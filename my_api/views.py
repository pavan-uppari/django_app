from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from django.core.exceptions import ObjectDoesNotExist

from django.views.decorators.cache import cache_page
from django.core.cache import cache

@api_view(['GET'])
def get_items(request):
    "Fetch all items"

    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def add_item(request):
    "Add one item"

    serializer = ItemSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(status=500, data=serializer.errors)

    serializer.save()
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def get_item(request, item_id=None):
    "Fetch single item"

    #try to fetch item from cache
    if item := cache.get(item_id):
        print('fetched from cache')
        pass


    #check item exists or not
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        cache.set(item_id, item)
        print('added into cache')
        return Response(status=404, data={"error": "item not found"})

    if request.method == 'DELETE':
        item.delete()
        return Response(status=204, data={"success": f"item {item.name} deleted"})

    if request.method == 'PUT':
        serializer = ItemSerializer(instance=item, data=request.data)
        if not serializer.is_valid():
            return Response(status=500, data=serializer.errors)

        serializer.save()
        return Response(serializer.data)


    serializer = ItemSerializer(item)
    return Response(serializer.data)

    

    