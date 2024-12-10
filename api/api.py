from datetime import datetime, date

import tinydb
from fastapi import FastAPI, Query
from starlette.middleware.cors import CORSMiddleware
from tinydb import TinyDB
from typing import Optional
from kind_model import to_models

from event_model import EventModel

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kinds = {'skiing': 'Лыжи', 'cycling': 'Велосипед', 'running': 'Бег', 'other': 'Прочее'}
kind_models = to_models(kinds)

db = TinyDB('../db.json')
events_table = tinydb.Query()
events = sorted(db.all(), key=lambda k: k['date_start'])
print(len(events))
event_models = []
for event in events:
    print(event['kind'])
    event_models.append(EventModel(event))

max_date = int(round(datetime.strptime('2044-12-31', '%Y-%m-%d').timestamp()))
current_date = int(round(datetime.strptime(str(date.today()), '%Y-%m-%d').timestamp()))
print(current_date)




# events = db.search((events_table.kind.any(kinds)) & (events_table.date_start >= now.timestamp()) & (
#         events_table.date_start <= date_limit.timestamp()))

@app.get("/events")
async def get_events(start_date: Optional[int] = Query(None),
                     end_date: Optional[int] = Query(None)):
    print(start_date, end_date)
    if not start_date and not end_date:
        start_date = current_date
        end_date = current_date + 30 * 24 * 60 * 60
    else:
        start_date = start_date / 1000 if start_date else current_date
        end_date = end_date / 1000 if end_date else max_date

    print(start_date, end_date)

    result = list(filter(lambda event: start_date <= event.timestamp_date <= end_date, event_models))
    print(len(result))
    return result


@app.get("/kinds")
async def get_kinds():
    return kind_models
