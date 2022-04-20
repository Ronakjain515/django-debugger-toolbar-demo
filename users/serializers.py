from .models import Students
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
	"""
	Serializer class for students.
	"""
	class Meta:
		model = Students
		fields = "__all__"
