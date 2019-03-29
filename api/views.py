from django.shortcuts import render
from .models import Rank
from rest_framework import viewsets
from .serializers import RankSerializer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from django.db.models import F
from django.db.models import Max

# Create your views here.


class RankViewSet(viewsets.ModelViewSet):
    queryset = Rank.objects.all().order_by('rank')
    serializer_class = RankSerializer

    def create(self, request, *args, **kwargs):
        maxRank = Rank.objects.all().aggregate(Max('rank'))

        for key, value in maxRank.items():
            try1 = value + 1

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        x = Rank.objects.latest('id')
        Rank.objects.filter(rank__gte=x.rank) \
                    .exclude(id=x.id).update(rank=F('rank') + 1)
        if x.rank > try1:
            r = Rank.objects.get(id=x.id)
            r.rank = try1
            r.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        maxRank = Rank.objects.all().aggregate(Max('rank'))

        for key, value in maxRank.items():
            try1 = value + 1

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        x = Rank.objects.get(id=instance.id)
        Rank.objects.filter(rank__gte=x.rank) \
                    .exclude(id=x.id).update(rank=F('rank') + 1)

        if x.rank > try1:
            r = Rank.objects.get(id=x.id)
            r.rank = try1
            r.save()

        return Response(serializer.data)
