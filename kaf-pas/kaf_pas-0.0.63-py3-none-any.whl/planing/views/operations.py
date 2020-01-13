from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from kaf_pas.planing.models.operations import Operations, OperationsManager


@JsonResponseWithException()
def Operations_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Operations.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=OperationsManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operations_Add(request):
    return JsonResponse(DSResponseAdd(data=Operations.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operations_Update(request):
    return JsonResponse(DSResponseUpdate(data=Operations.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operations_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Operations.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operations_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Operations.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operations_Info(request):
    return JsonResponse(DSResponse(request=request, data=Operations.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Operations_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Operations.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)            
