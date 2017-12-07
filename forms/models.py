from django.db import models
from django.contrib.auth.models import User
import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

class Survey(models.Model):

    def __init__(self,*args,**kargs):

        super(Survey, self).__init__(*args,**kargs)
        self.date_created = datetime.datetime.now()


    date_created = models.DateTimeField(null=True)
    user = models.ForeignKey(User)

class TextField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)


class TextFieldAnswers(models.Model):

    extends = models.ForeignKey(TextField)
    user = models.IntegerField()

    text = models.TextField(max_length=1000,null=True)


class DateField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)



class DateFieldAnswers(models.Model):
    extends = models.ForeignKey(DateField)
    user = models.IntegerField()

    date = models.DateTimeField(null=True)



class CheckField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)



class CheckFieldAnswers(models.Model):
    extends = models.ForeignKey(CheckField)
    user = models.IntegerField()

    check = models.NullBooleanField(null=True)


class ChoiceField(models.Model):

    extends = models.ForeignKey(Survey)

    identifier = models.CharField(max_length=10,null=False)

    name = models.CharField(max_length=30,null=True)

class ChoiceFieldOptions(models.Model):

    extends = models.ForeignKey(ChoiceField)

    name = models.CharField(max_length=30,null=True)



class ChoiceFieldAnswers(models.Model):
    extends = models.ForeignKey(ChoiceFieldOptions)
    user = models.IntegerField()

    choice = models.NullBooleanField(null=True)

# Testing Serializers


# from django.db import models


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)






