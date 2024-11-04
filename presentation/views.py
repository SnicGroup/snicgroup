from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View

from presentation.models import Service, Realisation, Partenaire, Team


def index(request):
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

        if email and subject and message:
            send_mail(subject, message, email, [settings.DEFAULT_FROM_EMAIL], fail_silently=False)
            #send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)

        return redirect('index')


def apropos(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, "presentation/apropos.html", context=context)