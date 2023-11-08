# Generated by Django 4.2.7 on 2023-11-08 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Papers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaperTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam', models.CharField(max_length=100)),
                ('ShortQuestions', models.IntegerField(null=True)),
                ('LongQuestions', models.IntegerField(null=True)),
                ('FillIntheBlanks', models.IntegerField(null=True)),
                ('MCQs', models.IntegerField(null=True)),
                ('TrueFalse', models.IntegerField(null=True)),
                ('ExtraFileds', models.CharField(max_length=200, null=True)),
                ('Paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paper', to='Papers.paper')),
            ],
        ),
    ]