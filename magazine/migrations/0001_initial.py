# Generated by Django 4.0.4 on 2022-05-24 00:15

from django.db import migrations, models
import django.db.models.deletion
import markdownfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('graduation_year', models.SmallIntegerField()),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('alias', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Scriptum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', markdownfield.models.MarkdownField(rendered_field='text_rendered')),
                ('text_rendered', markdownfield.models.RenderedMarkdownField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magazine.author')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editor_note', markdownfield.models.MarkdownField(rendered_field='editor_note_rendered')),
                ('editor_note_rendered', markdownfield.models.RenderedMarkdownField()),
                ('publication_date', models.DateField(editable=False, null=True)),
                ('volume', models.SmallIntegerField(editable=False, null=True)),
                ('issue', models.SmallIntegerField(editable=False, null=True)),
                ('scripta', models.ManyToManyField(to='magazine.scriptum')),
            ],
            options={
                'ordering': ['-publication_date'],
            },
        ),
    ]