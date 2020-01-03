import dbsettings


class LatestArticleSettings(dbsettings.Group):
    latest_article_is_activated = dbsettings.BooleanValue("Funktion aktivieren?", default=True)
    wp_domain = dbsettings.StringValue("WordPress-Domain", help_text="Ohne abschließenden Slash",
                                       default="https://katharineum-zu-luebeck.de")
    replace_vs_composer_stuff = dbsettings.BooleanValue("VisualComposer-Tags durch regulären Ausdruck entfernen?",
                                                        default=True)


class CurrentEventsSettings(dbsettings.Group):
    current_events_is_activated = dbsettings.BooleanValue("Funktion aktivieren?", default=True)
    calendar_url = dbsettings.StringValue("URL des Kalenders", help_text="Pfad zu einer ICS-Datei",
                                          default="https://nimbus.katharineum.de/remote.php/dav/public-calendars"
                                                  "/owit7yysLB2CYNTq?export")
    events_count = dbsettings.IntegerValue("Anzahl der Termine, die angezeigt werden sollen", default=5)


class MyStatusSettings(dbsettings.Group):
    my_status_is_activated = dbsettings.BooleanValue("Funktion aktivieren?", default=True)


class CurrentExamsSettings(dbsettings.Group):
    current_exams_is_activated = dbsettings.BooleanValue("Funktion aktivieren?", default=True)


latest_article_settings = LatestArticleSettings("Funktion: Letzter Artikel")
current_events_settings = CurrentEventsSettings("Funktion: Aktuelle Termine")
my_status_settings = MyStatusSettings("Funktion: Mein Status")
current_exams_settings = MyStatusSettings("Funktion: Aktuelle Klausuren")
