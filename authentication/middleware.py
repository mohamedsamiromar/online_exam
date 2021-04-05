from django.conf import settings
from django.http import HttpResponseRedirect


class Securtyview:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.hi = 'hi'
        if request.get_full_path() not in settings.PUBLIC_URLS:
            if request.user is None or request.user.is_anonymous:
                return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)
