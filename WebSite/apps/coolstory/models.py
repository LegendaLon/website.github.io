from django.db import models

from django.utils import timezone

class Person(models.Model):
	person_name = models.CharField('Имя персонажа', max_length = 200)
	person_photo = models.ImageField('Изображение персонажа', upload_to='img', blank=True)
	person_author = models.CharField('Автор персонажа', max_length = 50)

	def __str__(self):
		return f'Имя: {self.person_name}'

	class Meta:
		verbose_name = 'Персонаж'
		verbose_name_plural = 'Персонажи'

class PersonHistory(models.Model):
	person_add = models.ForeignKey(
			Person, default=1, verbose_name="Персонаж", on_delete=models.CASCADE, related_name="history"
		)
	history_title = models.CharField('Заголовок истории', max_length = 200)
	history_text = models.TextField('Текст Истории')
	history_photo = models.ImageField('Изображения истории', upload_to='img', blank=True)
	history_author = models.CharField('Автор истории', max_length = 50)
	history_date = models.DateTimeField('Дата публикации истории', auto_now=True)

	def __str__(self):
		return f'ID: {self.id} | Название: {self.history_title} | История для: {self.person_add.person_name} | Автор: {self.history_author}'

	class Meta:
		verbose_name = 'История'
		verbose_name_plural = 'Истории'