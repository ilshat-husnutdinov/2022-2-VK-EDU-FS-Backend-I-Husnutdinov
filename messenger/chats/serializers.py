from rest_framework import serializers
from chats.models import Chat, Message, ChatMember
from users.serializers import AppUserSerializer

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'

class ChatMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMember
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):


    class Meta:
        model = Message
        fields = ('id', 'chat', 'sent_from', 'text', 'sending_time', 'is_read')

