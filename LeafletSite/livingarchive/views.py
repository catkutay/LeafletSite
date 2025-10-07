import json, os
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render

ANNOT_PATH = os.path.join(os.path.dirname(__file__), "annotations.json")

def _load():
    if os.path.exists(ANNOT_PATH):
        with open(ANNOT_PATH) as f: return json.load(f)
    return {"type":"FeatureCollection","features":[]}

def _save(data):
    with open(ANNOT_PATH, "w") as f: json.dump(data, f)

def annotations_geojson(request):
    return JsonResponse(_load())

def annotations_post(request):
    if request.method != "POST": return HttpResponseBadRequest("POST only")
    body = json.loads(request.body)
    data = _load()
    data["features"].append(body)
    _save(data)
    return JsonResponse({"ok": True})

def cesium_view(request):
    return render(request, "cesium/tileset_annotations.html")
