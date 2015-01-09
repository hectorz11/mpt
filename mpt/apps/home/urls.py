from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('mpt.apps.home.views',
	url(r'^$','index_view',name='vista_principal'),
	url(r'^login/$','login_view',name='vista_login'),
	url(r'^logout/$','logout_view',name='vista_logout'),
	url(r'^registro/$','register_view',name='vista_registro'),
	url(r'^equipos/page/(?P<pagina>.*)/$','equipos_view',name='vista_equipos'),
	url(r'^personas/page/(?P<pagina>.*)/$','personas_view',name='vista_personas'),
	url(r'^departamentos/page/(?P<pagina>.*)/$','departamentos_view',name='vista_departamentos'),
	url(r'^locaciones/page/(?P<pagina>.*)/$','locaciones_view',name='vista_locaciones'),
	url(r'^tipos/page/(?P<pagina>.*)/$','tipos_view',name='vista_tipos'),
	url(r'^movimientos/(?P<pagina>.*)/$','movimientos_view',name='vista_movimientos'),
	url(r'^locacion/(?P<id_loc>.*)/$', 'singleLocacion_view', name = 'vista_single_locacion'),
)