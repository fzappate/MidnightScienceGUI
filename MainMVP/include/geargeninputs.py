class GearGenInputs():
    '''This class is meant to be as close as possible to a simple collection of inputs.
    The actions should be performed by the methods of it's parent class GearGenControls'''

    def __init__(self)->None: 
        '''Initialize the GearGen input object.'''

        self.inputFileFound = False 
        
        # Input lists
        self.i1 = self.BuildDict('N1','Number of teeth for pinion gear.','N1 (number of teeth for pinion gear)')
        self.i2 = self.BuildDict('m1','Module of gear1. m=D_ref_1/N1, mm.','m1 (module of gear1. m=D_ref_1/N1, mm)')  
        self.i3 = self.BuildDict('alpha_ref_1','pressure angle at reference circle, rad','alpha_ref_1 (pressure angle at reference circle, rad)')
        self.i4 = self.BuildDict('r_ded_1','Pinion gear dedendum circle radius (mm)','r_ded_1 (pinion gear dedendum circle radius (mm)')
        self.i5 = self.BuildDict('r_add_1','Pinion gear addendum circle radius (mm)','r_add_1 (pinion gear addendum circle radius (mm)')
        self.i6 = self.BuildDict('N2','Number of teeth for ring gear','N2 (number of teeth for ring gear)')
        self.i7 = self.BuildDict('E','Center distance, mm','E (center distance, mm)')
        self.i8 = self.BuildDict('m2','Mdule of gear2. m=D_ref_2/N2, mm','m2 (module of gear2. m=D_ref_2/N2, mm)')
        self.i9 = self.BuildDict('r_ded_2','Ring gear dedendum circle radius (mm)','r_ded_2 (ring gear dedendum circle radius (mm)')
        self.i10 = self.BuildDict('r_fillet','Fillet radius gear 1 root, mm','r_fillet (fillet radius gear 1 root, mm)')
        self.i11 = self.BuildDict('r_s','Shaft radius mm','r_s (shaft radius mm)')
        self.i12 = self.BuildDict('n','outer gear rotation velocity, rev/min','n (outer gear rotation velocity, rev/min)')
        self.i13 = self.BuildDict('lateral clearance','lateral clearance one side (um)','lateral clearance one side (um)')
        self.i14 = self.BuildDict('tip clearance','','tip clearance (um)')
        self.i15 = self.BuildDict('dr_G2','','dR_G2 (outside circle radius of ring gear minus to its max involute radius, mm)')
        self.i16 = self.BuildDict('min gear tip','','minimal gear tip length allowable (for both gears, mm)')
        self.i17 = self.BuildDict('Q','','Q (required outlet flow, L/min)')
        self.i18 = self.BuildDict('CRmin','','CRmin (minimal Contact ratio)')
        self.i19 = self.BuildDict('mean vel','','mean velocity calculation window range (for either side,the total window will double this angle value, deg)')
        self.i20 = self.BuildDict('rad port diam','','radial port diameter (expressed as a percentage of the gear axial length. No port: 0.00)')

        # Combine the Inputs
        self.dictCollection = [ self.i1, self.i2, self.i3,self.i4,self.i5,self.i6,self.i7,self.i8,self.i9,self.i10,
                                self.i11, self.i12, self.i13, self.i14, self.i15, self.i16,self.i17,self.i18,self.i19,self.i20 ]


    def BuildDict(self,name,desc = None,fileEntry = None, img = None, type = None, val = 1)->dict:
        """This function ease the construction of the dictionary list."""

        dict = {'name': name,
            'description': desc,
            'inputHeader': fileEntry,
            'image': img,
            'type': type,
            'value': val}
        
        return dict

    
    def GetValueFromDictionary(self,nameTarget:str)->float:
        """This function takes as input the name of an input entry and retrieve 
         its value from the input dictionary."""
        
        for dict in self.dictCollection:
            nameTemp = dict["name"]
            if (nameTemp ==nameTarget):
                return dict["value"]


            

    

