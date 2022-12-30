# Generated by Django 4.1.4 on 2022-12-17 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_established', models.DateField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('pincode', models.CharField(max_length=6, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('website', models.URLField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('hospital_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='hck.hospital')),
                ('specialization', models.CharField(choices=[('--', '--'), ('Anesthesiology', 'Anesthesiology'), ('Cardiography', 'Cardiography'), ('Radiology', 'Radiology'), ('Orthopedics', 'Orthopedics'), ('Opthalmology', 'Opthalmology'), ('Psychiatry', 'Psychiatry'), ('Opthalmology', 'Opthalmology'), ('Dermatology', 'Dermatology'), ('Neurology', 'Neurology'), ('Nephrology', 'Nephrology')], default='--', max_length=30)),
                ('name', models.CharField(max_length=100)),
            ],
            bases=('hck.hospital',),
        ),
    ]
