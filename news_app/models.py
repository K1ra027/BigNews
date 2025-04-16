from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100,verbose_name='Категория')

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = ' Категории'
    

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Титул')
    news = models.TextField(verbose_name='Текст')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='Категория')
    created_at= models.DateField(auto_now=True)
    image = models.ImageField(upload_to='news/images',verbose_name='Фото')


    def __str__(self):
        return self.title
    


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        

