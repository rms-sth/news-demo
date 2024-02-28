from newspaper.models import Post, Tag, Category


def navigation(request):
    categories = Category.objects.all()[:5]
    tags = Tag.objects.all()[:10]
    recent_posts = Post.objects.filter(
        published_at__isnull=False,
        status="active",
    ).order_by("-published_at", "-views_count")[:3]

    return {
        "categories": categories,
        "tags": tags,
        "recent_posts": recent_posts,
    }
