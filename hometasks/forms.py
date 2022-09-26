from django import forms

from .models import HomeTask


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].empty_label = ''

    class Meta:
        model = HomeTask
        fields = ('date', 'subject', 'homework', 'next_controlwork')
        widgets = {
            'date': forms.SelectDateWidget(attrs={'class': 'p-3 rounded-md bg-blue-100 shadow-xl shadow-blue-100 text-blue-500 w-full mb-5 transition focus:shadow-blue-100/50 focus:outline-none'}),
            'subject': forms.Select(attrs={'class': 'p-3 rounded-md bg-blue-100 shadow-xl shadow-blue-100 text-blue-500 w-full mb-5 transition focus:shadow-blue-100/50 focus:outline-none'}),
            'homework': forms.TextInput(attrs={'class': 'p-3 rounded-md bg-blue-100 shadow-xl shadow-blue-100 text-blue-500 w-full mb-5 transition focus:shadow-blue-100/50 focus:outline-none'}),
            'next_controlwork': forms.NumberInput(attrs={'class': 'p-3 rounded-md bg-blue-100 shadow-xl shadow-blue-100 text-blue-500 w-full mb-5 transition focus:shadow-blue-100/50 focus:outline-none', 'min': '0'})
        }