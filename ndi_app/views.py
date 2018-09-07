from django.shortcuts import render, get_object_or_404
from .models import News, Activity, WorksInActivity, Slider, MainSlide, DownloadFiles, ServicesOfExpertise
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def contact_send(request):
    from_email = settings.EMAIL_HOST_USER
    to_email = [from_email, '11@gmail.com ']

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            theme = form.cleaned_data['theme']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_message = "{},\n {},\n {},\n {},\n {},\n".format(message, phone, name, theme, email)

            try:
                send_mail(name, send_message, from_email, to_email)
            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:

        form = ContactForm()


def main_page(request):
    all_slides = Slider.objects.all()
    all_news = News.objects.all()
    all_main_slide = MainSlide.objects.all()

    context = {
        'all_main_slide': all_main_slide,
        'all_slides': all_slides,
        'all_news': all_news,

    }

    return render(request, 'ndi_app/main.html', context)


def news_view(request):
    all_news = News.objects.all()
    context = {
        'all_news': all_news,
    }
    return render(request, 'ndi_app/news.html', context)


def activity_view(request, activity_slug=None):
    selected_activity = None
    activity_works = None
    files_of_expertise = None
    service_of_expertise = None
    activities = Activity.objects.all()
    if activity_slug:
        selected_activity = get_object_or_404(Activity, slug=activity_slug)
        activity_works = WorksInActivity.objects.filter(activity=selected_activity)
        files_of_expertise = DownloadFiles.objects.filter(activity=selected_activity)
        service_of_expertise = ServicesOfExpertise.objects.filter(activity=selected_activity)
    context = {
        'selected_activity': selected_activity,
        'activities': activities,
        'activity_works': activity_works,
        'files_of_expertise': files_of_expertise,
        'service_of_expertise': service_of_expertise,
    }
    return render(request, 'ndi_app/restoration.html', context)


def base_view(request):
    all_activity = Activity.objects.all()
    return render(request, "ndi_app/base.html", {"all_activity": all_activity})


def contacts_view(request):
    return render(request, 'ndi_app/contacts.html')
