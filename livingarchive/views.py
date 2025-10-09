import json, os
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Store the JSON file beside this views.py (keeps it app-local)
ANNOT_PATH = os.path.join(os.path.dirname(__file__), "annotations.json")

def _load():
    if os.path.exists(ANNOT_PATH):
        with open(ANNOT_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"type": "FeatureCollection", "features": []}

def _save(data):
    with open(ANNOT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def annotations_geojson(request):
    return JsonResponse(_load())

@csrf_exempt   # simplest way to avoid CSRF issues during local dev
def annotations_post(request):
    if request.method != "POST":
        return HttpResponseBadRequest("POST only")
    try:
        body = json.loads(request.body.decode("utf-8"))
    except Exception:
        return HttpResponseBadRequest("Invalid JSON")
    data = _load()
    data["features"].append(body)
    _save(data)
    return JsonResponse({"ok": True})

def cesium_view(request):
    return render(request, "cesium/tileset_annotations.html")
