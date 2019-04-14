from .models import SMV
from django import forms


class Smv(forms.ModelForm):
    class Meta:
        model = SMV
        fields = ('operation','complexity_Factor','complexity','s_P_I','stitch_Length','machine','automation','work_Aid',
                  'pick_in_sec','pick_in_frequency','main_Process_in_sec','main_Process_in_frequency',
                  'turn_in_sec','turn_in_frequency','dispose_in_sec','dispose_in_frequency',
                  'personal_Allowance','fatigue_Allowance','delay_Allowance')


SEC = [('Colar Section', 'Colar Section'),
       ('Sleeve Section', 'Sleeve Section'),
       ('Lining Section', 'Lining Section'),
       ('Front Section', 'Front Section'),
       ('Assembly Section', 'Assembly Section'),
]


class Pfm(forms.Form):
    section = forms.ChoiceField(choices=SEC)

v1=[('Men','Men'),('Women','Women')]
v2=[('Jeans','Jeans'),
    ('Shirt','Shirt'),
    ('T-shirt','T-shirt'),
    ]

class Ob(forms.Form):

    category=forms.ChoiceField(choices=v1)
    subcategory=forms.ChoiceField(choices=v2)
    def __init__(self, *args, **kwargs):
        self.data = kwargs.pop('operation')
        CH = [(i, i) for i in self.data]
        super().__init__(*args, **kwargs)
        self.fields['Add Neccessary Operation'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                                      choices=CH)
