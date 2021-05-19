# Generated by Django 3.2.3 on 2021-05-18 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=1000, verbose_name='Text')),
                ('publication_date', models.DateField(verbose_name='Publication Date')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200, verbose_name='Choice text')),
                ('number_of_votes', models.IntegerField(default=0, verbose_name='Number of Votes')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling.question')),
            ],
        ),
    ]
