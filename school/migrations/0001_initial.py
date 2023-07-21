# Generated by Django 4.0.7 on 2023-07-21 17:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class_room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('roomName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('middelName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Family_type',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('typeName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('middelName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
                ('class_room_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.class_room')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('subjectName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('firstName', models.CharField(max_length=50)),
                ('middelName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.IntegerField()),
                ('sex', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
                ('teacherId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('familyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.family')),
                ('familyTypeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.family_type')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.student')),
            ],
        ),
        migrations.CreateModel(
            name='Class_subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classRoomId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.class_room')),
                ('subjectId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.subject')),
                ('teacherId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.teacher')),
            ],
        ),
    ]