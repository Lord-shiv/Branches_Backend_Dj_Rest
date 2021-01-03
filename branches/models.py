from django.db import models


class Branch(models.Model):
    branchId = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=200)
    ifsc_code = models.CharField(max_length=100)
    address = models.CharField(max_length=225)
    city = models.CharField(max_length=64, default="MUMBAI")
    district = models.CharField(max_length=64, default="GREATER BOMBAY")
    state = models.CharField(max_length=64, default="MAHARASHTRA")

    def __str__(self):
        return self.branch_name
