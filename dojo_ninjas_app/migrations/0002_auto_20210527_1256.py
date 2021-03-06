# Generated by Django 2.2 on 2021-05-27 19:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ninja',
            name='dojo',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='ninjas', to='dojo_ninjas_app.Dojo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dojo',
            name='state',
            field=models.CharField(max_length=255),
        ),
    ]
