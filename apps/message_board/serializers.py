from rest_framework.serializers import ModelSerializer
from .models import MessageBoardModel

class MessageBoardSerializer(ModelSerializer):
    class Meta:
        model = MessageBoardModel
        fields = "__all__"