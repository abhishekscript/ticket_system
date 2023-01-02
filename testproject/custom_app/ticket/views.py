from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ticket import dal, serializers

# Create your views here.

class UserTicket(viewsets.ModelViewSet):
    permission_classes = ()
    serializer_class = serializers.TicketSerializer

    @action(methods=['post'], detail=False, url_path='save-ticket', url_name='save_ticket')
    def save_app(self, request):
        request.data['agent'] = request.user
        serializer = serializers.TicketAPISerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        dal.save(
            title=request.data['title'],
            description=request.data['description'],
            client_id=request.data['client'],
            agent_id=request.user.id,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False, url_path='search', url_name='search_ticket')
    def search(self, request):
        request.data['agent'] = request.user
        output = dal.search(
            title=request.data['title'], email=request.data['email']
        )
        print(output, '#data')
        return Response(list(output), status=status.HTTP_200_OK)
