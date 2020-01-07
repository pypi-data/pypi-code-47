from calparse import CalDavParser
from datetime import datetime, timedelta


if __name__ == "__main__":
    today = datetime.today()
    tomorrow = today + timedelta(days=1, hours=23, minutes=59, seconds=59)

    parser = CalDavParser(
        url="https://cloud.intra.lfda.de/remote.php/dav/calendars/intranet.syncuser/lfda-allgemein_shared_by_admin/",
        username="intranet.syncuser",
        password="hieYah0ni5eFae",
        single_calendar=True,
        start_date=today,
        end_date=tomorrow,
    )

    parser.init_client()
    print(parser.get_events_by_date())
