from django.contrib import admin

from .models import Post, join_info

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id','post_title', 'post_date', 'post_author']

	class Meta:
		model = Post

@admin.register(join_info)
class PostAdmin(admin.ModelAdmin):
	list_display = ['info_title']

	class Meta:
		model = join_info