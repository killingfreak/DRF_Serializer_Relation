# Generated by Django 3.2 on 2022-10-19 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='school',
            field=models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='api.school'),
        ),
    ]
