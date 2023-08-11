from rest_framework import serializers
from .models import StudentSubjectsScore,Subjects,Schools,Classes,Personnel,SchoolStructure

class PersonnelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = '__all__'

class StudentSubjectsScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSubjectsScore
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'

class SchoolstructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolStructure
        fields = '__all__'