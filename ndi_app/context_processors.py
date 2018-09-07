from django.conf import settings
from ndi_app.models import Activity
from .forms import ContactForm


def activity_base(request):

    context = {
        "all_activities": Activity.objects.all(),
        "form": ContactForm(),
        }
    return context
