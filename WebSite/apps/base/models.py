from django.db import models

class Post(models.Model):
 	post_title = models.CharField('Название поста', max_length = 200)
 	post_text = models.TextField('Текст поста')
 	post_photo = models.ImageField('Главное изображение', upload_to='img', blank=True)
 	post_date = models.DateTimeField('Дата публикации поста', auto_now=True)
 	post_author = models.CharField('Автор', max_length = 50)

 	def __str__(self):
 		return f'ID: {self.id} | Заголовок: {self.post_title} | Автор: {self.post_author} | Дата: {self.post_date}'

 	class Meta:
 		verbose_name = 'Пост'
 		verbose_name_plural = 'Посты'

class join_info(models.Model):
	info_title = models.CharField('Заголовок', max_length = 200)
	info_text = models.TextField('Текст')

	def __str__(self):
		return f'Название: {self.info_title}'

	class Meta:
		verbose_name = 'Как зайти на сервер?'
		verbose_name_plural = 'Как зайти на сервер?'