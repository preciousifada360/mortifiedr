# Core Django imports.
from django.views import View
from blog import views
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView

# Blog application imports.
from blog.views.blog.article_views import (
    ArticleListView,
    ArticleDetailView,
    ArticleSearchListView,
    TagArticlesListView,
    About,
)

from blog.views.blog.category_views import (
    CategoryArticlesListView,
    CategoriesListView,
    CategoryCreateView,
    CategoryUpdateCreateView,
)

from blog.views.blog.minister_views import (
    MinisterArticlesListView,
    MinistersListView,
)

from blog.views.blog.comment_views import (
    CommentCreateView,
    ArticleCommentList
)

from blog.views.dashboard.minister.dashboard_views import (
    DashboardHomeView,
    ArticleWriteView,
    ArticleUpdateView,
    ArticleDeleteView,
    DashboardArticleDetailView,
    ArticlePublishView,
    MinisterWrittenArticlesView,
    MinisterPublishedArticlesView,
    MinisterDraftedArticlesView,
    MinisterDeletedArticlesView,
)

from blog.views.dashboard.minister.minister_profile_views import (
    MinisterProfileUpdateView,
    MinisterProfileView,
)

from blog.views.account.register_view import \
    (
      ActivateView,
      AccountActivationSentView,
      UserRegisterView,
    )
from blog.views.account.logout_view import UserLogoutView
from blog.views.account.login_view import UserLoginView

from blog.views.blog.forms_view import FormsListView


# Specifies the app name for name spacing.
app_name = "blog"

# article/urls.py
urlpatterns = [
    

    # ARTICLE URLS #

    # /home/
    path(
        route='',
        view=ArticleListView.as_view(),
        name='home'
    ),

    # /article/<str:slug>/
    path(
        route='@<str:username>/<str:slug>/',
        view=ArticleDetailView.as_view(),
        name='article_detail'

    ),

    # /search/?q=query/
    path(
        route='article/search/',
        view=ArticleSearchListView.as_view(),
        name='article_search_list_view'

     ),

    # /tag/<str:tag_name>/
    path(
        route='tag/<str:tag_name>/articles',
        view=TagArticlesListView.as_view(),
        name="tag_articles"
    ),

    


    # AUTHORS URLS #

    # /ministers-list/
    path(
        route='minister/list/',
        view=MinistersListView.as_view(),
        name='minister_list'
    ),

    # /minister/<str:username>/
    path(
        route='minister/<str:username>/articles',
        view=MinisterArticlesListView.as_view(),
        name='minister_articles'
     ),


    # CATEGORY URLS #

    # category-articles/<str:slug>/
    path(
        route='category/<str:slug>/articles',
        view=CategoryArticlesListView.as_view(),
        name='category_articles'
    ),

    # /categories-list/
    path(
        route='categories/list',
        view=CategoriesListView.as_view(),
        name='categories_list'
    ),

    # /category/new/
    path(
        route='category/create/',
        view=CategoryCreateView.as_view(),
        name="category_create"
    ),

    # /category/<str:slug>/update/
    path(
        route='category/<str:slug>/update/',
        view=CategoryUpdateCreateView.as_view(),
        name="category_update"
    ),




    # COMMENT URLS #

    # /comment/new/
    path(
        route='comment/new/<str:slug>/',
        view=CommentCreateView.as_view(),
        name="comment_create"
    ),

    # /<str:slug>/comments/
    path(
        route='<str:slug>/comments/',
        view=ArticleCommentList.as_view(),
        name="article_comments"
    ),


    # ACCOUNT URLS #

    # account/login/
    path(
        route='account/login/',
        view=UserLoginView.as_view(),
        name='login'
    ),

    # account/login/
    path(
        route='account/register/',
        view=UserRegisterView.as_view(),
        name='register'
    ),

    # account/logout/
    path(
        route='account/logout/',
        view=UserLogoutView.as_view(),
        name='logout'
    ),

    path(route='account_activation_sent/',
         view=AccountActivationSentView.as_view(),
         name='account_activation_sent'
         ),

    path(route='activate/<uidb64>/<token>/',
         view=ActivateView.as_view(),
         name='activate'
         ),



    # DASHBOARD URLS #

    # /minister/dashboard/
    path(
        route="minister/dashboard/home/",
        view=DashboardHomeView.as_view(),
        name="dashboard_home"
    ),

    # minister/profile/details
    path(
        route='minister/profile/details/',
        view=MinisterProfileView.as_view(),
        name='minister_profile_details'
    ),

    # minister/profile/update/
    path(
        route='minister/profile/update/',
        view=MinisterProfileUpdateView.as_view(),
        name='minister_profile_update'
    ),

    # me/article/write
    path(
        route='me/article/write/',
        view=ArticleWriteView.as_view(),
        name="article_write"
    ),

    # me/article/<str:slug>/update/
    path(
        route='me/article/<str:slug>/update/',
        view=ArticleUpdateView.as_view(),
        name="article_update"
    ),

    # /article/<str:slug>/delete/
    path(
        route='me/article/<str:slug>/delete/',
        view=ArticleDeleteView.as_view(),
        name="article_delete"
    ),

    # /me/<str:slug>/publish/
    path(
        route="article/<str:slug>/publish/",
        view=ArticlePublishView.as_view(),
        name="publish_article"
    ),

    # /me/articles/written/
    path(
        route="me/articles/written/",
        view=MinisterWrittenArticlesView.as_view(),
        name="written_articles"
    ),

    # /me/articles/published/
    path(
        route="me/articles/published/",
        view=MinisterPublishedArticlesView.as_view(),
        name="published_articles"
    ),

    # /me/articles/drafted/
    path(
        route="me/articles/drafts/",
        view=MinisterDraftedArticlesView.as_view(),
        name="drafted_articles"
    ),

    # /me/articles/deleted/
    path(
        route="me/articles/deleted/",
        view=MinisterDeletedArticlesView.as_view(),
        name="deleted_articles"
    ),

    # /me/<str:slug>/
    path(
        route="me/<str:slug>/",
        view=DashboardArticleDetailView.as_view(),
        name='dashboard_article_detail'

    ),




    

    # /categories-list/
    path(
        route='programs/',
        view=FormsListView.as_view(),
        name='form_list'
    ),

    path(
        route='about/programs/',
        view=FormsListView.as_view(),
        name='form_list'
    ),

    path(
        route='categories/programs/',
        view=FormsListView.as_view(),
        name='form_list'
    ),

    


      # /categories-list/
    path(
        route='about/',
        view=About.as_view(),
        name='about'
    ),
    path(
        route='about/about',
        view=About.as_view(),
        name='about'
    ),

    path(
        route='categories/about',
        view=About.as_view(),
        name='about'
    ),


    path(
        route='programs/about',
        view=About.as_view(),
        name='about'
    ),

    path(
        route='programs/programs',
        view=About.as_view(),
        name='about'
    ),
    
    
    
    path(
        route='categories/programs/programs',
        view=About.as_view(),
        name='programs'
    ),
    
    
     path(
        route='categories/programs/about',
        view=About.as_view(),
        name='about'
    ),


    

 

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        