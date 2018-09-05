# Generated by Django 2.1 on 2018-08-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_writer', models.CharField(max_length=30)),
                ('b_email', models.CharField(max_length=30)),
                ('b_subject', models.CharField(max_length=30)),
                ('b_passwd', models.CharField(max_length=30)),
                ('b_reg_date', models.DateField(auto_now_add=True)),
                ('b_read_count', models.IntegerField(null=True)),
                ('b_content', models.CharField(max_length=500)),
                ('b_ip', models.CharField(max_length=300)),
                ('b_file_name', models.CharField(max_length=30)),
                ('b_file_size', models.IntegerField()),
            ],
        ),
    ]
