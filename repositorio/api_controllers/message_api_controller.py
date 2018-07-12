from django.views.generic import View
from django.http import HttpResponse, JsonResponse

VERIFY_TOKEN = 'EAADTPsw1mMsBAKZBruRRrEOJ6HSkxeRKiZC0pM1LhUZCmSoBj94GmLBMlYykp5vK82Nb74oVQQzbniwpRduSOTr7oYzZCZB7BATJdIrQnHAAR1ZBsd1HEjyfVjmhuobKDZCFyXAjQzZBlwXTFot49rZCtJfME3y6qN3A0Czo0dtspSEHiu5CnG34H'

class MessageApiController(View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == '2318934571':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')