from .models import Registrado
from .forms import RegistradoForm
from django.shortcuts import render

# Create your views here.
def inicio(request):
    formulario = RegistradoForm(request.POST or None)
    if formulario.is_valid():
        formdata = formulario.cleaned_data
        elnombre = formdata.get ("nombre")  
        elemail = formdata.get ("email")
        Registrado.objects.create (nombre=elnombre,email=elemail)
        context = {"miformulario": formulario}
    return render (request, "inicio.html", context )
    
 