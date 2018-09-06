from django.db import models
from app.core.models import CreateUpdateModel, UUIDUser

# Projector
# - - - - - - - - - - - - - - - - - - -
class Projector (CreateUpdateModel):

	Computador_Interativo = "Interativo"
	Datashow = "Datashow"
	TYPE = (
		(Datashow, "Datashow"),
		(Computador_Interativo, "Interativo")
		)

	HDMI = "HDMI"
	VGA = "VGA"
	CABLE = (
		(HDMI, "HDMI"), 
		(VGA, "VGA")
		)

	tipping = models.CharField(max_length=255, null=False, blank=False, unique=True, verbose_name='Tombamento')
	status = models.BooleanField(null=False, verbose_name='Disponibilidade')
	type = models.CharField(max_length=10, choices=TYPE, default=Datashow, verbose_name='Tipo')
	note = models.CharField(max_length=255, null=True, blank=True, verbose_name='Notas')
	cable = models.CharField(max_length=4, choices=CABLE, default=VGA, verbose_name='Tipo')

	def __str__(self):
		return "%s" % (self.tipping)

	class Meta:
		verbose_name = 'Projetor'
		verbose_name_plural = 'Projetores'
		
# Reserve
# - - - - - - - - - - - - - - - - - - -
class Reserve (CreateUpdateModel):

	user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, null=False, verbose_name='Usuário')
	date = models.DateField(auto_now=False, auto_now_add=False,verbose_name='Data')
	projector = models.ForeignKey('Projector', on_delete=models.CASCADE, null=False, verbose_name='Projetor')
	slots = models.ManyToManyField('Slot', verbose_name="Slot")

	def __str__(self):
		return self.user.first_name

	class Meta:
		verbose_name = 'Reserva'
		verbose_name_plural = 'Reservas'

# Rate
# - - - - - - - - - - - - - - - - - - -
class Rate (CreateUpdateModel):

	rate = models.TextField(null=False, verbose_name='Avaliação')
	user = models.ForeignKey(UUIDUser, on_delete=models.CASCADE, null=False, verbose_name='Usuário')
	projector = models.ForeignKey('Projector', on_delete=models.CASCADE, null=False, verbose_name='Projetor')

	def __str__(self):
		return self.first_name

	class Meta:
		verbose_name = 'Avaliação'
		verbose_name_plural = 'Avaliações'

# Slot
# - - - - - - - - - - - - - - - - - - -
class Slot (CreateUpdateModel):

	TURNS = (
		(0, "Manhã"), 
		(1, "Tarde"),
		(2, "Noite")
	)

	name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
	start = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Horário Início')
	end = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Horário Final')
	turn = models.IntegerField(choices= TURNS)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Slot'
		verbose_name_plural = 'Slots'