from django import forms



from .models import *

class AHPForm(forms.ModelForm):

    gaji_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control '}))
    gaji_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    gaji_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    umur_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    umur_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    umur_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    luas_rumah_a=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    luas_rumah_b=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    luas_rumah_c=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Alternatif
        fields = ('gaji','umur','luas')
        widgets = {

            'gaji':forms.HiddenInput(),
            'umur':forms.HiddenInput(),
            'luas':forms.HiddenInput(),
        }
class AHPKriteriaForm(forms.ModelForm):
    PLANNING_CHOICES_WITH_TITLES = (
        ('1', 'Sama Penting (1)'),
        ('2', 'Diantara Sama dan Cukup Penting (2)'),
        ('3', 'Cukup Penting (3)'),
        ('4', 'Diantara Cukup dan Lebih Penting (4)'),
        ('5', 'Lebih Penting (5)'),
        ('6', 'Diantara Lebih dan Sangat Lebih Penting (6)'),
        ('7', 'Sangat Lebih Penting (7)'),
        ('8', 'Diantara Sangat dan Mutlak Lebih Penting (8)'),
        ('9', 'Mutlak Lebih Penting (9)'),
    )


    kriteria_umur_gaji=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kriteria_umur_luas=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    kriteria_gaji_luas=forms.ChoiceField(
        required=True, choices=PLANNING_CHOICES_WITH_TITLES,widget=forms.Select(attrs={'class':'form-control '}))
    class Meta:
        model = Alternatif
        fields = ('kri',)
        widgets = {
            'kri':forms.HiddenInput(),
        }

