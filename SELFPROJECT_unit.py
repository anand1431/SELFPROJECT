import SELFPROJECT
import unittest

class Tester(unittest.TestCase):
    def test_cond1(ak):
        obj1=SELFPROJECT.Randomroll()
        ak.assertEqual(obj1.rolling(-2,-10),"invalid try again")
        ak.assertEqual(obj1.rolling(0,0),"invalid try again")
        ak.assertEqual(obj1.rolling(-2,10),"invalid try again")
        ak.assertEqual(obj1.rolling(-10,0),"invalid try again")
        ak.assertEqual(obj1.rolling(2,-10),"invalid try again")
        ak.assertEqual(obj1.rolling(-2,-10),"invalid try again")
        ak.assertEqual(obj1.rolling(12,1),"invalid try again")
        ak.assertEqual(obj1.rolling(0,10),"invalid try again")
    
    def test_cond2(ak):
        obj2=SELFPROJECT.Randomroll()
        ak.assertIn(obj2.rolling(1,6),range(1,6))   
        ak.assertIn(obj2.rolling(14,31),range(14,31))
        ak.assertIn(obj2.rolling(3,11),range(3,11))
        ak.assertIsNot(obj2.rolling(1,6),range(7,11))
    
        


if __name__ == "__main__":
    unittest.main()