from rest_framework import serializers
from accounts.models import User
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 200,write_only = True)
    class Meta:
        model = User
        fields= ["id",'username','email','password']
        read_only_fields=['id']

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
# class UserLoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length = 200,required =True)
#     password = serializers.CharField(max_length = 200,required = True)
