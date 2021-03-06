"""rare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rareapi.views import register_user, login_user, CategoryView
from rest_framework import routers
from rareapi.views.comment import CommentView
from rareapi.views.post import PostView
from rareapi.views.subscription import SubscriptionView
from rareapi.views.tag import TagView
from rareapi.views.rareuser import RareUserView
from rareapi.views import MyPostView
from rareapi.views import PostReactionView
from rareapi.views import ReactionView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'posts', PostView, 'post')
router.register(r'myposts', MyPostView, 'mypost')
router.register(r'categories', CategoryView, 'category')
router.register(r'tags', TagView, 'tag')
router.register(r'comments', CommentView, 'comment' )
router.register(r'users', RareUserView, 'rareuser' )
router.register(r'subscriptions', SubscriptionView, 'subscription' )
router.register(r'postreactions', PostReactionView, 'postreaction')
router.register(r'reactions', ReactionView, 'reaction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('', include(router.urls)),
]

    # requests to http://127.0.0.0:8088/register are routed to 'register_user' FN
    # requests to http://127.0.0.0:8088/login are routed to 'login_user' FN
