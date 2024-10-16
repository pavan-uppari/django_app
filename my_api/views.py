from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer
from django.core.exceptions import ObjectDoesNotExist

from django.views.decorators.cache import cache_page
from django.core.cache import cache

import logging
logger = logging.getLogger('my_app_logs')

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
        return Response(status=400, data=serializer.errors)

    serializer.save()
    return Response(serializer.data, status=201)

@api_view(['GET', 'DELETE', 'PUT'])
def get_item(request, item_id=None):
    "Fetch single item"

    item = None
    #try to fetch item from cache
    if item := cache.get(item_id):
        logger.info("fetched item from cache")
        pass


    #check item exists or not
    if item is None: #not available in cache
        try:
            item = Item.objects.get(id=item_id)
            cache.set(item_id, item)
            logger.info("added item to cache")
        except ObjectDoesNotExist:
            return Response(status=404, data={"error": "item not found"})

    if request.method == 'DELETE':
        item.delete()
        return Response(status=204, data={"success": f"item {item.name} deleted"})

    if request.method == 'PUT':
        serializer = ItemSerializer(instance=item, data=request.data)
        if not serializer.is_valid():
            return Response(status=400, data=serializer.errors)

        serializer.save()
        return Response(serializer.data)


    serializer = ItemSerializer(item)
    return Response(serializer.data)

    

    