from django.http import JsonResponse


def get_routes(request):
    routes = [
        {'GET': '/api/index'},
        {'GET': '/api/enquiry/id'},
        {'POST': '/api/enquiry/id/vote'},

    ]
    return JsonResponse(routes, safe=False)
