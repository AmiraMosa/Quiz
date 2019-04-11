from rest_framework import serializers
from .models import Quiz


# Serializers allow complex data such as querysets
# and model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types.

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def create(self, validated_data):
        # validated data will be a quiz object and contains a lot of fields, so in a simple one step we divide its
        # partitions into many and create the data
        return Quiz.objects.create(**validated_data)

'''Below is Serializer also but is built manually'''
#
# class ArticleSerializer(serializers.Serializer):
#
#     title = serializers.CharField(max_length=120)
#
#     description = serializers.CharField()
#
#     body = serializers.CharField()
