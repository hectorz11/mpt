from django.shortcuts import render_to_response
from django.template import RequestContext
from mpt.apps.page.models import Equipo,Persona,Departamento,Locacion,Tipo,Movimiento
from mpt.apps.home.forms import LoginForm,RegisterForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.contrib.auth.decorators import login_required

def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def equipos_view(request,pagina):
	if request.method=="POST":
		if "equipo_id" in request.POST:
			try:
				id_equipo = request.POST['equipo_id']
				p = Equipo.objects.get(pk=id_equipo)
				mensaje = {"control":"True","equipo_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"control":"False"}
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_equi = Equipo.objects.filter(control=True) # Select * from ventas_productos where control = True
	paginator = Paginator(lista_equi,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		equipos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		equipos = paginator.page(paginator.num_pages)
	ctx = {'equipos':equipos}
	return render_to_response('home/equipos.html',ctx,context_instance=RequestContext(request))

def personas_view(request,pagina):
	if request.method=="POST":
		if "persona_id" in request.POST:
			try:
				id_persona = request.POST['persona_id']
				p = Persona.objects.get(pk=id_persona)
				mensaje = {"control":"True","persona_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"control":"False"}
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_prod = Persona.objects.filter(control=True) # Select * from ventas_productos where control = True
	paginator = Paginator(lista_prod,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		personas = paginator.page(page)
	except (EmptyPage,InvalidPage):
		personas = paginator.page(paginator.num_pages)
	ctx = {'personas':personas}
	return render_to_response('home/personas.html',ctx,context_instance=RequestContext(request))

def departamentos_view(request,pagina):
	if request.method=="POST":
		if "departamento_id" in request.POST:
			try:
				id_departamento = request.POST['departamento_id']
				p = Departamento.objects.get(pk=id_departamento)
				mensaje = {"control":"True","departamento_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"control":"False"}
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_depto = Departamento.objects.filter(control=True) # Select * from ventas_productos where control = True
	paginator = Paginator(lista_depto,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		departamentos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		departamentos = paginator.page(paginator.num_pages)
	ctx = {'departamentos':departamentos}
	return render_to_response('home/departamentos.html',ctx,context_instance=RequestContext(request))

def locaciones_view(request,pagina):
	if request.method=="POST":
		if "locacion_id" in request.POST:
			try:
				id_locacion = request.POST['locacion_id']
				p = Locacion.objects.get(pk=id_locacion)
				mensaje = {"control":"True","locacion_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"control":"False"}
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_loc = Locacion.objects.filter(control=True) # Select * from ventas_productos where control = True
	paginator = Paginator(lista_loc,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		locaciones = paginator.page(page)
	except (EmptyPage,InvalidPage):
		locaciones = paginator.page(paginator.num_pages)
	ctx = {'locaciones':locaciones}
	return render_to_response('home/locaciones.html',ctx,context_instance=RequestContext(request))

def tipos_view(request,pagina):
	if request.method=="POST":
		if "tipo_id" in request.POST:
			try:
				id_tipo = request.POST['tipo_id']
				p = Tipo.objects.get(pk=id_tipo)
				mensaje = {"control":"True","tipo_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"control":"False"}
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_tipo = Tipo.objects.filter(control=True) # Select * from ventas_productos where control = True
	paginator = Paginator(lista_tipo,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		tipos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		tipos = paginator.page(paginator.num_pages)
	ctx = {'tipos':tipos}
	return render_to_response('home/tipos.html',ctx,context_instance=RequestContext(request))

def movimientos_view(request,pagina):
	if request.method=="POST":
		if "movimiento_id" in request.POST:
			try:
				id_movimiento = request.POST['movimiento_id']
				p = Movimiento.objects.get(pk=id_movimiento)
				mensaje = {"control":"True","movimiento_id":p.id}
				p.delete() # Elinamos objeto de la base de datos
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
			except:
				mensaje = {"control":"False"}
				#return HttpResponse(simplejson.dumps(mensaje),mimetype='application/json')
	lista_mov = Movimiento.objects.filter(control=True) # Select * from ventas_productos where control = True
	paginator = Paginator(lista_mov,5) # Cuantos productos quieres por pagina? = 3
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		movimientos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		movimientos = paginator.page(paginator.num_pages)
	ctx = {'movimientos':movimientos}
	return render_to_response('home/movimientos.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				next = request.POST['next']
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuario = authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect(next)
				else:
					mensaje = "usuario y/o password incorrecto"
		next = request.REQUEST.get('next')
		form = LoginForm()
		ctx = {'form':form,'mensaje':mensaje,'next':next}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			nombres = form.cleaned_data['nombres']
			apellidos = form.cleaned_data['apellidos']
			username = form.cleaned_data['username']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(nombre=nombres,apellidos=apellidos,username=username,password=password_one)
			u.save() # Guardar el objeto
			return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return 	render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))

def singleLocacion_view(request,id_loc):
	prod = Locacion.objects.get(id=id_loc)
	#cats = prod.categorias.all() # Obteniendo la(s) categoria(s) del producto encontrado
	ctx = {'producto':prod } #,'categorias':cats}
	return render_to_response('home/singleLocacion.html', ctx, context_instance= RequestContext(request))