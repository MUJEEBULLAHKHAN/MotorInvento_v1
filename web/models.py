from django.db import models

# Create your models here.

class admins(models.Model):
    # admin_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=200,null=False)
    email = models.CharField(max_length=200, unique=True,null=False)
    mobile_no = models.CharField(max_length=10,null=False)
    username = models.CharField(max_length=50,null=False)
    password = models.CharField(max_length=50,null=False)
    national_id = models.CharField(max_length=200,null=False)
    role = models.CharField(max_length=12,null=False)

    def __str__(self):
        return self.full_name

class make(models.Model):
    make_id = models.AutoField(primary_key=True)
    make_name = models.CharField(max_length=200)
    # admin = models.ForeignKey(admins,on_delete=models.CASCADE)

    def __str__(self):
        return self.make_name

class model(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=200)
    make = models.ForeignKey(make,on_delete=models.CASCADE)
    # admin = models.ForeignKey(admins,on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name

class years(models.Model):
    year_id = models.AutoField(primary_key=True)
    year = models.CharField(max_length=200)
    # model = models.ForeignKey(model,on_delete=models.CASCADE)
    # make = models.ForeignKey(make,on_delete=models.CASCADE)
    # admin = models.ForeignKey(admins,on_delete=models.CASCADE)

    def __str__(self):
        return self.year


class addcar(models.Model):
    car_id = models.AutoField(primary_key=True)
    purchase_price = models.IntegerField()
    purchase_date = models.DateTimeField(auto_now=True)
    year = models.CharField(max_length=200)
    model = models.ForeignKey(model,on_delete=models.CASCADE)
    make = models.ForeignKey(make,on_delete=models.CASCADE)
    admin = models.ForeignKey(admins,on_delete=models.CASCADE)

    def __str__(self):
        return self.car_id

class addpart(models.Model):
    part_id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=200)
    part_no = models.IntegerField()
    is_scrap = models.BooleanField(default=False)
    sell_price = models.CharField(max_length=200)
    part_location = models.CharField(max_length=200)
    year = models.ForeignKey(years,on_delete=models.CASCADE)
    model = models.ForeignKey(model,on_delete=models.CASCADE)
    make = models.ForeignKey(make,on_delete=models.CASCADE)
    admin = models.ForeignKey(admins,on_delete=models.CASCADE)

    def __str__(self):
        return self.part_id

class sellpart(models.Model):
    sell_id = models.AutoField(primary_key=True)
    part_name = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)
    discount = models.CharField(max_length=200)
    discounted_amount = models.CharField(max_length=200)
    sell_price = models.CharField(max_length=200)
    sell_price_after_discount = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    sub_total = models.CharField(max_length=200)
    year = models.ForeignKey(years,on_delete=models.CASCADE)
    model = models.ForeignKey(model,on_delete=models.CASCADE)
    make = models.ForeignKey(make,on_delete=models.CASCADE)
    admin = models.ForeignKey(admins,on_delete=models.CASCADE)

    def __str__(self):
        return self.sell_id


# models.py
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)

class Task(models.Model):
    name = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
