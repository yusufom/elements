from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Element(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    formula= RichTextUploadingField(max_length=200,blank=True, null=True)
    CASno = models.CharField(max_length=300,blank=True, null=True)
    
    def __str__(self):
        return f"{self.name}"

class  Vapor_Pressure_Of_IOL(models.Model):
    el = models.ForeignKey(Element, related_name='Vapor_pressure_Of_IOL', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    C5= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    PTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    PTmax= models.CharField(max_length=2000, blank=True, null=True)
        
class  DensityOfIOL(models.Model):
    Equation = (
    ('1','1'),
    ('2','2'),
    )
    el = models.ForeignKey(Element, related_name='DensityOfIOl', blank=True, on_delete=models.CASCADE)
    eqn = models.CharField(max_length=2000, blank=True, null=True, choices=Equation)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    DTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    DTmax= models.CharField(max_length=2000, blank=True, null=True)
    
class  CriticalConstantsAndAFIOC(models.Model):
    el = models.ForeignKey(Element, related_name='CriticalconstantsAndAFIOC', blank=True, on_delete=models.CASCADE)
    Tc= models.CharField(max_length=2000, blank=True, null=True)
    Pc= models.CharField(max_length=2000, blank=True, null=True)
    Vc= models.CharField(max_length=2000, blank=True, null=True)
    Zc= models.CharField(max_length=2000, blank=True, null=True)
    AccentricFactor= models.CharField(max_length=2000, blank=True, null=True)
    
class  HeatofVaporizationOIOL(models.Model):
    el = models.ForeignKey(Element, related_name='HeatofvaporizationOIOL', blank=True, on_delete=models.CASCADE)
    C1x07= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    HvTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    HvTmax= models.CharField(max_length=2000, blank=True, null=True)
    
class  HeatCapacityOIOL(models.Model):
    Equation = (
    ('1','1'),
    ('2','2'),
    )
    el = models.ForeignKey(Element, related_name='HeatcapacityOIOL', blank=True, on_delete=models.CASCADE)
    eqn = models.CharField(max_length=2000, blank=True, null=True, choices=Equation)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    C5= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    CpTminE05= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    CpTmaxE05= models.CharField(max_length=2000, blank=True, null=True)
    
class  HeatCapacityAtConstantPOIOLpolynomial(models.Model):
    el = models.ForeignKey(Element, related_name='HeatcapacityAtConstantPOIOLpolynomial', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4E05= models.CharField(max_length=2000, blank=True, null=True)
    C5E10= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    CpTminE05= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    CpTmaxE05= models.CharField(max_length=2000, blank=True, null=True)
    
class  HeatCapacityAtConstantPOIOLhyperbolic(models.Model):
    el = models.ForeignKey(Element, related_name='HeatcapacityAtConstantPOIOLhyperbolic', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3E03= models.CharField(max_length=2000, blank=True, null=True)
    C4E05= models.CharField(max_length=2000, blank=True, null=True)
    C5= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    CpTminE05= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    CpTmaxE05= models.CharField(max_length=2000, blank=True, null=True)
    
class  EnthalpyandGibbs(models.Model):
    el = models.ForeignKey(Element, related_name='Enthalpyandgibbs', blank=True, on_delete=models.CASCADE)
    IdealgasEnthalpyE07= models.CharField(max_length=2000, blank=True, null=True)
    IdealgasGibbsE07= models.CharField(max_length=2000, blank=True, null=True)
    IdealgasEntropyE05= models.CharField(max_length=2000, blank=True, null=True)
    StandardnetEnthalpyE09= models.CharField(max_length=2000, blank=True, null=True)
    
class  VaporViscosityIOS(models.Model):
    el = models.ForeignKey(Element, related_name='VaporviscosityIOS', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    VsTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    VsTmax= models.CharField(max_length=2000, blank=True, null=True)

class  ViscosityofIOL(models.Model):
    el = models.ForeignKey(Element, related_name='ViscosityofIOl', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    C5= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    VsTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    VsTmax= models.CharField(max_length=2000, blank=True, null=True)
    
class  VaporThermalofIOS(models.Model):
    el = models.ForeignKey(Element, related_name='VaporthermalofIOS', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    TCTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    TCTmax= models.CharField(max_length=2000, blank=True, null=True)
    
class  ThermalConductivityofIOL(models.Model):
    el = models.ForeignKey(Element, related_name='ThermalconductivityofIOL', blank=True, on_delete=models.CASCADE)
    C1= models.CharField(max_length=2000, blank=True, null=True)
    C2= models.CharField(max_length=2000, blank=True, null=True)
    C3= models.CharField(max_length=2000, blank=True, null=True)
    C4= models.CharField(max_length=2000, blank=True, null=True)
    C5= models.CharField(max_length=2000, blank=True, null=True)
    Tmin= models.CharField(max_length=2000, blank=True, null=True)
    TCTmin= models.CharField(max_length=2000, blank=True, null=True)
    Tmax= models.CharField(max_length=2000, blank=True, null=True)
    TCTmax= models.CharField(max_length=2000, blank=True, null=True)