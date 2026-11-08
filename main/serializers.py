
from rest_framework import serializers
from django.utils.html import strip_tags

from .models import Experience, Project


class ExperienceSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = [
            'id',
            'title',
            'description',
            'category',
            'started_at',
            'ended_at',
            'star_count',
            'is_starred',
        ]
        read_only_fields = [
            'id',
            'star_count',
            'is_starred',
        ]

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get('request')

        if request and request.user.is_authenticated:
            return obj.starred_by.filter(
                pk=request.user.pk
            ).exists()

        return False

    def validate_title(self, value):
        cleaned_value = strip_tags(value).strip()

        if not cleaned_value:
            raise serializers.ValidationError(
                "Title tidak boleh kosong."
            )

        return cleaned_value

    def validate_description(self, value):
        cleaned_value = strip_tags(value).strip()

        if not cleaned_value:
            raise serializers.ValidationError(
                "Description tidak boleh kosong."
            )

        return cleaned_value


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'tech_stack',
            'link_url',
            'star_count',
        ]
        read_only_fields = ['id', 'star_count']

    def get_star_count(self, obj):
        return obj.starred_by.count()
