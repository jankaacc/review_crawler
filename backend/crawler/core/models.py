from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """

    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
        editable=False,
        null=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated at"), auto_now=True, editable=False, null=True
    )

    class Meta:
        abstract = True
        ordering = ["created_at"]
