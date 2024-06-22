from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client,Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username']
        
class ProjectViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField() 

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_by', 'created_at', 'updated_at', 'projects'] 

    def get_created_by(self, obj):
        return obj.created_by.username

    def get_projects(self, obj):
        projects = Project.objects.filter(client=obj)
        return ProjectViewSerializer(projects, many=True).data

class ClientSerializerList(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_by', 'created_at', 'updated_at'] 

    def get_created_by(self, obj):
        return obj.created_by.username



class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=True)
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_by', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        users_data = validated_data.pop('users', [])
        project = Project.objects.create(**validated_data)
        project.users.set(users_data)
        return project

    def validate(self, data):
        project_name = data.get('project_name')
        client = data.get('client')
        if Project.objects.filter(project_name=project_name, client=client).exists():
            raise serializers.ValidationError("This project already exists for the client.")
        return data
