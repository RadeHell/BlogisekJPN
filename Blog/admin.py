from django.contrib import admin
from .models import Cities, Comment
from .models import VocabularyList, VocabularyWord

admin.site.register(Cities)
admin.site.register(Comment)


admin.site.register(VocabularyList)
admin.site.register(VocabularyWord)

