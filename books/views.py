from django.shortcuts import render, get_object_or_404
from django.utils.autoreload import raise_last_exception
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .models import Book
from .serializers import BookSerializer

# class BookAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookAPIView(APIView):
    def get(self, request):
        books=Book.objects.all()
        serializer_data=BookSerializer(books,many=True).data
        data={
            'status':f"Returned: {len(books)} books",
            'books':serializer_data
        }
        return Response(data)


# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer
class BookDetailAPIView(APIView):
    def get(self,request,pk):
        try:
            book=Book.objects.get(id=pk)
            serializer_data = BookSerializer(book).data
            data={
                'status':'Successfull',
                'book':serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {'status':'Does not exits',
                 'message': 'Kitob topilmadi'},
                status=status.HTTP_404_NOT_FOUND
            )

# class BookDeleteAPIView(generics.RetrieveAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

class BookDeleteAPIView(APIView):
    def delete(self,request,pk):
        try:
            book=Book.objects.get(id=pk)
            book.delete()
            return Response({
                'status':True,
                'message':"Successfully deleted"
            },status=status.HTTP_200_OK)
        except Exception:
            return Response({
                 'status':False,
                 'message': 'Book is not found'},
                status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

class BookUpdateAPIView(APIView):

    def put(self,request,pk):
        book=get_object_or_404(Book.objects.all(),id=pk)
        data=request.data
        serializer=BookSerializer(instance=book,data=data,partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved=serializer.save()
        return Response(
            {
                'status':True,
                'message':f"Book {book_saved} updated successfully"
            }
        )

# class BookUpdateAPIView(APIView):

#     def put(self, request, pk):
#         book=get_object_or_404(Book.objects.all(),id=pk)
#         data=request.data
#         serializer=BookSerializer(instance=book, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             book_saved=serializer.save()
#         return Response(
#             {
#                 'status':True,
#                 'message':f"Book {book_saved} updated successfully"
#             }
#         )

# class BookCreateAPIView(generics.CreateAPIView):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

class BookCreateAPIView(APIView):

    def post(self,request):
        data=request.data
        serializer=BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data={
                'status':f"book save database",
                'books':data
            }
            return Response(data)

# @api_view(['GET'])
# def book_list_view(request,*args,**kwargs):
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True).data
#     return Response(serializer.data)


class BookViewSet(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer