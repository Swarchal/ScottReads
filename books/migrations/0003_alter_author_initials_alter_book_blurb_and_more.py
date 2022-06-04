# Generated by Django 4.0.5 on 2022-06-04 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0002_remove_book_published_alter_author_initials_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="initials",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="blurb",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(blank=True, null=True, to="books.genre"),
        ),
        migrations.AlterField(
            model_name="book",
            name="isbn",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="page_count",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="book",
            name="pub_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="published date"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="subtitle",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="reading",
            name="comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reading",
            name="finished_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="reading",
            name="rating",
            field=models.FloatField(blank=True, null=True),
        ),
    ]