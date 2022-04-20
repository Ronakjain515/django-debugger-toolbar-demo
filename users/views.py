from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .serializers import StudentSerializer
from .utils import ResponseInfo
from .models import Students


class GetUsersAPIView(ListAPIView):
	"""
	Class for creating api for getting user list.
	"""
	permission_classes = ()
	authentication_classes = ()
	serializer_class = StudentSerializer

	def __init__(self, **kwargs):
		"""
		Constructor function for formatting the web response to return.
		"""
		self.response_format = ResponseInfo().response
		super(GetUsersAPIView, self).__init__(**kwargs)

	def get_queryset(self):
		"""
		method for returning filtered student queryset
		"""
		return Students.objects.all()

	def get(self, request, *args, **kwargs):
		"""
		GET method for getting paginated courses list.
		"""
		user_serialized_data = super().list(request, *args, **kwargs)
		return Response(user_serialized_data.data)


class AddUsersAPIView(CreateAPIView):
	"""
	Class for creating api for adding user list.
	"""
	permission_classes = ()
	authentication_classes = ()
	serializer_class = StudentSerializer

	def __init__(self, **kwargs):
		"""
		Constructor function for formatting the web response to return.
		"""
		self.response_format = ResponseInfo().response
		super(AddUsersAPIView, self).__init__(**kwargs)

	def post(self, request, *args, **kwargs):
		"""
		GET method for getting paginated courses list.
		"""
		serializer = self.get_serializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			self.response_format["data"] = serializer.data
			self.response_format["message"] = "user added success."
		return Response(self.response_format)
