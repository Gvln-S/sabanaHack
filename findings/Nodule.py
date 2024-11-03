class Nodule:
    noduleStateList = ["nodulo"]
    noduleNegationBefore=["no hay"]
    noduleConfirmationBefore=["si hay", "hay otro"]
    noduleConfirmationAfter=["cordenada"]
    noduleMorphologyAfter = ["ovalado", "ovalada", "irregular" , "redondo"]

    def __init__(self, containsNodule, morphology):
        self.containsNodule = containsNodule
        self.morphology = morphology

    def __str__(self):
        return f"Nodule: {self.containsNodule}" f" Morphology: {self.morphology}"




    
