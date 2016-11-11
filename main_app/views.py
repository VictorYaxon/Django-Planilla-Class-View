import time
from django.core.urlresolvers import reverse
from django.urls import reverse_lazy
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView,UpdateView
from django.views.generic.list import ListView
from .forms import IgssForm,SalarioOrdinarioForm,EmpleadoForm,BonificacionForm,RetencionForm,PlanillaForm
from .models import Igss,SalarioOrdinario,Empleado,Bonificacion,Retencion,Planilla

class IgssLista(ListView):
    model = Igss
    template_name='igss.html'

class IgssCrear(CreateView):
    model = Igss
    fields = ['anio','cuota_igss']
    template_name = 'post_igss.html'

    def get_success_url(self):
        return reverse('lista_igss')

class Index(TemplateView):
    """Clase para ver index"""
    template_name = "index.html"

class IgssEliminar(DeleteView):
    model = Igss
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse("lista_igss")

class IgssEditar(UpdateView):
    """docstring for IgssEditar."""
    model = Igss
    fields = ['anio','cuota_igss']
    template_name = "post_igss.html"

    def get_success_url(self):
        return reverse('lista_igss')


class SalarioCrear(CreateView):
    model = SalarioOrdinario
    fields = ['anio','cuota_salario']
    template_name = 'post_salario.html'

    def get_success_url(self):
        return reverse('lista_salario')

class SalarioEliminar(DeleteView):
    model = SalarioOrdinario
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse("lista_salario")

class SalarioEditar(UpdateView):
    """docstring for IgssEditar."""
    model = SalarioOrdinario
    fields = ['anio','cuota_salario']
    template_name = "post_salario.html"

    def get_success_url(self):
        return reverse('lista_salario')

class SalarioLista(ListView):
    model = SalarioOrdinario
    template_name='salario.html'

class EmpleadoCrear(CreateView):
    model = Empleado
    fields = ['nombre','apellido','fechaInicio','estado','fechaInactividad']
    template_name = 'post_empleado.html'

    def get_success_url(self):
        return reverse('lista_empleado')

class EmpleadoEliminar(DeleteView):
    model = Empleado
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse("lista_empleado")

class EmpleadoEditar(UpdateView):
    model = Empleado
    fields = ['nombre','apellido','fechaInicio','estado','fechaInactividad']
    template_name = "post_empleado.html"

    def get_success_url(self):
        return reverse('lista_empleado')

class EmpleadoLista(ListView):
    model = Empleado
    template_name='empleado.html'

class BonificacionCrear(CreateView):
    model = Bonificacion
    fields = ['idEmpleado','BonificacionCuota','fechaBonificacion']
    template_name = 'post_bonificacion.html'

    def get_success_url(self):
        return reverse('lista_bonificacion')

class BonificacionEliminar(DeleteView):
    model = Bonificacion
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse("lista_bonificacion")

class BonificacionEditar(UpdateView):
    model = Bonificacion
    fields = ['idEmpleado','BonificacionCuota','fechaBonificacion']
    template_name = "post_bonificacion.html"

    def get_success_url(self):
        return reverse('lista_bonificacion')

class BonificacionLista(ListView):
    model = Bonificacion
    template_name='bonificacion.html'


class RetencionCrear(CreateView):
    model = Retencion
    fields = ['idEmpleado','RetencionCuota','fechaRetencion']
    template_name = 'post_retencion.html'

    def get_success_url(self):
        return reverse('lista_retencion')

class RetencionEliminar(DeleteView):
    model = Retencion
    template_name = 'confirm_delete.html'
    def get_success_url(self):
        return reverse("lista_retencion")

class RetencionEditar(UpdateView):
    model = Retencion
    fields = ['idEmpleado','RetencionCuota','fechaRetencion']
    template_name = "post_retencion.html"

    def get_success_url(self):
        return reverse('lista_retencion')

class RetencionLista(ListView):
    model = Retencion
    template_name='retencion.html'

#Funcion Para obtener lista de Empleados,IGSS y salario ordinario de la DB
def planilla_ver(request):
    form = PlanillaForm()
    anios = []
    for i in range(1999,int(time.strftime("%Y"))):
        i = i + 1
        anios.append(i)
    mes_seleccionado= request.POST.get('meses')
    anio_seleccionado= request.POST.get('nombres')
    fecha_planilla = str(anio_seleccionado) + "-" + str(mes_seleccionado) + "-28"
    if request.method=="POST":
        anios_Igss = Igss.objects.get(anio=anio_seleccionado)
        anios_Salario = SalarioOrdinario.objects.get(anio=anio_seleccionado)
        empleados_anio = Empleado.objects.filter(fechaInicio__year__lte=anio_seleccionado,estado="Activo")
        for empleado in empleados_anio:
            retencion_planilla = empleado.retencion_set.filter(fechaRetencion__lte=fecha_planilla,idEmpleado=empleado.id).order_by('-fechaRetencion')[:1]
            bonificacion_planilla = empleado.bonificacion_set.filter(fechaBonificacion__lte=fecha_planilla,idEmpleado=empleado.id).order_by('-fechaBonificacion')[:1]
            for item in bonificacion_planilla:
                empleado.bono = item.BonificacionCuota
                empleado.totalSueldo = float(anios_Salario.cuota_salario) + float(empleado.bono)
                empleado.sueldoLiquido = empleado.totalSueldo - float(anios_Igss.cuota_igss)
            for items in retencion_planilla:
                empleado.ret = items.RetencionCuota
                empleado.totalSueldo += float(empleado.ret)
                empleado.sueldoLiquido

        return render(request,'planillatabla.html',
                {'mes_seleccionado':mes_seleccionado,
                'anios_Igss':anios_Igss,'empleados_anio':empleados_anio,
                'anios_Salario':anios_Salario,
                'bonificacion_planilla':bonificacion_planilla,
                'anio_seleccionado':anio_seleccionado,})
    return render(request,'planilla.html',{
    'anios_lista':anios,
    'form':form,'mes_seleccionado':mes_seleccionado,'anio_seleccionado':anio_seleccionado})
