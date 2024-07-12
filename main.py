# -*- coding: utf_8 -*-
import direct.directbase.DirectStart
from modules.location import gameLocation
#from modules.character import character
from pandac.PandaModules import Vec4,CollisionTraverser,BitMask32
from modules.control import mouseControl
from modules.globals import *

loc=gameLocation()
loc.loadTerrain('res/textures/heightfield.png')
loc.setTexture('res/textures/grass.png',20,20)
loc.setLights(Vec4(0.6,0.6,0.6,1), Vec4(1,1,1,1))

box=loader.loadModel('res/geometry/box')
box.reparentTo(render)
box.setScale(3)
box.setPos(35,35,loc.terrain.getElevation(35,35)*30)
box.find('**/+GeomNode').node().setIntoCollideMask(BitMask32.bit(2))

player.root.setPos(25,25,loc.terrain.getElevation(25,25)*30+5)
loc.camera.j1.setPos(player.root.getPos())

mc=mouseControl()
run()