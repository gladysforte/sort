from django.shortcuts import render
from .models import Rank
from rest_framework import viewsets
from .serializers import RankSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all().order_by('rank')
    serializer_class = RankSerializer
    # ranked = Rank.objects.filter(rank__gt=1).exclude(id=5).update(rank=F('rank') + 1)
    # r = rank.objects.values().last()
    # ranked.save()
    # return ranked


# class RankList(APIView):
#     def get(self, request, format=None):
#         ranks = Rank.objects.all().order_by('rank')
#         serializer = RankSerializer(ranks, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = RankSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class RankDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Rank.objects.get(pk=pk)
#         except Rank.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         rank = self.get_object(pk)
#         serializer = RankSerializer(rank)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         rank = self.get_object(pk)
#         serializer = RankSerializer(rank, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
