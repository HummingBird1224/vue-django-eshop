from notices.models import NoticeCategory

def render_notice_info(request):
    """
      The context processor must return a dictionary.
    """
    user = request.user
    if not user.is_authenticated:
        return {}
    
    user_notice_categories = [
        {
          'slug': notice_category.slug,
          'message': notice_category.message,
          'is_read': not user.notice_set.filter(noticeread__read_at=None,category_id=notice_category.id).exists(),
          'icon_path': notice_category.icon_path,
        } for notice_category in NoticeCategory.objects.all()
      ]
    unread_category_list = list(filter(lambda cat: cat['is_read'] == False,user_notice_categories))

    return {
        'user_notice_summary': {
            'unread_count': len(unread_category_list),
            'user_notice_categories': user_notice_categories
        },
    }