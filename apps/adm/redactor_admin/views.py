import logging
import json

from apps.hubsapp.models import PostImage
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

logger = logging.getLogger(__name__)


def is_admin(user):
    if user.is_authenticated():
        return user.is_staff
    else:
        return False


@csrf_exempt
@login_required
@user_passes_test(is_admin)
def upload_image(request):
    error = 'Unknown'
    if request.method == 'POST':
        if request.FILES:
            first_file = None
            for filename, the_file in request.FILES.iteritems():
                if not first_file:
                    first_file = the_file
            image_model = PostImage(image=first_file)
            image_model.save()
            return HttpResponse(json.dumps({'filelink': image_model.image.url}), content_type='application/json')
        else:
            error = 'no files found in request'
            logger.error(error)
    else:
        error = 'not POST'
        logger.error(error)

    return HttpResponse(json.dumps({'error': error}), content_type='application/json', status=500)
