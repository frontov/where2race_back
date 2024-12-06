import json
from event import Event
from date_utils import russiarunning_date_to_timestamp

import requests

request_data = '''
{"EventsLoaderType": 0, "UseTenantBeneficiaryCode": false, "Skip": 0, "Take": 999, "DisciplinesCodes": null,
 "DateFrom": null, "DateTo": null, "StarRaitings": [], "SportSeriesCode": null, "ApprovedStarRaitingOnly": false,
 "RrRecomended": false, "InSportmasterChampionship": false, "NationalMovementOnly": false, "Place": null,
 "OnlyWithOpenRegistration": false, "FromAge": null, "ToAge": null, "ResultsCalculated": false,
 "OnlyWithAdmissions": false, "SortRule": {"Type": 0, "Direction": 1}, "IntoRayRussiaRunnung": false,
 "HidePastEvents": false}'''

kinds = {'run': 'running', 'Велогонка': 'cycling', 'ski-race': 'skiing'}

def get_events():
    headers = {'content-type': 'application/json', }
    response = requests.post('https://russiarunning.com/api/events/list/ru/', headers=headers, data=request_data)
    json = response.text
    return json


def parse_events():
    result = []
    text = get_events()

    items = json.loads(text)
    for item in items['Items']:
        name = item['t']
        slug = item['c']
        link = 'https://russiarunning.com/event/' + item['c']
        description = ''
        kind = [kinds.get(item['dc'], 'other')]
        sub_kind = ''
        date_start = russiarunning_date_to_timestamp(item['d'])
        date_finish = russiarunning_date_to_timestamp(item['et'])
        region = item['address'] if item['address'] is not None else item['p']
        distances = []

        event = Event(name, slug, link, description, kind, sub_kind, date_start, date_finish, region, distances)
        result.append(event)
    return result

