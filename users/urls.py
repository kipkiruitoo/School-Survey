
from django.urls import path, include
from .views import LoginView, RegisterUsersView, UserViewSet,  UsersProfileViewSet, RolesViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('profile', UsersProfileViewSet)
router.register('users', UserViewSet)
router.register('roles', RolesViewSet )

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    # path('users/', UserListView.as_view(), name="list-users"),
    path('', include(router.urls)),
    # path('', include(router.urls)),
    # path('users/<int:pk>', UserDetailsView.as_view(), name="user-details"),
]


# from django.conf.urls import url, include
# from rest_framework import routers
# from users.views import SchoolViewSet

# router = routers.DefaultRouter()
# router.register(r'users', SchoolViewSet)

# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^auth/', include('rest_auth.urls')),
# ]
