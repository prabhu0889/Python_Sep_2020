# Way 01
import Learn_Modules.Module01

obj1 = Learn_Modules.Module01.Test_Leaf_02()
obj1.registration()

# Way 02
from Learn_Modules.Module01 import Test_Leaf_01
obj2 = Test_Leaf_01()
obj2.appium()
obj2.python()

# Way 03
from Learn_Modules.Module01 import Test_Leaf_01 as tl
#Test_Leaf_01.appium()
#tl.appium()
x = tl()
x.python()
x.appium()

# Way 04
from Learn_Modules.Module01 import Test_Leaf_01, Test_Leaf_02

# Way 05
from Learn_Modules.Module01 import Test_Leaf_01 as tl1, Test_Leaf_02 as tl2