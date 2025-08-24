from django.shortcuts import render, get_object_or_404
from curriculo.models import Certificados, Experiencias

# Create your views here.
def curriculo(request):
    certificados = Certificados.objects.all()
    experiencias = Experiencias.objects.all()
    context = {
        "certificados": certificados,
        "experiencias": experiencias,
    }
    return render(request, "curriculo/index.html", context)

def curriculo_detail(request, pk):
    certificado = get_object_or_404(Certificados, pk=pk)
    experiencia = get_object_or_404(Experiencias, pk=pk)
    context = {
        "certificado": certificado,
        "experiencia": experiencia,
    }
    return render(request, "curriculo/detail.html", context)