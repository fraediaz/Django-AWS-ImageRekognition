from django.shortcuts import render
from django.http import HttpResponse
from .models import Consulta
from .formularios import ConsultaForm
from .formulas import detectar_etiquetas
from ImageRecognition.settings import MEDIA_ROOT
from googletrans import Translator
traductor = Translator()


# Create your views here.
def InicioView(r):
    datos = {
        'consultas':Consulta.objects.all(),
        'form':ConsultaForm,
    }
    if r.method == 'POST':
        form = ConsultaForm(r.POST, r.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']
            c = Consulta.objects.create(img=img)
            c.save()
            ruta = (MEDIA_ROOT+str(c.img))
            respuesta = detectar_etiquetas(ruta)
            for x in respuesta:
                print(x['Name'])
                spain   = traductor.translate(x['Name'],dest='es')
                x['Name'] = spain.text
                x['Confidence'] = str(x['Confidence'])[:4]
            datos.update({
                'respuesta':respuesta,
                'img':str(c.img),
            })
        return render(r,'respuesta.html', datos)
    return render(r,'inicio.html', datos)

