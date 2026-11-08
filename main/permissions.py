
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsPortfolioOwnerOrEditorOrReadOnly(BasePermission):
    """
    Mengatur hak akses Experience API:

    - Visitor: hanya dapat membaca.
    - Pengguna biasa: membaca dan memberikan star.
    - Editor: membaca, memberikan star, dan mengedit.
    - Superuser: membaca, memberikan star, membuat,
      mengedit, dan menghapus.
    """

    def has_permission(self, request, view):
        # Semua pengguna boleh membaca.
        if request.method in SAFE_METHODS:
            return True

        # Pengguna harus login untuk mengubah data.
        if not request.user or not request.user.is_authenticated:
            return False

        # Superuser memiliki seluruh hak akses.
        if request.user.is_superuser:
            return True

        # Editor hanya boleh mengubah data dengan PUT/PATCH.
        if request.method in ("PUT", "PATCH"):
            return request.user.groups.filter(
                name="Editor"
            ).exists()

        # POST dan DELETE hanya untuk superuser.
        return False

    def has_object_permission(self, request, view, obj):
        # Semua pengguna boleh membaca detail.
        if request.method in SAFE_METHODS:
            return True

        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        # Editor boleh mengedit, tetapi tidak menghapus.
        if request.method in ("PUT", "PATCH"):
            return request.user.groups.filter(
                name="Editor"
            ).exists()

        return False
