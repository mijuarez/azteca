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
	name_student = models.CharField(u'Nombre(s)', max_length=50)
	lastname_student = models.CharField(u'Apellido Paterno', max_length=30)
	mother_lastname_student = models.CharField(u'Apellido Materno', max_length=30)
	H = 'HOMBRE'
	M = 'MUJER'
	gender_choices = (
		(H,'HOMBRE'),
		(M,"MUJER"),
	)
	gender = models.CharField(
		u'Genero',
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
	JAL = 'Jalisco'
	MIC = 'Michoacán'
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
		u'Lugar de Nacimiento',
		max_length=30,
		choices=birthplace_choices,
		default=JAL,
	)
	birthdate = models.DateField(u'Fecha de Nacimiento',blank=True, null=True)
	educational_options = models.CharField(u'Oferta Educativa', max_length=30)
	campus = models.CharField(u'Plantel', max_length=30)
	time = models.TimeField(u'Horario', blank=True, null=True)
	day = models.DateField(u'Fecha de Inicio', blank=True, null=True)
	movil = models.CharField(u'Teléfono Móvil', max_length=10)
	email = models.CharField(u'Correo Electrónico', max_length=255)
	agreement = models.BooleanField(u'Convenio', default=True)
	company = models.CharField(u'Empresa', max_length=50)
	enrollment = models.BooleanField(u'Inscripción', default=True)
	payment_enrollment  = models.IntegerField(u'Monto de Inscripción')
	S = "SEMANAL"
	M = "MENSUAL"
	payment_period_choices = (
		(S,'SEMANAL'),
		(M,"MENSUAL"),
	)
	payment_period = models.CharField(
		u'Colegiatura',
		max_length=8,
		choices=payment_period_choices,
		default=S,
	)
	payment_period_amount = models.IntegerField(u'Monto de Colegiatura')
	curp = models.CharField(u'CURP', max_length=18)
	notes = models.TextField(u'NOTAS', max_length=2000, blank=True, null=True)
	PROSPECTO = "PROSPECTO"
	INSCRITO = "INSCRITO"
	status_options = (
		(PROSPECTO,'PROSPECTO'),
		(INSCRITO,"INSCRITO"),
	)
	status = models.CharField(
		u'Estatus',
		max_length=10,
		choices=status_options,
		default=INSCRITO,
	)

	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = "Prospectos"
		verbose_name = "Prospecto"
