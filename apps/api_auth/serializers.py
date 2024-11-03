# api_auth/serializers.py
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    # def validate(self, data):
    #     username = data.get('username')
    #     password = data.get('password')
    #     if data['username'] == data['password']:
    #         raise serializers.ValidationError("Both username and password are required.")
    #     return data
