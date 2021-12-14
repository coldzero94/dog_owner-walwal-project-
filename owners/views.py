import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, dogs

# Create your views here.

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        Owner.objects.create(
            name=data['owner_name'],
            email=data['owner_email'],
            age=data['owner_age'],
            )
        return JsonResponse({'MESSAGE':'CREATED!!'}, status=201) 

    def get(self, request):
        owners = Owner.objects.all()
        result = []
        for i in owners:
            enddog = list(dogs.objects.values('name', 'age').filter(owner_id=i.id))
            result.append(
                {
                    'owner_name':i.name,
                    'owner_email':i.email,
                    'owner_age':i.age,
                    'owner_match':enddog,
                }
            )
        return JsonResponse({'results':result}, status=200)
      


class DogsView(View):
    def post(self,request):
        data = json.loads(request.body)
        dogs.objects.create(
            name=data['dog_name'],
            age=data['dog_age'],
            owner=Owner.objects.get(name=data['owner_name'])
        )
        return JsonResponse({'MESSAGE':'CREATED!!'}, status=201)
    def get(selft, request):
        dog = dogs.objects.all()
        result = []
        for i in dog:
            result.append(
                {
                    'dog_name':i.name,
                    'dog_age':i.age,
                    'owner_name':i.owner.name,
                }
            )
        return JsonResponse({'results':result}, status=200)
