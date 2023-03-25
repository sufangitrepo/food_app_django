
from rest_framework import serializers
from .models import AppUser


class AppUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


    def create(self, validated_data):
        user:AppUser = AppUser.objects.create(email=validated_data['email'], 
                                              first_name=validated_data['first_name'],
                                              last_name=validated_data['last_name'],
                                              is_staff = validated_data['is_staff']
                                              )
        user.set_password(raw_password=validated_data['password'])

        user.save()
        return user


        

class LoginSeriliazer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()
    
    
class UserDetailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
        
    


