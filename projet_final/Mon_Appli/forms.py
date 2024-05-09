from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms

class PredictionForm(forms.Form):
    JOB_CHOICES = [
        ('admin.', 'Admin'),
        ('blue-collar', 'Blue-collar'),
        ('entrepreneur', 'Entrepreneur'),
        ('housemaid', 'Housemaid'),
        ('management', 'Management'),
        ('retired', 'Retired'),
        ('self-employed', 'Self-employed'),
        ('services', 'Services'),
        ('student', 'Student'),
        ('technician', 'Technician'),
        ('unemployed', 'Unemployed'),
        ('unknown', 'Unknown')
    ]

    MARITAL_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
        ('divorced', 'Divorced'),
        ('unknown', 'Unknown')
    ]

    EDUCATION_CHOICES = [
        ('basic.education', 'Basic Education'),
        ('illiterate', 'Illiterate'),
        ('high.school', 'High School'),
        ('professional.course', 'Professional Course'),
        ('university.degree', 'University Degree'),
        ('unknown', 'Unknown')
    ]

    DEFAULT_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown')
    ]

    HOUSING_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown')
    ]

    LOAN_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unknown', 'Unknown')
    ]

    AGE_GROUP_CHOICES = [
        ('Group 1', 'Group 1'),
        ('Group 2', 'Group 2'),
        ('Group 3', 'Group 3'),
        ('Group 4', 'Group 4'),
        ('Group 5', 'Group 5')
    ]

    PREVIOUS_CHOICES = [(i, str(i)) for i in range(11)]  # Génère des choix de 0 à 10

    # Définir les choix pour 'cons_price_idx'
    CONS_PRICE_IDX_CHOICES = [(-i, str(-i)) for i in range(20, 61)]  # Génère des choix de -20 à -60

    # Définir les choix pour 'cons_conf_idx'
    CONS_CONF_IDX_CHOICES = [(i, str(i)) for i in range(89, 96)]  # Génère des choix de 89 à 95

    duration = forms.IntegerField(
        label='Duration',
        validators=[MinValueValidator(0)]
    )
    campaign = forms.IntegerField(
        label='Campaign',
        validators=[MinValueValidator(0)]
    )
    pdays = forms.IntegerField(
        label='Pdays',
        validators=[MinValueValidator(0)],
        initial=999  # Valeur initiale proposée si le client n'a pas été contacté
    )
    previous = forms.ChoiceField(choices=PREVIOUS_CHOICES, label='Previous')
    cons_price_idx = forms.ChoiceField(choices=CONS_PRICE_IDX_CHOICES, label='Consumer Price Index')
    cons_conf_idx = forms.ChoiceField(choices=CONS_CONF_IDX_CHOICES, label='Consumer Confidence Index')

    # Fields with choices
    job = forms.ChoiceField(choices=JOB_CHOICES, label='Job')
    marital = forms.ChoiceField(choices=MARITAL_CHOICES, label='Marital')
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, label='Education')
    default = forms.ChoiceField(choices=DEFAULT_CHOICES, label='Default')
    housing = forms.ChoiceField(choices=HOUSING_CHOICES, label='Housing')
    loan = forms.ChoiceField(choices=LOAN_CHOICES, label='Loan')
    age_group = forms.ChoiceField(choices=AGE_GROUP_CHOICES, label='Age Group')
