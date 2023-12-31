from django.http import JsonResponse
import datetime


def get_info(request):
    # get the slack_name and track from the request
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    # get the current day of the week
    current_day = datetime.datetime.utcnow().strftime("%A")

    # get the current UTC time with validation of +/-2 
    utc_time = datetime.datetime.utcnow().isoformat() + "Z"
    

    # get the github file url and repo url
    github_file_url = "https://github.com/AAEO04/hngx/blob/main/views.py"
    github_repo_url = "https://github.com/AAEO04/hngx"

    # creating a dictionary with the required information
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    # return a JsonResponse with dicitionary
    return JsonResponse(response_data, safe=False)

