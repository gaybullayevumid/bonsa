from modeltranslation.translator import register, TranslationOptions
from .models import Category, Blog, Comment

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

@register(Category)
class CategoryTranslateOptions(TranslationOptions):
    fields = ('name',)

@register(Comment)
class CommentTranslateOptions(TranslationOptions):
    fields = ('content',)