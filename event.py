kind_dict = {'skiing': 'Лыжи', 'cycling': 'Велосипед', 'running': 'Бег', 'other': 'Прочее'}


class Event:
    name = ''
    slug = '/'
    link = ''
    description = ''
    kind = []
    kind_rus = []
    sub_kind = ''
    date_start = None
    date_finish = None
    region = None
    distances = []

    def set_kind(self, kind):
        self.kind = kind
        self.kind_rus = []
        if kind:
            for k in kind:
                self.kind_rus.append(kind_dict.get(k, 'Прочее'))

    def __init__(self, name, slug, link, description, kind, sub_kind, date_start, date_finish, region, distances):
        self.name = name
        self.slug = slug
        self.link = link
        self.description = description
        self.set_kind(kind)
        self.sub_kind = sub_kind
        self.date_start = date_start
        self.date_finish = date_finish
        self.region = region
        self.distances = distances
