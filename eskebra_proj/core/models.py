from django.db import models
from django.utils.translation import gettext as _
# from djmoney.models.fields import MoneyField
from decimal import Decimal

# Create your models here.
class Ads(models.Model):

    CATEGORIES = ['Eletrônicos','Fashion & Acessórios','Jogos','Casa & Lar',
                  'Família & Crianças','Jardim','Saúde & Beleza','Desporto',
                  'Escritório']
    
    STORES = ['Kinda Home', 'Inovia', 'Casacon', 'NCR Angola', 
              'Seaside', 'Soba-store', 'Megáfrica', 'Maxi', 
              'Meu Merkado', 'Okulandas', 'Brechó Angola','Amo']
    
    CATEGORY = []
    STORE = []
    for category, store in zip(CATEGORIES,STORES):
        CATEGORY.append((category,category))
        STORE.append((store,store))

    name  = models.CharField(_("Product Name"), max_length=200) 
    vendor_name  = models.CharField(_("Vendor Name"), max_length=100, choices= STORE, default=1) 
    price = models.DecimalField(_("Product Price"), max_digits=12, decimal_places=2)
    disc_price = models.DecimalField(_("Product Dicount Price"), max_digits=12, decimal_places=2)
    disc_off = models.IntegerField(_("Price Off"), blank=True)
    description = models.TextField(_("Product Description"), blank=True)
    link_vendor = models.URLField(_("Vendor Link"), max_length=2048) #increase length to 2048
    link_image = models.URLField(_("Product Image Link"), max_length=2048) #increase length to 2048
    category = models.CharField(_("Product category"), max_length=200, choices= CATEGORY, default=1)
    created_date = models.DateTimeField(_("Time of Creation"), auto_now_add=True)

    def price_off(self):
        price = Decimal((self.price - self.disc_price)/self.price)* Decimal(100)
        price = round(price,1)
        return int(price)


    def save(self, *args, **kwargs):
        self.disc_off = self.price_off()
        super(Ads, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("Ads")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



class User(models.Model):
    email  = models.EmailField(_("Email"), max_length=254, primary_key=True)
    # created_date = models.DateTimeField(_("Time of Creation"), auto_now_add=False)

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})