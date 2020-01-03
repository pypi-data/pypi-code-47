from django.shortcuts import render

from meta import OPEN_SOURCE_COMPONENTS


def offline(request):
    return render(request, 'common/offline.html')


def about(request):
    return render(request, "common/about.html", context={"components": OPEN_SOURCE_COMPONENTS})
