import string
import random

class Generator :

    def __init__(self) :

        self.LENGTH = 16

    def generate( self ):

        asciiDigits = string.ascii_letters + string.digits

        generateResult = "".join( [random.choice(asciiDigits) for _ in range(self.LENGTH)] )

        stripeGenerateResult = ""

        for stripeGenerate in range(len(generateResult)):

            if ((stripeGenerate == 4)|(stripeGenerate == 8)|(stripeGenerate == 12)) :

                stripeGenerateResult += "-"
                stripeGenerateResult += generateResult[stripeGenerate]

            else :

                stripeGenerateResult += generateResult[stripeGenerate]

        return stripeGenerateResult