from django.db import models


class List(models.Model):
    pass

class Item(models.Model):
    done = models.BooleanField(default=False)
    text = models.CharField(max_length=200)
    list = models.ForeignKey(
        List,
        on_delete=models.CASCADE,
        related_name="items"
    )

    def toggle_done(self):
        self.done = not self.done
