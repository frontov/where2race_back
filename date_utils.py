from datetime import datetime


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%d.%m-%Y")


def date_to_timestamp(date):
    dtime = datetime.strptime(date, '%d.%m.%Y')
    dtimestamp = dtime.timestamp()
    return int(round(dtimestamp))


def russiarunning_date_to_timestamp(date):
    if date == 0:
        return 0

    dtime = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
    dtimestamp = dtime.timestamp()
    return int(round(dtimestamp))

    # Define a dictionary to map Russian month names to numbers


months = {
    'января': '01',
    'февраля': '02',
    'марта': '03',
    'апреля': '04',
    'мая': '05',
    'июня': '06',
    'июля': '07',
    'августа': '08',
    'сентября': '09',
    'октября': '10',
    'ноября': '11',
    'декабря': '12'
}

# Get today's date
today = datetime.now()


# Function to process a single date
def process_single_date(day, month_name, year=None):
    day = f"{int(day):02}"
    month = months[month_name] if month_name in months else month_name
    date_object = datetime.strptime(f"{day}.{month}.{today.year}", "%d.%m.%Y")

    if year is None:
        if date_object < today:
            year = today.year + 1
        else:
            year = today.year

    return date_to_timestamp(f"{day}.{month}.{year}")


def russian_date_to_timestamp(date_str):
    # Check for intervals
    if '–' in date_str or '-' in date_str or '—' in date_str:
        # Handle intervals
        if '–' in date_str:
            start_str, end_str = date_str.split('–')
        elif '-' in date_str:
            start_str, end_str = date_str.split('-')
        elif '—' in date_str:
            start_str, end_str = date_str.split('—')

        end_day, end_month_name = end_str.strip().split()

        split = start_str.strip().split()
        start_day, start_month_name = split if len(split) == 2 else (start_str, end_month_name)
    else:
        start_day, start_month_name = date_str.split()
        end_day, end_month_name = date_str.strip().split()

    start_date = process_single_date(start_day, start_month_name)
    end_date = process_single_date(end_day, end_month_name)

    return start_date, end_date


def dates_to_timestamp(date_str):
    # Check for intervals
    if '-' in date_str:
        # Handle intervals
        if '-' in date_str:
            start_str, end_str = date_str.split('-')

        end_day, end_month_name, end_year = end_str.strip().split('.')

        split = start_str.strip().split('.')
        if len(split) == 3:
            start_day, start_month_name, start_year = split
        elif len(split) == 2:
            start_day = split[0]
            start_month_name = split[1]
            start_year = end_year
        elif len(split) == 1:
            start_day = split[0]
            start_month_name = end_month_name
            start_year = end_year
    else:
        start_day, start_month_name, start_year = date_str.split(".")
        end_day, end_month_name, end_year = date_str.strip().split(".")

    start_date = process_single_date(start_day, start_month_name, start_year)
    end_date = process_single_date(end_day, end_month_name, end_year)

    return start_date, end_date


