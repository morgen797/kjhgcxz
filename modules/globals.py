# -*- coding: utf_8 -*-
from modules.character import character
import direct.directbase.DirectStart
from pandac.PandaModules import CollisionTraverser

base.cTrav=CollisionTraverser()
player=character('res/actors/gnum',{'stand':'res/actors/gnum-stand','walk':'res/actors/gnum-walk'},base.cTrav,0)
player.model.setScale(0.3)
taskMgr.add(player.update,'char_update')