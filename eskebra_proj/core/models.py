from django.db import models
from django.utils.translation import gettext as _
from djmoney.models.fields import MoneyField


# Create your models here.
class Ads(models.Model):
    CATEGORIES = [('eletrônicos','Eletrônicos'), ('fashion & acessórios','Fashion & Acessórios'), 
                  ('jogos','Jogos'), ('casa & lar','Casa & Lar'),
                  ('família & crianças','Família & Crianças'), ('jardim','Jardim'),
                  ('saúde & beleza','Saúde & Beleza'), ('desporto','Desporto')]

    name  = models.CharField(_("Product Name"), max_length=200) #increase length to 200
    vendor_name  = models.CharField(_("Vendor Name"), max_length=100) #increase length to 100
    price = MoneyField(_("Product Price"), max_digits=12, decimal_places=2, default_currency='AOA')
    disc_price = MoneyField(_("Product Dicount Price"), max_digits=12, decimal_places=2, default_currency='AOA')
    description = models.TextField(_("Product Description"), blank=True)
    link_vendor = models.URLField(_("Vendor Link"), max_length=2048) #increase length to 2048
    link_image = models.URLField(_("Product Image Link"), max_length=2048) #increase length to 2048
    category = models.CharField(_("Product category"), max_length=200, choices= CATEGORIES)
    # created_date = models.DateTimeField(_("Time of Creation"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("Ads")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



class User(models.Model):
    email  = models.EmailField(_("Email"), max_length=254)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})