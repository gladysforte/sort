from rest_framework import serializers
from .models import Rank
from django.db.models import F
from .utils import insertion_sort


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = (
            'id',
            'name',
            'rank',
            'created_at',
            'updated_at',
            'deleted_at'
        )

        read_only_fields = (
            'id', 'created_at', 'updated_at', 'deleted_at'
        )

        def create(self, validated_data):
            ranked = Rank.objects.created(**validated_data)
            last = Rank.objects.last()
            r2 = Rank.objects.values_list('rank')
            # ranked = Rank.objects.filter(rank__gt=1).exclude(id=5).update(rank=F('rank') + 1)
            # r = rank.objects.values().last()

            if last.id > ranked.rank:
                Rank.objects.create(rank=last.id + 1)
            elif ranked.rank < last.id:
                # Rank.objects.filter(rank__gt=1).exclude(id=6)
                # ranked = Rank.objects.filter(rank__gt=1).exclude(id=5).update(rank=F('rank') + 1)
                ranked.rank = insertion_sort(r2)

            ranked.save()
            return ranked
