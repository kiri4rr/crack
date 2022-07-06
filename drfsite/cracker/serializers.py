import io
from abc import ABC

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Cracker
from .models import User


# class CrackerModel:
#    def __init__(self, question, true_answer):
#        self.question = question
#        self.true_answer = true_answer


class CrackerSerializer(serializers.Serializer):
    question_id = serializers.CharField(max_length=255)
    question = serializers.CharField()
    answer_1 = serializers.CharField(max_length=255)
    answer_2 = serializers.CharField(max_length=255)
    answer_3 = serializers.CharField(max_length=255)
    answer_4 = serializers.CharField(max_length=255)
    answer_5 = serializers.CharField(max_length=255)
    true_answer = serializers.CharField(max_length=255)
    picture_id = serializers.IntegerField()

    def create(self, validated_data):
        return Cracker.objects.create(**validated_data)


class UserSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    login = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return User.objects.create(**validated_data)



# def encode():
#    model = CrackerModel('8+8=?', 'true_answer: 16')
#    model_sr = CrackerSerializer(model)
#    print(model_sr.data, type(model_sr.data), sep='/n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)
#
# def decode():
#    stream = io.BytesIO(b'{"question":"8+8=?","true_answer":"true_answer: 16"}')
#    data = JSONParser().parse(stream)
#    serializer = CrackerSerializer(data=data)
#    serializer.is_valid()
#    print(serializer.validated_data)


# class Meta:
#    model = Cracker
#    fields = ('question', 'true_answer')
