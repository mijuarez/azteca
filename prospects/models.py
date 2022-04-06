from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

def get_default_my_hour():
	hour = timezone.now()
	formatedHour = hour.strftime("%H:%M:%S")
	return formatedHour


class Prospecters(models.Model):
	sponsor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	name_student = models.CharField(max_length=50)
	lastname_student = models.CharField(max_length=30)
	mother_lastname_student = models.CharField(max_length=30)
	H = 'HOMBRE'
	M = 'MUJER'
	gender_choices = (
		(H,'HOMBRE'),
		(M,"MUJER"),
	)
	gender = models.CharField(
		max_length=6,
		choices=gender_choices,
		default=H,
	)
	AGS = 'Aguascalientes'
	BCN = 'Baja California'
	BCS = 'Baja California Sur'
	CAM = 'Campeche'
	CHP = 'Chiapas'
	CHI = 'Chihuahua'
	CMX = 'Ciudad de México'
	COA = 'Coahuila'
	COL = 'Colima'
	DUR = 'Durango'
	GTO = 'Guanajuato'
	GRO = 'Guerrero'
	HGO = 'Hidalgo'
	JAL = 'JALISCO'
	MIC = 'MICHOACAN'
	MEX = 'México'
	MOR = 'Morelos'
	NAY = 'NAYARIT'
	NLE = 'Nuevo León'
	OAX = 'Oaxaca'
	PUE = 'Puebla'
	QRO = 'Querétaro'
	ROO = 'Quintana Roo'
	SLP = 'San Luis Potosí'
	SIN = 'Sinaloa'
	SON = 'Sonora'
	TAB = 'Tabasco'
	TAM = 'Tamaulipas'
	TLX = 'Tlaxcala'
	VER = 'Veracruz'
	YUC = 'Yucatán'
	ZAC = 'Zacatecas'
	birthplace_choices= (
	(AGS, 'Aguascalientes'),
	(BCN, 'Baja California'),
	(BCS, 'Baja California Sur'),
	(CAM, 'Campeche'),
	(CHP, 'Chiapas'),
	(CHI, 'Chihuahua'),
	(CMX, 'Ciudad de México'),
	(COA, 'Coahuila'),
	(COL, 'Colima'),
	(DUR, 'Durango'),
	(GTO, 'Guanajuato'),
	(GRO, 'Guerrero'),
	(HGO, 'Hidalgo'),
	(JAL, 'Jalisco'),
	(MIC, 'Michoacán'),
	(MEX, 'México'),
	(MOR, 'Morelos'),
	(NAY, 'Nayarit'),
	(NLE, 'Nuevo León'),
	(OAX, 'Oaxaca'),
	(PUE, 'Puebla'),
	(QRO, 'Querétaro'),
	(ROO, 'Quintana Roo'),
	(SLP, 'San Luis Potosí'),
	(SIN, 'Sinaloa'),
	(SON, 'Sonora'),
	(TAB, 'Tabasco'),
	(TAM, 'Tamaulipas'),
	(TLX, 'Tlaxcala'),
	(VER, 'Veracruz'),
	(YUC, 'Yucatán'),
	(ZAC, 'Zacatecas'),
	)
	birthplace = models.CharField(
		max_length=30,
		choices=birthplace_choices,
		default=JAL,
	)
	birthdate = models.DateField(blank=True, null=True)
	educational_options = models.CharField(max_length=30)
	campus = models.CharField(max_length=30)
	time = models.TimeField(blank=True, null=True)
	day = models.DateField(blank=True, null=True)
	movil = models.CharField(max_length=10)
	email = models.CharField(max_length=255)
	agreement = models.BooleanField(default=True)
	company = models.CharField(max_length=50)
	enrollment = models.BooleanField(default=True)
	payment_enrollment  = models.IntegerField()
	S = "SEMANAL"
	M = "MENSUAL"
	payment_period_choices = (
		(S,'SEMANAL'),
		(M,"MENSUAL"),
	)
	payment_period = models.CharField(
		max_length=8,
		choices=payment_period_choices,
		default=S,
	)
	payment_period_amount = models.IntegerField()
	curp = models.CharField(max_length=18)

	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title