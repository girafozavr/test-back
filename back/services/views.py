import json

from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods

from services.models import Services, Params


@require_http_methods(['GET'])
def get_services(request):
    try:
        services = {
            'services': [{'name': e.name, 'enabled': e.is_enabled, 'started': e.is_started} for e in
                         Services.objects.all()]}
        return JsonResponse(services)
    except ValueError:
        return HttpResponseBadRequest()


@require_http_methods(['POST'])
def start_service(request):
    dto = json.loads(request.body.decode())
    name = dto['name'].strip()
    try:
        Services.objects.filter(name=name).update(launch_action='ST')
        return HttpResponse(status=200)
    except ValueError:
        return HttpResponseBadRequest()


@require_http_methods(['POST'])
def stop_service(request):
    dto = json.loads(request.body.decode())
    name = dto['name'].strip()
    try:
        Services.objects.filter(name=name).update(launch_action='SP')
        return HttpResponse(status=200)
    except ValueError:
        return HttpResponseBadRequest()


@require_http_methods(['POST'])
def restart_service(request):
    dto = json.loads(request.body.decode())
    name = dto['name'].strip()
    try:
        Services.objects.filter(name=name).update(launch_action='RT')
        return HttpResponse(status=200)
    except IntegrityError():
        return print('Bad')


@require_http_methods(['POST'])
def enable_service(request):
    dto = json.loads(request.body.decode())
    name = dto['name'].strip()
    try:
        Services.objects.filter(name=name).update(enable_action='EE')
        return HttpResponse(status=200)
    except ValueError:
        return HttpResponseBadRequest()


@require_http_methods(['POST'])
def disable_service(request):
    dto = json.loads(request.body.decode())
    name = dto['name'].strip()
    try:
        Services.objects.filter(name=name).update(enable_action='DE')
        return HttpResponse(status=200)
    except ValueError:
        return HttpResponseBadRequest()


@require_http_methods(['GET'])
def get_params(request):
    try:
        params = {
            'params': [{'CPU': e.cpu, 'RAM': e.ram, } for e in Params.objects.all()]}
        return JsonResponse(params)
    except ValueError:
        return HttpResponseBadRequest()
