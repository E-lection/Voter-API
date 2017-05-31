import json
import datetime

from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Voter


def index(request):
    return HttpResponse("Hello, world. You're at the voter index.")


def check_votable(request, voter_id):
    try:
        voter = Voter.objects.get(pk=voter_id)
        return JsonResponse({'voter_exists': True,
                             'used_vote': voter.used_vote})
    except ObjectDoesNotExist:
        return JsonResponse({'voter_exists': False,
                             'used_vote': None})

def get_voter(request, station_id, voter_name, postcode):
        voters = Voter.objects.filter(station=station_id, first_name=voter_name, postcode=postcode)
        voters_json = json.loads(serializers.serialize("json", voters))

        return JsonResponse({'success' : voters.count() > 0,
           'voters' : voters_json })