from django.contrib import admin, messages
from magazine.models import Author, Scriptum, Magazine

# BUG: Markdown field causes admin view to fail

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Scriptum)
class ScriptumAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'author_pseudonym']

@admin.register(Magazine)
class MagazineAdmin(admin.ModelAdmin):
    list_display = ['status', 'volume', 'issue', 'publication_date']

    actions = ['publish', 'withdraw']

    @admin.action(description='Publish selected magazine')
    def publish(self, request, queryset):
        if len(queryset) > 1:
            self.message_user(request, 'Cannot publish more than one magazine at once', messages.MessageFailure)
        else:
            queryset.first().publish()
            self.message_user(request, 'Published magazine', messages.SUCCESS)

    @admin.action(description='Withdraw selected magazine')
    def withdraw(self, request, queryset):
        for magazine in queryset:
            magazine.withdraw()
        # TODO: better error messaging
