from django.shortcuts import render
from AppCoder import forms, models

def inicio(request):
    return render(request, 'AppCoder/inicio.html')


def cursos(request):
    if request.method == 'POST':
        formulario = forms.Form_Curso(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            curso = models.Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, 'AppCoder/cursos.html')
    else:
        formulario = forms.Form_Curso()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/cursos.html", contexto)
    

def profesores(request):
    if request.method == 'POST':
        formulario = forms.Form_Profesor(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesor = models.Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email,"], profesion=informacion["profesion"])
            profesor.save()
            return render(request, 'AppCoder/profesores.html')
    else:
        formulario = forms.Form_Profesor()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/profesores.html", contexto)


def estudiantes(request):
    if request.method == 'POST':
        formulario = forms.Form_Estudiante(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante = models.Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email,"])
            estudiante.save()
            return render(request, 'AppCoder/estudiantes.html')
    else:
        formulario = forms.Form_Estudiante()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/estudiantes.html", contexto)



def entregables(request):
    if request.method == 'POST':
        formulario = forms.Form_Entregable(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            entregable = models.Entregable(nombre=informacion["nombre"], fecha_entrega=informacion["fecha+de+entrega"])
            entregable.save()
            return render(request, 'AppCoder/entregables.html')
    else:
        formulario = forms.Form_Entregable()
        contexto = {"formulario": formulario}
        return render(request, "AppCoder/entregables.html", contexto)


def buscar(request):
  if request.GET['camada']:
    camada = request.GET['camada']
    cursos = models.Curso.objects.filter(camada__icontains=camada)
    return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})
  else:
    respuesta = 'No enviaste datos'
  
  return render(request, 'AppCoder/inicio.html', {'respuesta': respuesta})