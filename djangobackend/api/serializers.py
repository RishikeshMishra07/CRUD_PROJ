from rest_framework import serializers
from.models import students
class studentsserializer(serializers.ModelSerializer):
    class Meta:
        model=students
        fields=['id','stuid', 'stuname','stuemail','stuage']


