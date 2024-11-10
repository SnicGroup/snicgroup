from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils import timezone
from user_agents import parse
from django.views import View

from presentation.models import Service, Realisation, Partenaire, Team, VisitePlateforme


def nombre_visite_site(request):
    user_agent = parse(request.META['HTTP_USER_AGENT'])
    device_type = 'Desktop' if user_agent.is_pc else 'Mobile' if user_agent.is_mobile else 'Tablet'

    today = timezone.now().date()
    daily_view, created = VisitePlateforme.objects.get_or_create(date=today, device_type=device_type)

    if not created:
        daily_view.view_count += 1
        daily_view.save()


def index(request):
    nombre_visite_site(request)
    patenaires = Partenaire.objects.all()
    context = {
        'partenaires': patenaires
    }
    return render(request, "presentation/index.html", context=context)


def service(request):
    services = Service.objects.all()
    realisations = Realisation.objects.all()
    context = {
        'services': services,
        'realisations': realisations
    }
    return render(request, 'presentation/service.html', context=context)


def temoignage(request):
    return render(request, 'presentation/temoignage.html')


class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "presentation/contact.html")

    def post(self, request, *args, **kwargs):
        snic_email = "entreprise.snicgroup@gmail.com"
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if email and message:
            send_mail(subject, message, email, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
            #send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

        return redirect('index')


def apropos(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, "presentation/apropos.html", context=context)