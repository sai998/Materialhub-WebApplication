from django.db import models

# Create your models here.

class login(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100)



class users(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)




class dealers(models.Model):
    dealer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE,default=1)


class drivers(models.Model):
    driver_name = models.CharField(max_length=100)
    license_no = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    DEALER = models.ForeignKey(dealers, on_delete=models.CASCADE, default=1)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE, default=1)


class material(models.Model):
    material_rate = models.CharField(max_length=100)
    material_type = models.CharField(max_length=100)
    material_image = models.CharField(max_length=100)


class complaint(models.Model):
    complaint = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    replay = models.CharField(max_length=100)
    replay_date = models.CharField(max_length=100)
    USER = models.ForeignKey(users, on_delete=models.CASCADE, default=1)

class order(models.Model):
    order_date = models.CharField(max_length=100)
    total_price = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    USER = models.ForeignKey(users, on_delete=models.CASCADE, default=1)
    otp = models.CharField(max_length=100)



class feedback(models.Model):
    feedback_date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)
    USER = models.ForeignKey(users, on_delete=models.CASCADE, default=1)


class order_allocation(models.Model):
    allocation_date = models.CharField(max_length=100)
    ORDER = models.ForeignKey(order, on_delete=models.CASCADE, default=1)
    DRIVER = models.ForeignKey(drivers, on_delete=models.CASCADE, default=1)




class payment(models.Model):
    payment_date = models.CharField(max_length=100)
    ammount = models.CharField(max_length=100)
    USER = models.ForeignKey(users, on_delete=models.CASCADE, default=1)
    ORDER = models.ForeignKey(order, on_delete=models.CASCADE, default=1)



class review(models.Model):
    review_date = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    USER = models.ForeignKey(users, on_delete=models.CASCADE, default=1)
    DEALER = models.ForeignKey(dealers, on_delete=models.CASCADE, default=1)


class stock(models.Model):
    stock = models.CharField(max_length=100)
    DEALER = models.ForeignKey(dealers, on_delete=models.CASCADE, default=1)
    MATERIAL = models.ForeignKey(material, on_delete=models.CASCADE, default=1)



class order_sub(models.Model):
    quantity = models.CharField(max_length=100)
    ORDER = models.ForeignKey(order, on_delete=models.CASCADE, default=1)
    STOCK = models.ForeignKey(stock, on_delete=models.CASCADE, default=1)









