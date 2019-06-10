from rest_framework import serializers
from case01.models import student

class studentser(serializers.Serializer):
    class Meta:
        model = student
        fielders = "__all__"
    #name = serializers.CharField(label="姓名",max_length=20)
    #age = serializers.IntegerField()
    #score = serializers.IntegerField()