import json
from django.conf import settings
from django.views.generic import View
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


# Project homepage.
class DjangocricHomepage(View):
    template_name = "djangoadmin/djangocric/djangocric_homepage.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# The search view to check live score.
class SearchLiveScoreDetail(View):
    template_name = "djangoadmin/djangocric/search_live_score_detail.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        query = self.request.POST["query"]
        if query:
            return render(request, self.template_name, context={"query": query})
        return render(request, self.template_name)


# The search view to check live score.
class SearchMatchSummaryDetail(View):
    template_name = "djangoadmin/djangocric/search_match_summary_detail.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        query = self.request.POST["query"]
        if query:
            return render(request, self.template_name, context={"query": query})
        return render(request, self.template_name)


# The view to access upcoming matches list.
class UpcomingMatchesList(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        data = settings.CRIC.upcoming_matches()
        return JsonResponse(data, safe=False)


# The view to access historical matches list.
class HistoricalMatchesList(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        data = settings.CRIC.historical_matches()
        return JsonResponse(data, safe=False)


# The view to access live score of a specific match.
class LiveScoreDetail(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        data = settings.CRIC.live_score(self.kwargs['match_id'])
        return JsonResponse(data, safe=True)


# The view to access match summary.
class MatchSummaryDetail(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, *args, **kwargs):
        data = settings.CRIC.match_summary(self.kwargs['match_id'])
        return JsonResponse(data, safe=False)


# The view to access information about player.
class AboutPlayerDetail(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL
    
    def get(self, request, *args, **kwargs):
        data = settings.CRIC.about_player(self.kwargs["player_id"])
        return JsonResponse(data, safe=False)
