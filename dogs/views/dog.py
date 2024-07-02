from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView, \
    get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from dogs.models import Dog
from dogs.paginators import DogPaginator
from dogs.permission import IsDogOwner, IsModerator, IsDogPublic
from dogs.serializers.dog import DogSerializer, DogDetailSerializer
from dogs.serializers.breed import DogListSerializer
from users.models import User
from dogs.tasks import send_message_about_like


class DogDetailView(RetrieveAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogDetailSerializer
    permission_classes = [IsAuthenticated, IsDogOwner | IsModerator | IsDogPublic]


class DogListView(ListAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogListSerializer
    permission_classes = [AllowAny] #[IsAuthenticated]
    pagination_class = DogPaginator


class DogCreateView(CreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [AllowAny] #[IsAuthenticated]



class DogUpdateView(UpdateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsAuthenticated, IsDogOwner | IsModerator]



class DogDeleteView(DestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
    permission_classes = [IsDogOwner]


class SetLikeToDog(APIView):
    def post(self, request):
        print(request.data)
        user = get_object_or_404(User, pk=request.data.get("user"))
        dog = get_object_or_404(Dog, pk=request.data.get("dog"))
        if dog.likes.filter(id=user.id).exists():
            return Response({"result": f"The dog {dog} has already a like added by {user.first_name} {user.last_name}"}, status=200)
        send_message_about_like.delay(user.username)
        dog.likes.add(user)
        return Response({"result": f"Like added for {dog} by {user.first_name} {user.last_name}"}, status=200)