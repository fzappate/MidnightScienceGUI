class GeomCodeInputs():
    '''This class is meant to be as close as possible to a simple collection of inputs.
    The actions should be performed by the methods of it's parent class GearGenControls'''

    def __init__(self)->None:
        '''Initialize the GearGen input object.'''

        self.inputFileFound = False 
        self.gearParaDictFound = False 
        self.radialRecessFound = False 
        
        self.dictCollection = []

        # Input lists
        self.i1 = self.BuildEntryDict('TableName','Name given to the geometry table.','Geometry table name:')
        self.i1['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i1)
        self.i2 = self.BuildEntryDict('PrintActivate','Specify whether the geometry code output graphical features ot not. Input ''1'' or ''0''.','Print activate:')  
        self.i2['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i2)
        self.i3 = self.BuildEntryDict('PrintFormat','Specify the format of the graphical output files. Input ''.vtk'',''.txt.., or''none''.','Input folder:')  
        self.i3['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i3)

        self.i4 = self.BuildEntryDict('N1','Pinion number of teeth.','N1')
        self.i4['pane'] = 'Gear Dictionary'
        self.i4['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i4)
        self.i5 = self.BuildEntryDict('N2','Ring gear number of teeth.','N2')
        self.i5['pane'] = 'Gear Dictionary'
        self.i5['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i5)
        self.i6 = self.BuildEntryDict('rG2_out','To be updated.','rG2_out')
        self.i6['pane'] = 'Gear Dictionary'
        self.i6['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i6)
        self.i7 = self.BuildEntryDict('gear_thickness','To be updated.','gear_thickness')
        self.i7['pane'] = 'Gear Dictionary'
        self.i7['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i7)
        self.i8 = self.BuildEntryDict('range_Xita','To be updated.','range_Xita')
        self.i8['pane'] = 'Gear Dictionary'
        self.i8['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i8)
        self.i9 = self.BuildEntryDict('range_Xita2','To be updated.','range_Xita2')
        self.i9['pane'] = 'Gear Dictionary'
        self.i9['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i9)
        self.i10 = self.BuildEntryDict('r_ref_1','To be updated.','r_ref_1')
        self.i10['pane'] = 'Gear Dictionary'
        self.i10['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i10)
        self.i11 = self.BuildEntryDict('alpha_ref_1','To be updated.','alpha_ref_1')
        self.i11['pane'] = 'Gear Dictionary'
        self.i11['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i11)
        self.i12 = self.BuildEntryDict('rb1','To be updated.','rb1')
        self.i12['pane'] = 'Gear Dictionary'
        self.i12['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i12)
        self.i13= self.BuildEntryDict('E','To be updated.','E')
        self.i13['pane'] = 'Gear Dictionary'
        self.i13['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i13)
        self.i14 = self.BuildEntryDict('rp1','To be updated.','rp1')
        self.i14['pane'] = 'Gear Dictionary'
        self.i14['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i14)
        self.i15 = self.BuildEntryDict('fi1','To be updated.','fi1')
        self.i15['pane'] = 'Gear Dictionary'
        self.i15['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i15)
        self.i16 = self.BuildEntryDict('fi2','To be updated.','fi2')
        self.i16['pane'] = 'Gear Dictionary'
        self.i16['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i16)
        self.i17 = self.BuildEntryDict('rb2','To be updated.','rb2')
        self.i17['pane'] = 'Gear Dictionary'
        self.i17['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i17)
        self.i18 = self.BuildEntryDict('alpha_p1','To be updated.','alpha_p1')
        self.i18['pane'] = 'Gear Dictionary'
        self.i18['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i18)
        self.i19 = self.BuildEntryDict('C1','To be updated.','C1')
        self.i19['pane'] = 'Gear Dictionary'
        self.i19['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i19)
        self.i20 = self.BuildEntryDict('C1','To be updated.','C1')
        self.i20['pane'] = 'Gear Dictionary'
        self.i20['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i20)
        self.i21 = self.BuildEntryDict('C2','To be updated.','C2')
        self.i21['pane'] = 'Gear Dictionary'
        self.i21['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i21)
        self.i22 = self.BuildEntryDict('C2','To be updated.','C2')
        self.i22['pane'] = 'Gear Dictionary'
        self.i22['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i22)
        self.i23 = self.BuildEntryDict('ra1','To be updated.','ra1')
        self.i23['pane'] = 'Gear Dictionary'
        self.i23['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i23)
        self.i24 = self.BuildEntryDict('MoreCutRatio','To be updated.','MoreCutRatio')
        self.i24['pane'] = 'Gear Dictionary'
        self.i24['entryType'] = 'LabelHelpEntry'        
        self.dictCollection.append(self.i24)
        self.i25 = self.BuildEntryDict('rT2_small','To be updated.','rT2_small')
        self.i25['pane'] = 'Gear Dictionary'
        self.i25['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i25)
        self.i26= self.BuildEntryDict('rT2_big','To be updated.','rT2_big')
        self.i26['pane'] = 'Gear Dictionary'
        self.i26['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i26)
        self.i27 = self.BuildEntryDict('rT1_small','To be updated.','rT1_small')
        self.i27['pane'] = 'Gear Dictionary'
        self.i27['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i27)
        self.i28 = self.BuildEntryDict('rT1_big','To be updated.','rT1_big')
        self.i28['pane'] = 'Gear Dictionary'
        self.i28['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i28)
        self.i29 = self.BuildEntryDict('AngleCrecG1_L','To be updated.','AngleCrecG1_L')
        self.i29['pane'] = 'Gear Dictionary'
        self.i29['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i29)
        self.i30 = self.BuildEntryDict('AngleCrecG1_R','To be updated.','AngleCrecG1_R')
        self.i30['pane'] = 'Gear Dictionary'
        self.i30['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i30)
        self.i31 = self.BuildEntryDict('AngleCrecG2_L','To be updated.','AngleCrecG2_L')
        self.i31['pane'] = 'Gear Dictionary'
        self.i31['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i31)
        self.i32 = self.BuildEntryDict('AngleCrecG2_R','To be updated.','AngleCrecG2_R')
        self.i32['pane'] = 'Gear Dictionary'
        self.i32['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i32)
        self.i33 = self.BuildEntryDict('CrecG2_ratio','To be updated.','CrecG2_ratio')
        self.i33['pane'] = 'Gear Dictionary'
        self.i33['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i33)
        self.i34 = self.BuildEntryDict('ACrecG2_gapL','To be updated.','ACrecG2_gapL')
        self.i34['pane'] = 'Gear Dictionary'
        self.i34['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i34)
        self.i35 = self.BuildEntryDict('ACrecG2_gapR','To be updated.','ACrecG2_gapR')
        self.i35['pane'] = 'Gear Dictionary'
        self.i35['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i35)
        self.i36 = self.BuildEntryDict('inlet_ang_upstart','To be updated.','inlet_ang_upstart')
        self.i36['pane'] = 'Recess Dictionary'
        self.i36['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i36)
        self.i37 = self.BuildEntryDict('inlet_ang_upend','To be updated.','inlet_ang_upend')
        self.i37['pane'] = 'Recess Dictionary'
        self.i37['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i37)
        self.i38 = self.BuildEntryDict('inlet_dR_up','To be updated.','inlet_dR_up')
        self.i38['pane'] = 'Recess Dictionary'
        self.i38['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i38)        
        self.i39 = self.BuildEntryDict('inlet_ang_downstart','To be updated.','inlet_ang_downstart')
        self.i39['pane'] = 'Recess Dictionary'
        self.i39['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i39)        
        self.i40 = self.BuildEntryDict('inlet_ang_downend','To be updated.','inlet_ang_downend')
        self.i40['pane'] = 'Recess Dictionary'
        self.i40['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i40)        
        self.i41 = self.BuildEntryDict('inlet_dR_down','To be updated.','inlet_dR_down')
        self.i41['pane'] = 'Recess Dictionary'
        self.i41['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i41)        
        self.i42 = self.BuildEntryDict('outlet_ang_upstart','To be updated.','outlet_ang_upstart')
        self.i42['pane'] = 'Recess Dictionary'
        self.i42['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i42)         
        self.i43 = self.BuildEntryDict('outlet_ang_upend','To be updated.','outlet_ang_upend')
        self.i43['pane'] = 'Recess Dictionary'
        self.i43['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i43)        
        self.i44 = self.BuildEntryDict('outlet_dR_up','To be updated.','outlet_dR_up')
        self.i44['pane'] = 'Recess Dictionary'
        self.i44['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i44)        
        self.i45 = self.BuildEntryDict('outlet_ang_downstart','To be updated.','outlet_ang_downstart')
        self.i45['pane'] = 'Recess Dictionary'
        self.i45['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i45)        
        self.i46 = self.BuildEntryDict('outlet_ang_downend','To be updated.','outlet_ang_downend')
        self.i46['pane'] = 'Recess Dictionary'
        self.i46['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i46)        
        self.i47 = self.BuildEntryDict('outlet_dR_down','To be updated.','outlet_dR_down')
        self.i47['pane'] = 'Recess Dictionary'
        self.i47['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i47)        
        self.i48 = self.BuildEntryDict('R_G2_radial_hole','To be updated.','R_G2_radial_hole')
        self.i48['pane'] = 'Recess Dictionary'
        self.i48['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i48)        
        self.i49 = self.BuildEntryDict('convention','To be updated.','convention')
        self.i49['pane'] = 'Recess Dictionary'
        self.i49['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i49)         
        self.i50 = self.BuildEntryDict('holes_each_TSV','To be updated.','holes_each_TSV')
        self.i50['pane'] = 'Recess Dictionary'
        self.i50['entryType'] = 'LabelHelpEntry'
        self.dictCollection.append(self.i50)

        self.i51 = self.BuildExpandableListDict('LateralFeature','To be updated.','Lateral features profile path:')
        self.i51['pane'] = 'Lateral Features'
        self.i51['entryType'] = 'ExpandableList'
        self.dictCollection.append(self.i51)

        self.i52 = self.BuildExpandableListDict('LateralGrooves','To be updated.','Lateral grooves profile path::')
        self.i52['pane'] = 'Lateral Grooves'
        self.i52['entryType'] = 'ExpandableList'
        self.dictCollection.append(self.i52)


    def BuildEntryDict(self,name,desc = None,fileEntry = None, img = None, type = None, val = None, pane = None,entryTipe = None)->dict:
        """This function ease the construction of the dictionary list."""

        dict = {'name': name,
                'description': desc,
                'inputHeader': fileEntry,
                'image': img,
                'type': type,
                'value': val,
                'pane':pane,
                'entryType':entryTipe}
        
        return dict

    def BuildExpandableListDict(self,name,desc = None,fileEntry = None, img = None, type = None, val = [], pane = None,entryTipe = None)->dict:
        """This function ease the construction of the dictionary list."""

        dict = {'name': name,
                'description': desc,
                'inputHeader': fileEntry,
                'image': img,
                'type': type,
                'value': val,
                'pane':pane,
                'entryType':entryTipe}
        
        return dict



    def GetValueFromDictionary(self,nameTarget:str)->float:
        """This function takes as input the name of an input entry and retrieve 
         its value from the input dictionary."""
        
        for dict in self.dictCollection:
            nameTemp = dict["name"]
            if (nameTemp ==nameTarget):
                return dict["value"]


            

    

