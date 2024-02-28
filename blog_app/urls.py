from django.urls import path

from blog_app import views

app_name = "news_admin"

# {% url 'news_admin:post-list' %}

urlpatterns = [
    path(
        "",
        views.PostListView.as_view(),
        name="post-list",
    ),
    path(
        "post-detail/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "draft-list/",
        views.DraftListView.as_view(),
        name="draft-list",
    ),
    path(
        "draft-detail/<int:pk>/",
        views.DraftDetailView.as_view(),
        name="draft-detail",
    ),
    path(
        "draft-publish/<int:pk>/",
        views.DraftPublishView.as_view(),
        name="draft-publish",
    ),
    path(
        "post-delete/<int:pk>/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path(
        "post-create/",
        views.PostCreateView.as_view(),
        name="post-create",
    ),
    path(
        "post-update/<int:pk>/",
        views.PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "tag-list/",
        views.TagListView.as_view(),
        name="tag-list",
    ),
    path(
        "category-list/",
        views.CategoryListView.as_view(),
        name="category-list",
    ),
    path(
        "post-list/",
        views.AllPostListView.as_view(),
        name="all-post-list",
    ),
    path(
        "tag-create/",
        views.TagCreateView.as_view(),
        name="tag-create",
    ),
    path(
        "tag-update/<int:pk>/",
        views.TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tag-delete/<int:pk>/",
        views.TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path(
        "category-create/",
        views.CategoryCreateView.as_view(),
        name="category-create",
    ),
    path(
        "category-update/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "category-delete/<int:pk>/",
        views.CategoryDeleteView.as_view(),
        name="category-delete",
    ),
]