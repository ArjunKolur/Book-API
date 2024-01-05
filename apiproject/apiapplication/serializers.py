from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="Enter Book Id")
    title=serializers.CharField(label="Enter the Title")
    author=serializers.CharField(label="Enter the Author")