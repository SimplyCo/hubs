from django.conf import settings


# Template context processor
def get_settings(request):
    return dict(settings=settings)
