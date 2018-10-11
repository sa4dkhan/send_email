from django import forms
from bootstrap_datepicker_plus import DatePickerInput


class ContactForm(forms.Form):
    subject = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }

          ))
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }))
    sender = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    cc_myself = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(

        )
    )
    schedule = forms.DateField(
            widget=DatePickerInput(
                options={
                    "format": "mm/dd/yyyy",
                    "autoclose": True
                }
            )
        )
