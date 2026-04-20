import json
from django.http import JsonResponse
from .models import Player
from django.views.decorators.csrf import csrf_exempt   # ✅ add this
# from django.views.decorators.csrf import csrf_exempt
@csrf_exempt   # ✅ add this line
def login_user(request):

    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        key = data.get("key")

        if not username or not key:
            return JsonResponse({
                "status": "error",
                "message": "Missing username or key"
            })

        user = Player.objects.filter(username=username).first()

        if user:
            if user.key == key:
                return JsonResponse({
                    "status": "success",
                    "message": "Login successful"
                })
            else:
                return JsonResponse({
                    "status": "error",
                    "message": "Wrong key"
                })

        else:
            Player.objects.create(username=username, key=key)
            return JsonResponse({
                "status": "success",
                "message": "User created"
            })

    return JsonResponse({
        "status": "error",
        "message": "Only POST method allowed"
    })

# Updating the score
@csrf_exempt
def update_score(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        score = data.get("score")

        try:
            player = Player.objects.get(username=username)

            if score > player.high_score:
                player.high_score = score
                player.save()
                return JsonResponse({
                    "status": "updated",
                    "high_score": player.high_score
                })
            else:
                return JsonResponse({
                    "status": "no_update",
                    "high_score": player.high_score
                })

        except Player.DoesNotExist:
            return JsonResponse({"status": "user_not_found"})

    return JsonResponse({"error": "Only POST allowed"})


@csrf_exempt
def get_score(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")

        try:
            player = Player.objects.get(username=username)
            return JsonResponse({
                "high_score": player.high_score
            })
        except:
            return JsonResponse({"high_score": 0})