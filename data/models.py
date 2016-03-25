from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Adult(models.Model):




    charNames = (
        ('CrrnM', 'CorrinM'),
        ('CrrnF', 'CorrinF'),
        ('Sls','Silas'),
        ('Hyt', 'Hayato'),
        ('Kgr', 'Kagero'),
        ('Bnny', 'Benny'),
        ('Eff', 'Effie'),
        ('Tkm', 'Takumi'),
        ('Hnk', 'Hinoka'),
        ('Xndr', 'Xander'),
        ('L', 'Leo'),
        ('Obr', 'Oboro'),
        ('Cmll', 'Camilla'),
        ('Rym', 'Ryoma'),
        ('Hn', 'Hana'),
        ('Ktn', 'Keaton'),
        ('Azm', 'Azama'),
        ('Odn', 'Odin'),
        ('Lslw', 'Laslow'),
        ('Pr', 'Peri'),
        ('Nls', 'Niles'),
        ('Stsn', 'Setsuna'),
        ('Azr', 'Azura'),
        ('Nx', 'Nyx'),
        ('Shr', 'Shura'),
        ('Kz', 'Kaze'),
        ('Sln', 'Selena'),
        ('Jkb', 'Jakob'),
        ('Gntr', 'Gunter'),
        ('Skr', 'Sakura'),
        ('Sbk', 'Subaki'),
        ('Rnkh', 'Rinkah'),
        ('Mz', 'Mozu'),
        ('Sz', 'Saizo'),
        ('Els', 'Elise'),
        ('Arthr', 'Arthur'),
        ('Chrltt', 'Charlotte'),
        ('Rn', 'Reina'),
        ('Kdn', 'Kaden'),
        ('Brk', 'Beruka'),
        ('Hnt', 'Hinata'),
        ('Orch', 'Orochi'),
        ('Flc', 'Felicia'),
        ('Scrlt', 'Scarlet'),
        ('Fg', 'Fuga'),
        ('Izn', 'Izana'),
    )
    classFE = (
        ('Spr Mstr', 'Spear Master'),
        ('Bsr', 'Basara'),
        ('Gnrl', 'General'),
        ('Grt Knght', 'Great Knight'),
        ('Pldn', 'Paladin'),
        ('Swrdmstr', 'Swordmaster'),
        ('Mstr of Arms', 'Master of Arms'),
        ('Mstr Nnj', 'Master Ninja'),
        ('Mchnst', 'Mechanist'),
        ('Mrchnt', 'Merchant'),
        ('On Chftn', 'Oni Chieftan'),
        ('Blcksmth', 'Blacksmith'),
        ('Onmyj', 'Onmyoji'),
        ('Grt Mstr', 'Great Master'),
        ('Prstss', 'Priestess'),
        ('Flcn, Knght', 'Falcon Knight'),
        ('Knsh Knght', 'Kinshi Knight'),
        ('Snpr', 'Sniper'),
        ('Brsrkr', 'Berserker'),
        ('Hr', 'Hero'),
        ('Bw Knght', 'Bow Knight'),
        ('Advntrr', 'Adventurer'),
        ('Wyvrn Lrd', 'Wyvern Lord'),
        ('Mlg Knght', 'Malig Knight'),
        ('Srcrr', 'Sorcerer'),
        ('Drk Knght', 'Dark Knight'),
        ('Strtgst', 'Strategist'),
        ('Btlr', 'Butler'),
        ('Md', 'Maid'),
        ('Drd Fghtr', 'Dread Fighter'),
        ('Drk Flr', 'Dark Flier'),
        ('Ldstr', 'Lodestar'),
        ('Grt Lrd', 'Great Lord'),
        ('Vngrd', 'Vanguard'),
        ('Grndmstr', 'Grandmaster'),
        ('Wtch', 'Witch'),
        ('Bllstcn', 'Ballistician'),
        ('Wlfssngr', 'Wolfssegner'),
        ('Nntls', 'Ninetails'),
        ('Nhr Nbl', 'Nohr Noble'),
        ('Hshd Nbl', 'Hoshido Noble'),
    )
    name = models.CharField(choices=charNames)
    sex = models.CharField(max_length=10)
    classChar = models.CharField(choices=classFE)
    #gonna change VthisV  to a JobClass model

    hpG = models.IntegerField()
    strG = models.IntegerField()
    magS = models.IntegerField()
    skillG = models.IntegerField()
    spdG = models.IntegerField()
    lckG = models.IntegerField()
    defG = models.IntegerField()
    resG = models.IntegerField()
    hpB = models.IntegerField()
    strB = models.IntegerField()
    magB = models.IntegerField()
    skillB = models.IntegerField()
    spdB = models.IntegerField()
    lckB = models.IntegerField()
    defB = models.IntegerField()
    resB = models.IntegerField()