from django.contrib import admin
from .models import Article, Scope, Tag
from django.forms import BaseInlineFormSet, ValidationError

class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        if len(self.forms) == 0:
            raise ValidationError('Не указаны теги!')
        self.count_is_main_tag = 0
        for form in self.forms:
            if self.count_is_main_tag > 0 and form.cleaned_data.get('is_main'):
                raise ValidationError('Главный может быть только 1 тег')
            else:
                if form.cleaned_data.get('is_main'):
                    print(f"{form.cleaned_data.get('tag')} - главный раздел")
                    self.count_is_main_tag += 1
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]
