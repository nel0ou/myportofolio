from rest_framework import serializers
from .models import Experience, Project


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ['id']


class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['id', 'starred_by', 'star_count']

    def get_star_count(self, obj):
        return obj.starred_by.count()
