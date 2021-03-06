from django import forms
from material import Layout, Fieldset, Row
from django.utils.translation import gettext_lazy as _
from hcap_accounts.models import HealthcareUnitNotifier
from hcap_notifications.models import HealthcareUnitCapacity


class NotifyCapacityForm(forms.ModelForm):
    layout = Layout(
        "notifier",
        "date",
        Fieldset(_("Clinical beds"), Row("clinical_adult_beds", "clinical_pediatric_beds")),
        Fieldset(_("ICU beds"), Row("icu_adult_beds", "icu_pediatric_beds")),
    )

    class Meta:
        model = HealthcareUnitCapacity
        fields = (
            "notifier",
            "date",
            "clinical_adult_beds",
            "clinical_pediatric_beds",
            "icu_adult_beds",
            "icu_pediatric_beds",
        )

    def __init__(self, *args, user, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["notifier"].queryset = HealthcareUnitNotifier.objects.filter(
            user=user, is_authorized=True
        )

    def clean_date(self):
        date = self.cleaned_data.get("date")
        notifier = self.cleaned_data.get("notifier")

        if isinstance(notifier, HealthcareUnitNotifier):
            healthcare_unit = notifier.healthcare_unit
            if healthcare_unit.capacity_notifications.filter(date=date).exists():
                raise forms.ValidationError(_("Notification already exists for this date."))

        return date
