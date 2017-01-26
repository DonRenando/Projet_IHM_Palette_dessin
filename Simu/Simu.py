from time import sleep

from ivy.std_api import IvySendMsg

from LibCommon import myIvy

ivy = myIvy.MyIvy("Simu", "127.255.255.255:2010")

list_cmds = [
    (
        # Test création RECTANGLE, xy en premier -> REC1
        "Geste forme={}".format("RECTANGLE"),
        "PALETTE x={} y={}".format(25, 70),
        "sra5 Parsed=VOCAL couleur={} confiance=0,99".format("rouge"),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ici"),
    ),
    (
        # Test création ROND, xy en premier -> RON1
        "Geste forme={}".format("ROND"),
        "PALETTE x={} y={}".format(250, 300),
        "sra5 Parsed=VOCAL couleur={} confiance=0,99".format("bleu"),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ici"),
    ),
    (
        # Test création RECTANGLE, couleur en premier REC2
        "Geste forme={}".format("RECTANGLE"),
        "PALETTE x={} y={}".format(10, 425),
        "sra5 Parsed=VOCAL couleur={} confiance=0,99".format("jaune"),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ici"),
    ),
    (
        # Test création ROND, couleur en premier RON2
        "Geste forme={}".format("ROND"),
        "PALETTE x={} y={}".format(300, 400),
        "sra5 Parsed=VOCAL couleur={} confiance=0,99".format("vert"),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ici"),
    ),
    ########################################################################################################################
    (
        # Test supression RECTANGLE, sans couleur annonce REC2
        "Geste forme={}".format("Z"),
        "sra5 Parsed=VOCAL couleur={} confiance=0,99".format("jaune"),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ce rectangle"),
        "PALETTE x={} y={}".format(15, 435),
    ),
    (
        # Test supression ROND, avec couleur annonce RON2
        "Geste forme={}".format("Z"),
        "sra5 Parsed=VOCAL couleur={} confiance=0,99".format("vert"),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ce rond"),
        "PALETTE x={} y={}".format(300, 450),
    ),
    ########################################################################################################################
    (
        # Test deplacement RECTANGLE, ça d'abord -> REC1
        "Geste forme={}".format("TRAIT"),
        "PALETTE x={} y={}".format(30, 80),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ça"),
        "PALETTE x={} y={}".format(600, 450),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("là"),
    ),
    (
        # Test deplacement RECTANGLE, la d'abord -> REC1
        "Geste forme={}".format("TRAIT"),
        "PALETTE x={} y={}".format(610, 460),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("ça"),
        "PALETTE x={} y={}".format(600, 100),
        "sra5 Parsed=VOCAL action={} confiance=0,99".format("là"),
    ),
]

for cmds in list_cmds:
    sleep(5)
    for cmd in cmds:
        print(cmd)
        IvySendMsg(cmd)
        sleep(1)
exit(0)
