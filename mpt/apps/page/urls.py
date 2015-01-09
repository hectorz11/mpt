from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('mpt.apps.page.views',
	url(r'^add/locacion/$','add_locacion_view',name='vista_agregar_locacion'),
	url(r'^add/departamento/$','add_departamento_view',name='vista_agregar_departamento'),
	url(r'^add/persona/$','add_persona_view',name='vista_agregar_persona'),
	url(r'^add/equipo/$','add_equipo_view',name='vista_agregar_equipo'),
	url(r'^add/tipo/$','add_tipo_view',name='vista_agregar_tipo'),
	url(r'^add/movimiento/$','add_movimiento_view',name='vista_agregar_movimiento'),
	url(r'^edit/locacion/(?P<id_loc>.*)/$','edit_locacion_view',name="vista_editar_locacion"),
	url(r'^edit/departamento/(?P<id_dep>.*)/$','edit_departamento_view',name="vista_editar_departamento"),
	url(r'^edit/persona/(?P<id_per>.*)/$','edit_persona_view',name="vista_editar_persona"),
	url(r'^edit/equipo/(?P<id_equi>.*)/$','edit_equipo_view',name="vista_editar_equipo"),
	url(r'^edit/tipo/(?P<id_tipo>.*)/$','edit_tipo_view',name="vista_editar_tipo"),
	url(r'^edit/movimiento/(?P<id_mov>.*)/$','edit_movimiento_view',name="vista_editar_movimientos"),
)