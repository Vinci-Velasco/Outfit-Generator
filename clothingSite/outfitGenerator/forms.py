from django.forms import ModelForm

from . import models

class TopClothingForm(ModelForm):
    class Meta:
        model = models.TopClothing
        fields = ["type", "colour"]

class BottomClothingForm(ModelForm):
    class Meta:
        model = models.BottomClothing
        fields = ["type", "colour"]

class ShoeForm(ModelForm):
    class Meta:
        model = models.Shoe
        fields = ["type", "colour"]