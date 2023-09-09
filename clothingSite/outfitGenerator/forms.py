from django.forms import ModelForm, HiddenInput

from . import models

class TopClothingForm(ModelForm):
    class Meta:
        model = models.TopClothing
        fields = ["type", "colour"]
        widgets = {
            "colour": HiddenInput()
        }

class BottomClothingForm(ModelForm):
    class Meta:
        model = models.BottomClothing
        fields = ["type", "colour"]
        widgets = {
            "colour": HiddenInput()
        }

class ShoeForm(ModelForm):
    class Meta:
        model = models.Shoe
        fields = ["type", "colour"]
        widgets = {
            "colour": HiddenInput()
        }