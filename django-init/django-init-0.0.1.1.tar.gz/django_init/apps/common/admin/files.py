from django.utils.translation import ugettext_lazy as _

FIELDSETS_PAGES_ICON = (u'Иконки страницы', {'fields': [('thumbnail_icon_1', 'icon_1'), ('thumbnail_icon_2', 'icon_2')],
                                             'classes': ['collapse']})

FIELDSETS_COVERS_SIMPLE_BASE = ('cover', 'thumbnail_cover')
FIELDSETS_COVERS_SIMPLE_SMALL = ('cover', 'thumbnail_cover_small')
FIELDSETS_COVERS_SIMPLE = (_('ОБЛОЖКА'), {'fields': [FIELDSETS_COVERS_SIMPLE_BASE]})

FIELDSETS_COVERS_BASE = FIELDSETS_COVERS_SIMPLE_BASE + ('is_show_cover',)
FIELDSETS_COVERS_SMALL = FIELDSETS_COVERS_SIMPLE_SMALL + ('is_show_cover',)
FIELDSETS_COVERS = (_('ОБЛОЖКА'), {'fields': [FIELDSETS_COVERS_BASE]})

FIELDSETS_COVERS_D_BASE = ('cover_2', 'thumbnail_2_tag', 'is_show_cover_2',)
FIELDSETS_COVERS_D_SMALL = ('cover_2', 'thumbnail_tag_2_small', 'is_show_cover_2',)
FIELDSETS_COVERS_D = (_('ОБЛОЖКА'), {'fields': [FIELDSETS_COVERS_D_BASE]})

FIELDSETS_BACKS_BASE = ('back', 'thumbnail_back', 'is_show_back')
FIELDSETS_BACKS = (_('Фон'), {'fields': [FIELDSETS_COVERS_BASE]})

FIELDSETS_COVER_NEW = (_('ОБЛОЖКА'), {'fields': ['cover', 'cover_title', 'cover_description'],
                                      'classes': ['collapse']})

FIELDSETS_COVER_FULL = (_('ОБЛОЖКА'), {'fields': [('thumbnail_cover', 'cover', 'is_show_cover'),
                                                  'cover_title', 'cover_description'], 'classes': ['collapse']})

FIELDSETS_BACK_NEW = (_('Фон'), {'fields': [('back', 'thumbnail_back', 'is_show_back'),
                                            'back_title', 'back_description'], 'classes': ['collapse']})


FIELDSETS_TEXT = (_('ТЕКСТ'), {'fields': ['full_text', 'short_text'], 'classes': ['collapse']})