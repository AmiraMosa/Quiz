from rest_framework import serializers
from .models import *


# Serializers allow complex data such as querysets
# and model instances to be converted to native Python datatypes
# that can then be easily rendered into JSON, XML or other content types.
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        # fields = '__all__'
        exclude = ['quiz_id'] #yb2a kda hyarg3 kol 7aga ma3da hewar al quizzes id ally mo4arka m3aya fe nfs al question

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

    def create(self, validated_data):
        # validated data will be a quiz object and contains a lot of fields, so in a simple one step we divide its
        # partitions into many and create the data
        return Quiz.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # m3naha lw mal2t4 da 5las 5od al value el 2dema b2a

        instance.title = validated_data.get('title', instance.title)

        instance.programming_language = validated_data.get('programming_language', instance.programming_language)

        instance.skill_type = validated_data.get('skill_type', instance.skill_type)
        instance.no_of_questions = validated_data.get('no_of_questions', instance.no_of_questions)
        instance.expected_duration = validated_data.get('expected_duration', instance.expected_duration)
        instance.score = validated_data.get('score', instance.score)

        instance.save()

        return instance


'''Below is Serializer also but is built manually'''
#
# class ArticleSerializer(serializers.Serializer):
#
#     title = serializers.CharField(max_length=120)
#
#     description = serializers.CharField()
#
#     body = serializers.CharField()
