from django.urls import reverse
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Changes(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название версии")
    description = models.TextField(verbose_name="Описание")
    product_id = models.ForeignKey("Product", models.CASCADE, null=False, verbose_name="Версия продукта", unique=True)

    class Meta:
        verbose_name = "Изменение"
        verbose_name_plural = "Изменения"

    def get_absolute_url(self):
        return reverse("ch_detail_url", kwargs={"change_id": self.pk})


def upload_location_product(instatnce, filename):
    file_path = '{title}/{filename}'.format(title=str(instatnce.title), filename=filename)
    return file_path


class Product(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Уникальное название")
    product_path = models.FileField(verbose_name="Программа", null=False, blank=False,
                                    upload_to=upload_location_product)

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'

    def __str__(self):
        return str(self.title)

@receiver(post_delete, sender=Product)
def submission_delete_projects(sender, instance, **kwargs):
    instance.product_path.delete(False)
