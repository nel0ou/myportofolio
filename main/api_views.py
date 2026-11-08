
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Experience
from .serializers import ExperienceSerializer
from .permissions import IsPortfolioOwnerOrEditorOrReadOnly


@api_view(["GET", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_list_create_api(request):
    """
    GET: Menampilkan daftar Experience dan melakukan pencarian.
    POST: Membuat Experience baru (khusus superuser).
    """

    if request.method == "GET":
        experiences = Experience.objects.all().order_by("-started_at")

        # Pencarian berdasarkan judul.
        title = request.query_params.get("title", "").strip()

        if title:
            experiences = experiences.filter(
                title__icontains=title
            )

        serializer = ExperienceSerializer(
            experiences,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data, status=status.HTTP_200_OK)

    serializer = ExperienceSerializer(
        data=request.data,
        context={"request": request},
    )

    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def experience_detail_api(request, pk):
    """
    GET: Melihat detail Experience.
    PUT: Mengganti seluruh data Experience.
    PATCH: Mengubah sebagian data Experience.
    DELETE: Menghapus Experience (khusus superuser).
    """

    experience = get_object_or_404(Experience, pk=pk)

    if request.method == "GET":
        serializer = ExperienceSerializer(
            experience,
            context={"request": request},
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method in ["PUT", "PATCH"]:
        serializer = ExperienceSerializer(
            experience,
            data=request.data,
            partial=(request.method == "PATCH"),
            context={"request": request},
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    experience.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def experience_star_api(request, pk):
    """
    Memberikan atau membatalkan star pada Experience.
    Akun pemberi star diambil dari request.user.
    """

    experience = get_object_or_404(Experience, pk=pk)

    if experience.starred_by.filter(pk=request.user.pk).exists():
        experience.starred_by.remove(request.user)
        is_starred = False
    else:
        experience.starred_by.add(request.user)
        is_starred = True

    serializer = ExperienceSerializer(
        experience,
        context={"request": request},
    )

    return Response(
        {
            "message": "Star berhasil diperbarui.",
            "is_starred": is_starred,
            "star_count": experience.starred_by.count(),
            "experience": serializer.data,
        },
        status=status.HTTP_200_OK,
    )
