from rest_framework import serializers
from .models import Start

class StartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Start
        fields = ('id','fname', 'lname', 'business', 'address', 'state', 'code')