from rest_framework import serializers
from user_data.models import User, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["title", "year", "slug"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","name", "email", "age", "location", "slug", "category"]

    category = CategorySerializer()
    def create(self, validated_data):
        category_data = validated_data.pop('category')
        user = User.objects.create(**validated_data)
        category = Category.objects.create(user=user, **category_data)
        user.category = category
        user.save()
        return user

class OneUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "age", "location", "slug", "category"]