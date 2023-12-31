# Generated by Django 4.2.5 on 2023-10-15 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_scopes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.tag'),
        ),
    ]
