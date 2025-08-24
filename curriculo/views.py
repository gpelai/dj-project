from django.shortcuts import render

# Create your views here.
def curriculo(request):
    return render(
        request=request,
        template_name="curriculo/index.html"
    )