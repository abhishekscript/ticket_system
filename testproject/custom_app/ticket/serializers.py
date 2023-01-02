from rest_framework import serializers
from ticket import models

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ticket
        fields = "__all__"



# API Serializers
class TicketAPISerializer(serializers.Serializer):
    title = serializers.CharField(max_length=30)
    client = serializers.IntegerField()
    description = serializers.CharField()
