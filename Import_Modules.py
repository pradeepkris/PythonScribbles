
# INSTALL LOCATION : Package included directly in the install location
import pradmod
print pradmod.__path__

# Version of import that will load module "hello world"
# into current script symbol table
from pradmod import helloworld as h
h.greet("from Install Location ..");
print '-----------'

# Version of import that loads function "greet" from "helloworld" module
# into current script symbol table
from pradmod.helloworld import greet as g
g("Kavin Pradeep")
print '-----------'
#############################################################################

# SYS PATH : Added to PATH environment variable
import My_Lib
print My_Lib.__path__

from My_Lib.HelloWorld import greet as abc
abc("from SYS PATH env ..")
print '-----------'
#############################################################################

# PACKAGES: More Packages to My_Lib         -----> Call 1
from My_Lib.PKG1 import Mod1
Mod1.greet("from PACKAGES ..")
print '-----------'

# Another way                               -----> Call 2
from My_Lib.PKG1.Mod1 import greet as xyz
xyz('Kavin')
print '-----------'

# Talk between packages                     -----> Call 3
from My_Lib.PKG2.Mod1 import greet as xyz
xyz('Kavin')
print '-----------'

#############################################################################
# These modles are defined in the same containing folder of calling script
# import Classes, Iterators
