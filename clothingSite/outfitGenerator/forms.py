from django.forms import ModelForm, HiddenInput

from . import models

class TopClothingForm(ModelForm):
    class Meta:
        model = models.TopClothing
        fields = ["type", "colour", "tint_or_shade", "saturation"]
        labels = {
            "tint_or_shade": "Tint/Shade"
        }

class BottomClothingForm(ModelForm):
    class Meta:
        model = models.BottomClothing
        fields = ["type", "colour", "tint_or_shade", "saturation"]
        labels = {
            "tint_or_shade": "Tint/Shade"
        }

class ShoeForm(ModelForm):
    class Meta:
        model = models.Shoe
        fields = ["type", "colour", "tint_or_shade", "saturation"]
        labels = {
            "tint_or_shade": "Tint/Shade"
        }
