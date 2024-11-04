import os
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class BaseModelWithImage(models.Model):
    """Modèle de base pour gérer l'image lors de la sauvegarde et de la suppression."""
    image = models.ImageField(upload_to="", null=True, blank=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def get_upload_to(cls, instance, filename):
        """Définit le chemin de téléchargement par défaut, à surcharger dans les sous-classes."""
        return os.path.join("default", filename)

    def save(self, *args, **kwargs):
        # Applique la fonction de chemin de téléchargement spécifique si elle est définie
        if hasattr(self, 'image') and not self.image.field.upload_to:
            self.image.field.upload_to = lambda instance, filename: self.get_upload_to(instance, filename)

        # Supprime l'ancienne image si une nouvelle est enregistrée
        if self.pk:
            try:
                old_instance = self.__class__.objects.get(pk=self.pk)
                if old_instance.image and old_instance.image != self.image:
                    old_image_path = os.path.join(settings.MEDIA_ROOT, old_instance.image.path)
                    if os.path.isfile(old_image_path):
                        os.remove(old_image_path)
            except self.__class__.DoesNotExist:
                pass

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Entreprise(BaseModelWithImage):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    adresse = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    nb_experience = models.IntegerField(default=0, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Entreprise"
        verbose_name_plural = "Entreprise"

    def clean(self):
        if Entreprise.objects.exists() and not self.pk:
            raise ValidationError("Il ne peut y avoir qu'une seule entreprise.")

    @classmethod
    def get_upload_to(cls, instance, filename):
        return os.path.join("logo", filename)


class Objectif(models.Model):
    objectif = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)


class Service(BaseModelWithImage):
    nom = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.nom

    @classmethod
    def get_upload_to(cls, instance, filename):
        return os.path.join("services", filename)


class Team(BaseModelWithImage):
    fullName = models.CharField(max_length=250)
    post = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Equipe"
        verbose_name_plural = "Equipes"

    def __str__(self):
        return self.fullName

    @classmethod
    def get_upload_to(cls, instance, filename):
        return os.path.join("equipes", filename)


class Realisation(BaseModelWithImage):
    nom_projet = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Realisation"
        verbose_name_plural = "Realisations"

    def __str__(self):
        return f"{self.nom_projet}"

    @classmethod
    def get_upload_to(cls, instance, filename):
        return os.path.join("realisation", filename)


# class Statistique(models.Model):
#     nb_projet = models.IntegerField(default=0)
#     nb_client = models.IntegerField(default=0)
#     nb_experience = models.IntegerField(default=0)
#     date_add = models.DateTimeField(auto_now_add=True)
#     date_modif = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         verbose_name = "Statistique"
#         verbose_name_plural = "Statistiques"


class Partenaire(BaseModelWithImage):
    nom = models.CharField(max_length=200)
    sigle = models.CharField(max_length=100, null=True, blank=True)
    adresse = models.CharField(max_length=250, null=True, blank=True)
    pays = models.CharField(max_length=200, null=True, blank=True)
    ville = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Partenaire"
        verbose_name_plural = "Partenaires"

    def __str__(self):
        return f"{self.nom}"

    @classmethod
    def get_upload_to(cls, instance, filename):
        return os.path.join("partenaire", filename)