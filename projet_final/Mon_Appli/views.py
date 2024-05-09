from django.shortcuts import render
from .forms import PredictionForm
import pandas as pd
import pickle
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def home_view(request):
    return render(request, "index.html")


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirigez vers l'URL de la page d'accueil après connexion réussie
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Assurez-vous que le modèle est chargé correctement
model = pickle.load(open("/home/yanis/Téléchargements/Projet chef d'oeuvre/api_ai/notebooks/mlruns/0/00b86de19af243328541a503787900f6/artifacts/logistic_regression_pipeline/model.pkl", 'rb'))

@login_required(login_url='/accounts/login/')
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Créez un DataFrame à partir des données du formulaire validées
            data_dict = form.cleaned_data
            data_dict['cons.conf.idx'] = data_dict.pop('cons_conf_idx')
            data_dict['cons.price.idx'] = data_dict.pop('cons_price_idx')
            data = pd.DataFrame([data_dict])
            
            # Faites la prédiction
            pred = model.predict(data)
            result = "Le client va souscrire" if pred[0] == 1 else "Le client ne va pas souscrire"
            return render(request, 'prediction_result.html', {'result': result})
    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form})
