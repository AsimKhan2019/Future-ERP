from rest_framework import serializers
from common.models import Product
from notes.models import Category, Note

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'wholesale_price', 'retail_price')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'user')

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'user', 'details', 'category', 'is_active', 'created_at')
