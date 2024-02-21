from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

from . import utils


def ping(request):
    serverstatus = True
    dbstatus = False
    if utils.PingMongo():
        dbstatus = True
    message = {"database": dbstatus, "server": serverstatus}

    return JsonResponse(message)


def indexPage(request):
    return render(request, "index.html")


def viewdata(request, collection_name) -> JsonResponse:
    id = request.GET.get("id")

    if id:
        message = utils.fetchdatabyid(collection_name, id)
        return JsonResponse(message, safe=False)

    message = utils.fetchalldata(collection_name)
    return JsonResponse(message, safe=False)


@csrf_exempt
def insertdatatodb(request, collection):
    if request.method == "POST":
        received = json.loads(request.body)

        try:
            utils.insertdata(collection, received)
            return JsonResponse({"message": "Data inserted successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@csrf_exempt
def deletedataindb(request, collection):
    if request.method == "POST":
        received = json.loads(request.body)
        id = received["_id"]
        try:
            res = utils.deletedatabyid(collection, id)
            return JsonResponse(
                {"message": "Data deleted successfully", "response": res}, status=201
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@csrf_exempt
def insertmanydata(request, collection):
    if request.method == "POST":
        received = json.loads(request.body)
        try:
            utils.insertmanydocuments(collection, received)
            return JsonResponse({"message": "Data inserted successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@csrf_exempt
def deletemanydata(request, collection):
    if request.method == "POST":
        received = json.loads(request.body)

        try:
            utils.deletemanydocuments(collection, received)
            return JsonResponse(
                {"message": "Data deleted successfully"}, status=201
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)
