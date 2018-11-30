# Generated by Django 2.1.3 on 2018-11-28 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbim', '0002_auto_20181128_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviereviews',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbim.Movie'),
        ),
        migrations.AlterField(
            model_name='moviereviews',
            name='review_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbim.Review'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbim.Movie'),
        ),
        migrations.AlterField(
            model_name='roles',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbim.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='moviereviews',
            unique_together={('movie_id', 'review_id')},
        ),
        migrations.AlterUniqueTogether(
            name='roles',
            unique_together={('movie_id', 'person_id')},
        ),
    ]