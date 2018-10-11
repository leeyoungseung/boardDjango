from django.db import models


# Create your models here.
class Board(models.Model):
	b_id = models.AutoField(primary_key=True)
	b_writer = models.CharField(max_length=30)
	b_email = models.CharField(max_length=30)
	b_subject = models.CharField(max_length=30)
	b_passwd = models.CharField(max_length=30)
	b_reg_date = models.DateField(auto_now_add=True)
	b_read_count = models.IntegerField(null=True)
	b_content = models.CharField(max_length=500)
	b_ip = models.CharField(max_length=300)
	b_file_name = models.CharField(max_length=30)
	b_file_size = models.IntegerField()


	def __str__(self):
		return '%s %s %s' % (self.b_id, self.b_writer, self.b_subject)