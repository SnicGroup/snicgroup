from presentation.models import Entreprise


def getEntrepriseInfo(*args, **kwargs):
    entreprise = Entreprise.objects.all().first()
    context = {
        'snicgroup': entreprise
    }
    return context
