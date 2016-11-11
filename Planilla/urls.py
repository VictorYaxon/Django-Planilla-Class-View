from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from main_app  import views
from main_app.views import (
    IgssLista,
    IgssEditar,
    IgssEliminar,
    Index,
    Igss,
    IgssCrear,
    SalarioLista,
    SalarioCrear,
    SalarioEditar,
    SalarioEliminar,
    EmpleadoLista,
    EmpleadoCrear,
    EmpleadoEditar,
    EmpleadoEliminar,
    BonificacionLista,
    BonificacionCrear,
    BonificacionEditar,
    BonificacionEliminar,
    RetencionLista,
    RetencionCrear,
    RetencionEditar,
    RetencionEliminar,
)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',Index.as_view() ,name='index'),
    url(r'^eliminar_igss/(?P<pk>\d+)/$', IgssEliminar.as_view(), name='delete_igss'),
    url(r'^editar_igss/(?P<pk>\d+)/$', IgssEditar.as_view(), name='editar_igss'),
    url(r'^igss/create/$',IgssCrear.as_view(),name='create_igss'),
    url(r'^igss/$',IgssLista.as_view(),name='lista_igss'),
    url(r'^eliminar_salario/(?P<pk>\d+)/$', SalarioEliminar.as_view(), name='delete_salario'),
    url(r'^editar_salario/(?P<pk>\d+)/$', SalarioEditar.as_view(), name='editar_salario'),
    url(r'^post_salario/',SalarioCrear.as_view(),name='create_salario'),
    url(r'^salario/$',SalarioLista.as_view(),name='lista_salario'),
    url(r'^eliminar_empleado/(?P<pk>\d+)/$', EmpleadoEliminar.as_view(), name='delete_empleado'),
    url(r'^editar_empleado/(?P<pk>\d+)/$', EmpleadoEditar.as_view(), name='editar_empleado'),
    url(r'^post_empleado/',EmpleadoCrear.as_view(),name='create_empleado'),
    url(r'^empleado/$',EmpleadoLista.as_view(),name='lista_empleado'),
    url(r'^eliminar_bonificacion/(?P<pk>\d+)/$',BonificacionEliminar.as_view(), name='delete_bonificacion'),
    url(r'^editar_bonificacion/(?P<pk>\d+)/$', BonificacionEditar.as_view(), name='editar_bonificacion'),
    url(r'^post_bonificacion/',BonificacionCrear.as_view(),name='create_bonificacion'),
    url(r'^bonificacion/$',BonificacionLista.as_view(),name='lista_bonificacion'),
    url(r'^eliminar_retencion/(?P<pk>\d+)/$',RetencionEliminar.as_view(), name='delete_retencion'),
    url(r'^editar_retencion/(?P<pk>\d+)/$', RetencionEditar.as_view(), name='editar_retencion'),
    url(r'^post_retencion/',RetencionCrear.as_view(),name='create_retencion'),
    url(r'^retencion/$',RetencionLista.as_view(),name='lista_retencion'),
    url(r'^planilla/', views.planilla_ver),
]
