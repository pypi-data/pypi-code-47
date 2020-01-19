from django.urls import re_path
from djangocric import views


# Create your appname
app_name = "djangocric"


urlpatterns = [
    re_path(r"^$", views.DjangocricHomepage.as_view(), name="djangocric_homepage"),
    re_path(r"^search-live-score/$", views.SearchLiveScoreDetail.as_view(), name="search_live_score"),
    re_path(r"^search-match-summary/$", views.SearchMatchSummaryDetail.as_view(), name="search_match_summary"),
    re_path(r"^upcoming-matches/$", views.UpcomingMatchesList.as_view(), name="upcoming_matches"),
    re_path(r"^historical-matches/$", views.HistoricalMatchesList.as_view(), name="historical_matches"),
    re_path(r"^live-score/(?P<match_id>[\d+]+)/$", views.LiveScoreDetail.as_view(), name="live_score_detail"),
    re_path(r"^match-summary/(?P<match_id>[\d+]+)/$", views.MatchSummaryDetail.as_view(), name="match_summary_detail"),
    re_path(r"^about-player/(?P<player_id>[\d+]+)/$", views.AboutPlayerDetail.as_view(), name="about_player_detail"),
]