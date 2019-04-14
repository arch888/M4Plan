from django.db import models

ch=[
    ('UBT','UBT'),
    ('Work Aid','Work Aid'),
    ('MT','MT'),
]

cho=[
    ('MF','MF'),
    ('AF','AF'),
]

class Complexity_factor(models.Model):
    complx_fact=models.CharField(max_length=2,choices=cho,default='MF')

    def __str__(self):
        return str(self.complx_fact)


class Complexity(models.Model):
    complex_fact = models.ForeignKey(Complexity_factor, on_delete=models.CASCADE)
    complx=models.DecimalField(max_digits=2,decimal_places=1)

    def __str__(self):
        return str(self.complx)

class SPI(models.Model):
    s_p_i=models.IntegerField(default=12)

    def __str__(self):
        return str(self.s_p_i)

class Stitch_Length(models.Model):
    stitch_length = models.IntegerField()

    def __str__(self):
        return str(self.stitch_length)

class SMV(models.Model):
    complexity_Factor = models.ForeignKey(Complexity_factor,on_delete=models.CASCADE,default='MF')
    complexity=models.ForeignKey(Complexity,on_delete=models.CASCADE)
    operation=models.CharField(max_length=30)
    s_P_I=models.ForeignKey(SPI,on_delete=models.CASCADE,default=12)
    stitch_Length=models.ForeignKey(Stitch_Length,on_delete=models.CASCADE,default=20)
    machine=models.CharField(max_length=25)
    automation=models.CharField(max_length=20,choices=ch,default='UBT')
    work_Aid=models.CharField(max_length=50,default='BINDER')
    pick_in_sec=models.IntegerField()
    pick_in_frequency=models.IntegerField(default=1)
    main_Process_in_sec=models.IntegerField()
    main_Process_in_frequency=models.IntegerField(default=1)
    turn_in_sec=models.IntegerField()
    turn_in_frequency=models.IntegerField(default=1)
    dispose_in_sec=models.IntegerField()
    dispose_in_frequency=models.IntegerField(default=1)
    personal_Allowance=models.DecimalField(max_digits=4,decimal_places=2,default=5)
    fatigue_Allowance=models.DecimalField(max_digits=4,decimal_places=2,default=5)
    delay_Allowance=models.DecimalField(max_digits=4,decimal_places=2,default=5)

    def __str__(self):
        return self.operation



SEC=[('Colar Section','Colar Section'),
    ('Sleeve Section','Sleeve Section'),
     ('Lining Section','Lining Section'),
     ('Front Section','Front Section'),
     ('Assembly Section','Assembly Section'),
]
class Section(models.Model):
    name=models.CharField(choices=SEC,max_length=20,default='Colar Section')

    def __str__(self):
        return self.name

class PFM(models.Model):
    sec=models.ForeignKey(Section,on_delete=models.CASCADE,blank=True)
    oper=models.CharField(max_length=40)

    def __str__(self):
        return self.oper
