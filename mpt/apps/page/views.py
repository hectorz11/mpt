from django.shortcuts import render_to_response
from django.template import RequestContext
from mpt.apps.page.forms import addLocacionForm,addDepartamentoForm,addPersonaForm,addEquipoForm,addTipoForm,addMovimientoForm
from mpt.apps.page.models import Locacion,Departamento,Persona,Equipo,Tipo,Movimiento
from django.http import HttpResponseRedirect,HttpResponse

def add_locacion_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addLocacionForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save() # Guardamos la informacion
			info = "Guardado satisfactoriamente"
			return HttpResponseRedirect('')
	else:
		form = addLocacionForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addLocacion.html',ctx,context_instance=RequestContext(request))

def add_departamento_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addDepartamentoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			#return HttpResponseRedirect('/departamento/%s/'%add.id)
	else:
		form = addDepartamentoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addDepartamento.html',ctx,context_instance=RequestContext(request))

def add_persona_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addPersonaForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			#return HttpResponseRedirect('/persona/%s'%add.id)
	else:
		form = addPersonaForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addPersona.html',ctx,context_instance=RequestContext(request))

def add_equipo_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addEquipoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			#return HttpResponseRedirect('/equipo/%s'%add.id)
	else:
		form = addEquipoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addEquipo.html',ctx,context_instance=RequestContext(request))

def add_tipo_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addTipoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			#return HttpResponseRedirect('/tipo/%s'%add.id)
	else:
		form = addTipoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addTipo.html',ctx,context_instance=RequestContext(request))

def add_movimiento_view(request):
	info = "iniciando"
	if request.method == "POST":
		form = addMovimientoForm(request.POST,request.FILES)
		if form.is_valid():
			add = form.save(commit=False)
			add.save()
			info = "Guardado satisfactoriamente"
			#return HttpResponseRedirect('/departamento/%s'%add.id)
	else:
		form = addMovimientoForm()
	ctx = {'form':form,'informacion':info}
	return render_to_response('page/addMovimiento.html',ctx,context_instance=RequestContext(request))

def edit_locacion_view(request,id_loc):
	info = "iniciado"
	prod = Locacion.objects.get(pk=id_loc)
	if request.method == "POST":
		form = addLocacionForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('')
	else:
		form = addLocacionForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editLocacion.html',ctx,context_instance=RequestContext(request))

def edit_departamento_view(request,id_dep):
	info = "iniciado"
	prod = Departamento.objects.get(pk=id_dep)
	if request.method == "POST":
		form = addDepartamentoForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('')
	else:
		form = addDepartamentoForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editDepartamento.html',ctx,context_instance=RequestContext(request))

def edit_persona_view(request,id_per):
	info = "iniciado"
	prod = Persona.objects.get(pk=id_per)
	if request.method == "POST":
		form = addPersonaForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('')
	else:
		form = addPersonaForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editPersona.html',ctx,context_instance=RequestContext(request))

def edit_equipo_view(request,id_equi):
	info = "iniciado"
	prod = Equipo.objects.get(pk=id_equi)
	if request.method == "POST":
		form = addEquipoForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('')
	else:
		form = addEquipoForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editEquipo.html',ctx,context_instance=RequestContext(request))

def edit_tipo_view(request,id_tipo):
	info = "iniciado"
	prod = Tipo.objects.get(pk=id_tipo)
	if request.method == "POST":
		form = addTipoForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('')
	else:
		form = addTipoForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editTipo.html',ctx,context_instance=RequestContext(request))

def edit_movimiento_view(request,id_mov):
	info = "iniciado"
	prod = Movimiento.objects.get(pk=id_mov)
	if request.method == "POST":
		form = addMovimientoForm(request.POST,request.FILES,instance=prod)
		if form.is_valid():
			edit_prod = form.save(commit=False)
			edit_prod.status = True
			edit_prod.save() # Guardamos el objeto
			info = "Correcto"
			return HttpResponseRedirect('')
	else:
		form = addMovimientoForm(instance=prod)
	ctx = {'form':form, 'informacion':info}
	return render_to_response('page/editMovimiento.html',ctx,context_instance=RequestContext(request))