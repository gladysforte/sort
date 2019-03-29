from rest_framework import serializers
from .models import Rank


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
