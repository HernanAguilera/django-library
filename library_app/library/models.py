from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _

def book_image_path(instance, filename):
    return "books/{}/{}".format(instance.id, filename)

class Book(models.Model):

    name = models.CharField(max_length=128, verbose_name=_("name"))
    summary = models.TextField(verbose_name=_("summary"))
    cover = models.ImageField(upload_to=book_image_path, max_length=100, verbose_name=_("cover"))
    category = models.ManyToManyField("Category", verbose_name=_("category"))
    author = models.ForeignKey("Author", verbose_name=_("author"), on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "book"
        verbose_name_plural = "books"

    def __str__(self):
        return "{} - {}".format(self.name, self.author)

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})


class Category(models.Model):

    description = models.CharField(max_length=128, verbose_name=_("description"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})


class Author(models.Model):

    first_name = models.CharField(max_length=128, verbose_name=_("first name"))
    last_name = models.CharField(max_length=128, verbose_name=_("last name"))

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"pk": self.pk})
