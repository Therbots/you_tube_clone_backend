# Generated by Django 3.2.7 on 2021-09-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=50)),
                ('like', models.IntegerField()),
                ('dislike', models.IntegerField()),
                ('comment', models.CharField(max_length=150)),
                ('reply', models.CharField(max_length=150)),
            ],
        ),
    ]