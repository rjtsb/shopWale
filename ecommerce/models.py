from django.db import models

class Signup(models.Model):
	name = models.CharField(max_length=40)
	email = models.EmailField(max_length=80)
	mobile = models.IntegerField()
	address = models.CharField(max_length=150)
	password = models.CharField(max_length=40)
	pin = models.IntegerField()

	def __str__(self):
		return self.name

class Oneplus(models.Model):
	odiscount = models.IntegerField()
	obrand = models.CharField(max_length=10)
	opic = models.ImageField(upload_to='imgs', default="")
	oname = models.CharField(max_length=50)
	odesc = models.CharField(max_length=200)
	oprice = models.IntegerField()

	def __str__(self):
		return self.oname

class Iphone(models.Model):
	idiscount = models.IntegerField()
	ibrand = models.CharField(max_length=10)
	ipic = models.ImageField(upload_to='imgs', default="")
	iname = models.CharField(max_length=50)
	idesc = models.CharField(max_length=200)
	iprice = models.IntegerField()
	
	def __str__(self):
		return self.iname

class Samsung(models.Model):
	sdiscount = models.IntegerField()
	sbrand = models.CharField(max_length=10)
	spic = models.ImageField(upload_to='imgs', default="")
	sname = models.CharField(max_length=50)
	sdesc = models.CharField(max_length=200)
	sprice = models.IntegerField()

	def __str__(self):
		return self.sname

class Hp(models.Model):
	hpdiscount = models.IntegerField()
	hpbrand = models.CharField(max_length=10)
	hppic = models.ImageField(upload_to='imgs', default="")
	hpname = models.CharField(max_length=50)
	hpdesc = models.CharField(max_length=200)
	hpprice = models.IntegerField()

	def __str__(self):
		return self.hpname
class Dell(models.Model):
	delldiscount = models.IntegerField()
	dellbrand = models.CharField(max_length=10)
	dellpic = models.ImageField(upload_to='imgs', default="")
	dellname = models.CharField(max_length=50)
	delldesc = models.CharField(max_length=200)
	dellprice = models.IntegerField()

	def __str__(self):
		return self.dellname

class Lenovo(models.Model):
	ldiscount = models.IntegerField()
	lbrand = models.CharField(max_length=10)
	lpic = models.ImageField(upload_to='imgs', default="")
	lname = models.CharField(max_length=50)
	ldesc = models.CharField(max_length=200)
	lprice = models.IntegerField()

	def __str__(self):
		return self.lname

class Tshirt(models.Model):
	tdiscount = models.IntegerField()
	tbrand = models.CharField(max_length=10)
	tpic = models.ImageField(upload_to='imgs', default="")
	tname = models.CharField(max_length=50)
	tdesc = models.CharField(max_length=200)
	tprice = models.IntegerField()


	def __str__(self):
		return self.tname

class Shirt(models.Model):
	shdiscount = models.IntegerField()
	shbrand = models.CharField(max_length=10)
	shpic = models.ImageField(upload_to='imgs', default="")
	shname = models.CharField(max_length=50)
	shdesc = models.CharField(max_length=200)
	shprice = models.IntegerField()


	def __str__(self):
		return self.shname

class Shoe(models.Model):
	shoediscount = models.IntegerField()
	shoebrand = models.CharField(max_length=10)
	shoepic = models.ImageField(upload_to='imgs', default="")
	shoename = models.CharField(max_length=50)
	shoedesc = models.CharField(max_length=200)
	shoeprice = models.IntegerField()


	def __str__(self):
		return self.shoename

class Watch(models.Model):
	wdiscount = models.IntegerField()
	wbrand = models.CharField(max_length=10)
	wpic = models.ImageField(upload_to='imgs', default="")
	wname = models.CharField(max_length=50)
	wdesc = models.CharField(max_length=200)
	wprice = models.IntegerField()


	def __str__(self):
		return self.wname

class Jeans(models.Model):
	jdiscount = models.IntegerField()
	jbrand = models.CharField(max_length=10)
	jpic = models.ImageField(upload_to='imgs', default="")
	jname = models.CharField(max_length=50)
	jdesc = models.CharField(max_length=200)
	jprice = models.IntegerField()

	def __str__(self):
		return self.jname

class Order(models.Model):
	pdiscount = models.IntegerField()
	pbrand = models.CharField(max_length=10)
	ppic = models.ImageField(upload_to='imgs', default="")
	pname = models.CharField(max_length=50)
	pdesc = models.CharField(max_length=200)
	pprice = models.IntegerField()

	def __str__(self):
		return self.pname

class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=80)
	message = models.CharField(max_length= 300)

	def __str__(self):
		return self.name