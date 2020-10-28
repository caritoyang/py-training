# Complete structure -> Directory.Module (complete structure - all classes will be imported)
import Library.CommonModule

objA=Library.CommonModule.A()
objA.startBrowser()

objB=Library.CommonModule.B()
objB.startBrowser()

# FROM: we need to mention which class we want to import (it won't import all the classes)
# When creating the object, we don't need to specify the directory
from Library.CommonModule import A
objD=A()
objD.startBrowser()

######### fomr sub-directories #########
import Pages.Login.ABC
objC=Pages.Login.ABC.C()
objC.myTesting()

from Pages.Login.ABC import C
objE=C()
objE.myTesting()