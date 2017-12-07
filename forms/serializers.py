from rest_framework import serializers
from .models import *

# TODO: create .updates() for all the serialized fields
# TODO: Give delete and create permisions only to request.user that created object

class TextFieldAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFieldAnswers
        fields = ('id','text','user')

class TextFieldSerializer(serializers.ModelSerializer):

    textfieldanswers_set = TextFieldAnswersSerializer(many=True,read_only=True)

    class Meta:
        model = TextField
        fields = ('id','name','identifier', 'textfieldanswers_set')





class DateFieldAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateFieldAnswers
        fields = ('id','date','user')

class DateFieldSerializer(serializers.ModelSerializer):

    datefieldanswers_set = DateFieldAnswersSerializer(many=True,read_only=True)

    class Meta:
        model = DateField
        fields = ('id','name','identifier', 'datefieldanswers_set')







class CheckFieldAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckFieldAnswers
        fields = ('id','check','user')


    # def update(self, instance, validated_data):
    #         # Update the  instance
    #     instance.user = validated_data['check']
    #     instance.check = validated_data['user']
    #     instance.save()

class CheckFieldSerializer(serializers.ModelSerializer):



    checkfieldanswers_set = CheckFieldAnswersSerializer(many=True)

    class Meta:
        model = CheckField
        fields = ('id','name','identifier', 'checkfieldanswers_set')
        # extra_kwargs = {'id': {'read_only': False, 'required': True},'name': {'read_only': False, 'required': True},'identifier': {'read_only': False, 'required': True}}

        # def create(self, validated_data):
        #     # As before.
        #     ...

    # def update(self, instance, validated_data):
    #         # Update the  instance
    #     instance.name = validated_data['name']
    #     instance.identifier = validated_data['identifier']
    #     instance.save()
    #     #
        #     # Delete any detail not included in the request
        #     # owner_ids = [item['owner_id'] for item in validated_data['owners']]
        #     # for owner in cars.owners.all():
        #     #     if owner.id not in owner_ids:
        #     #         owner.delete()
        #
        #     # Create or update owner
        #     # for owner in validated_data['owners']:
        #     #     ownerObj = Owner.objects.get(pk=item['id'])
        #     #     if ownerObje:
        #     #         ownerObj.some_field = item['some_field']
        #     #         ....fields...
        #     #     else:
        #     #         ownerObj = Owner.create(car=instance, **owner)
        #     #     ownerObj.save()
        #
        #     return instance



class ChoiceFieldAnswersSerializer(serializers.ModelSerializer):


    class Meta:
        model = ChoiceFieldAnswers
        fields = ('id', 'choice',)

class ChoiceFieldOptionsSerializer(serializers.ModelSerializer):

    choicefieldanswers_set = ChoiceFieldAnswersSerializer(many=False, read_only=True)
    class Meta:
        model = ChoiceFieldOptions
        fields = ('id','name','choicefieldanswers_set',)

class ChoiceFieldSerializer(serializers.ModelSerializer):


    choicefieldoptions_set = ChoiceFieldOptionsSerializer(many=True)
    class Meta:
        model = ChoiceField
        fields = ('id','name', 'identifier','choicefieldoptions_set')

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    choicefield_set = ChoiceFieldSerializer(many=True)
    checkfield_set = CheckFieldSerializer(many=True)
    datefield_set = DateFieldSerializer(many=True)
    textfield_set = TextFieldSerializer(many=True, read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='forms:survey-detail',
        lookup_field='pk'
    )

    # highlight = serializers.HyperlinkedModelSerializer(view_name='survey-list', many=True, read_only=True)

    class Meta:
        model = Survey
        fields = ('id','url' ,'date_created', 'choicefield_set','checkfield_set' ,'datefield_set','textfield_set')

    def update(self, instance, validated_data):
            # Update the  instance
        print('++++++',validated_data)
        print(instance)

        id_iterator = (id.id for id in instance.checkfield_set.all())
        checkfield_iterator  = (checkfield for checkfield in validated_data['checkfield_set'])
        iterator = zip(id_iterator,checkfield_iterator)



        for id,checkfield in iterator:

            print('isisisisisisisisi',checkfield)


            a = instance.checkfield_set.get(pk=id)
            a.identifier = checkfield['identifier']
            a.name = checkfield['name']
            a.save()

        return instance


# Testing Serializers can delete later

from rest_framework import serializers
from forms.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Snippet.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    survey_set = serializers.HyperlinkedRelatedField(many=True,view_name='forms:survey-detail', read_only=True)

    owner = serializers.ReadOnlyField(source='owner.username')
    # users = serializers.HyperlinkedRelatedField(many=True, view_name='user-list', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'survey_set','owner')

