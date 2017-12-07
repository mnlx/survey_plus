from django.shortcuts import render
from .forms import SurveyForms
from .models import User
from .models import Survey,ChoiceFieldOptions
from .serializers import *
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required


@login_required
def survey_create(request):





    if request.method == 'POST':

        usr = User.objects.get_or_create(pk=request.user.pk)

        print(usr)
        
        dic = request.POST
        sur = Survey(user=  usr[0]  )



        sur.save()

        for i,u in dic.items():
            print(i,u)

            if i.count('text')==1:
                sur.textfield_set.create(identifier=i,name=u) # identifier follows this pattern text_1, date_1, etc...
            elif i.count('date')==1:
                sur.datefield_set.create(identifier=i,name=u)
            elif i.count('check')==1:
                sur.checkfield_set.create(identifier=i,name=u)

            elif i.count('choice')==1 and i.count('[]')!=1:
                print('passed')

                choice_options = sur.choicefield_set.create(identifier=i,name=u)

                options = request.POST.getlist(i+'[]')

                for k in options:

                    choice_options.choicefieldoptions_set.create(name=k)

    form = SurveyForms()





    return render(request, 'forms/survey_create.html', {'form': form})





@csrf_exempt
def form_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = ChoiceFieldOptions.objects.all()
        # serializer = FormSerializer(snippets, many=True)
        # return JsonResponse(serializer.data, safe=False)

def survey_view(request):
    return render(request,'forms/survey_view.html')


from .models import Snippet
from .serializers import SnippetSerializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SurveyList(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class SurveyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def put(self,*args,**kwargs):
    #     return JsonResponse('test')

from rest_framework import viewsets

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer






@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('forms:user-list', request=request, format=format),
        'survey': reverse('forms:survey-list', request=request, format=format)
    })


from rest_framework import renderers
from rest_framework.response import Response

class SnippetsHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
