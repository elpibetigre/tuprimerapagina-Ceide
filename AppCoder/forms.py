from django import forms

class Form_Curso(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()
    
class Form_Estudiante(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
   
class Form_Profesor(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)
   
class Form_Entregable(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()

class Form_Equipo(forms.Form):
    nombre = forms.CharField()
    division = forms.CharField()
    fundacion = forms.DateField()
