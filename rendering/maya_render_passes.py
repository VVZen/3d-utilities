# brought you by

# dP    dP .d8888b. .d8888b. 
# 88    88 88'  `88 Y8ooooo. 
# 88.  .88 88.  .88       88 
# `8888P88 `88888P8 `88888P' 
#      .88                   
#  d8888P                    
    

import maya.mel as mel
import pymel.core as pm          
import maya.cmds as cmd

### CREATING THE NEW RENDER LAYER

renderLayerName = "rl_beauty"
cmd.createRenderLayer (name = renderLayerName, number = 1, empty = True)


### GLOBAL VARIABLES INITIALISING ###

passNames = ["ambient", "diffkey", "difffill", "diffrim", 
"diffextrar", "diffextrag", "diffextrab", "shdkey", "shdfill", 
"shdrim", "shdextrar", "shdextrag", "id01", "id02", "id03", "id04",
"specular", "reflection", "mvector", "normal", "matte"]



### CREATING THE RENDER PASSES ###

# General Create Pass Function
def createPass(passName):
    # Matte 
    if (passName == "matte"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "MATTE")
    # Ids 
    elif (passName[0:2] == "id"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "CSTCOL")
    # Ambient
    elif (passName[0:3] == "amb"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "CSTCOL")
    # Diffuse  
    elif (passName[0:3] == "dif"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "DIFF")
    # Shadows 
    elif (passName[0:3] == "shd"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "SHD")
    # Specular
    elif (passName[0:3] == "spe"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "SPEC")    
    # Reflection
    elif (passName[0:3] == "ref"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "REFL")
    # Normal
    elif (passName[0:3] == "nor"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "NORMAL")
    # Motion Vector
    elif (passName[0:3] == "mve"):
        cmd.shadingNode ("renderPass", asRendering = True, n = passName)
        cmd.setRenderPassType (passName, type = "MV2N")
# General Attributes    
    cmd.setAttr (passName + ".frameBufferType", 2)
    if (passName != "specular" and passName != "reflection" and passName != "mvector" and passName != "normal"
    and passName != "matte"):
        cmd.setAttr (passName + ".useTransparency", 1)
        cmd.setAttr (passName + ".transparentAttenuation", 1)
    
## CREATING THE RENDER PASSES AND CONTRIBUTION MAPS AND CONNECTING RENDER PASSES TO CONTRIBUTION MAPS

for i in passNames:
    createPass(i)
    mel.eval("renderLayerEditorCreateContMap RenderLayerTab %s 0" %(renderLayerName))
    mel.eval('renderLayerEditorItemOnRename "rl_beauty%passContributionMap1"' + i + "CM")
    cmd.connectAttr(renderLayerName + ".renderPass", i + ".owner", nextAvailable = True)
    cmd.connectAttr(i + ".message", i + "CM" +".renderPass", nextAvailable = True)