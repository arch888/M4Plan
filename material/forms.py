from django import forms

from .models import *

class Matter(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('item_no','shell_fabric','lining_fabric','trim_fabric','fusing','trims','thread','button','brand_label',
                  'fit_label','size_label','wash_care_label','hangtag','polybag','carton','carton_sticket','pallet',
                  'corner_protection')