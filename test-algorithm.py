import unittest
import numpy as np
from algorithm import simplex
import traceback

class TestSimplex(unittest.TestCase):
    
    def test_basic_case(self):
        """Test the example from your original test file"""
        print("\n=== Test Case 1: Basic Case ===")
        c = np.array([3, 2])
        A = np.array([[2, 1], [1, 2]])
        b = np.array([18, 14])
        
        try:
            print(f"Input - c: {c}, A: {A}, b: {b}")
            result = simplex(c, A, b)
            print(f"Result type: {type(result)}")
            print(f"Result length: {len(result)}")
            
            # Try different unpacking scenarios
            if len(result) == 3:
                solution, z_value, tableau = result
                print(f"✅ 3-value unpacking successful")
                print(f"  Solution: {solution}")
                print(f"  Z-value: {z_value}")
                print(f"  Tableau shape: {tableau.shape}")
                self.assertTrue(np.allclose(solution, [5.2, 4.4], atol=1e-1))
                
            elif len(result) == 2:
                solution, z_value = result
                print(f"✅ 2-value unpacking successful") 
                print(f"  Solution: {solution}")
                print(f"  Z-value: {z_value}")
                self.assertTrue(np.allclose(solution, [5.2, 4.4], atol=1e-1))
                
            else:
                self.fail(f"Unexpected result format: {len(result)} values returned")
                
        except Exception as e:
            print(f"❌ Error: {e}")
            traceback.print_exc()
            self.fail(f"Simplex function failed: {e}")
    
    def test_simple_case(self):
        """Test a very simple case"""
        print("\n=== Test Case 2: Simple Case ===")
        c = np.array([1.0, 1.0])  # Maximize x1 + x2
        A = np.array([[1.0, 1.0],  # x1 + x2 <= 10
                      [2.0, 1.0]])  # 2x1 + x2 <= 15
        b = np.array([10.0, 15.0])
        
        try:
            print(f"Input - c: {c}, A: {A}, b: {b}")
            result = simplex(c, A, b)
            print(f"Result: {result}")
            
            # Test unpacking
            solution, z_value, tableau = result
            print(f"✅ Unpacking successful")
            print(f"  Solution: {solution}")
            print(f"  Z-value: {z_value}")
            
            # Basic checks
            self.assertIsInstance(solution, np.ndarray)
            self.assertIsInstance(z_value, (int, float, np.number))
            self.assertIsInstance(tableau, np.ndarray)
            
        except ValueError as e:
            if "too many values to unpack" in str(e):
                print(f"❌ FOUND THE UNPACKING ERROR: {e}")
                print("This is the error you're getting in Streamlit!")
                result = simplex(c, A, b)
                print(f"Actual result: {result}")
                print(f"Type: {type(result)}")
                print(f"Length: {len(result) if hasattr(result, '__len__') else 'No length'}")
            raise
        except Exception as e:
            print(f"❌ Other error: {e}")
            traceback.print_exc()
            raise
    
    def test_streamlit_scenario(self):
        """Test the exact scenario from Streamlit"""
        print("\n=== Test Case 3: Streamlit Default Scenario ===")
        # These are the default values from your Streamlit app
        c = np.array([1.0, 1.0])  # Default coefficients
        A = np.array([[1.0, 1.0],  # Default constraint matrix
                      [1.0, 1.0]])
        b = np.array([10.0, 10.0])  # Default bounds
        
        try:
            print(f"Input - c: {c}, A: {A}, b: {b}")
            result = simplex(c, A, b)
            
            print(f"Raw result: {result}")
            print(f"Result type: {type(result)}")
            
            if hasattr(result, '__len__'):
                print(f"Result length: {len(result)}")
                for i, item in enumerate(result):
                    print(f"  Item {i}: {item} (type: {type(item)})")
            
            # Try the exact unpacking from your app
            solution, z_value, tableau = result
            print(f"✅ Streamlit unpacking successful")
            
        except Exception as e:
            print(f"❌ Streamlit scenario failed: {e}")
            traceback.print_exc()
            raise

def debug_simplex_function():
    """Additional debugging outside unittest"""
    print("\n" + "="*50)
    print("DEBUGGING SIMPLEX FUNCTION")
    print("="*50)
    
    c = np.array([1.0, 1.0])
    A = np.array([[1.0, 1.0], [1.0, 1.0]])
    b = np.array([10.0, 10.0])
    
    try:
        print("Calling simplex function...")
        result = simplex(c, A, b)
        
        print(f"Function returned: {result}")
        print(f"Type: {type(result)}")
        
        if isinstance(result, tuple):
            print(f"Tuple length: {len(result)}")
            for i, item in enumerate(result):
                print(f"  Element {i}: {item}")
                print(f"    Type: {type(item)}")
                if hasattr(item, 'shape'):
                    print(f"    Shape: {item.shape}")
        
        # Test unpacking
        print("\nTesting unpacking...")
        a, b_val, c_val = result
        print("✅ Unpacking successful!")
        
    except Exception as e:
        print(f"❌ Debug failed: {e}")
        traceback.print_exc()

if __name__ == '__main__':
    # Run debug first
    debug_simplex_function()
    
    # Then run unit tests
    print("\n" + "="*50)
    print("RUNNING UNIT TESTS")
    print("="*50)
    unittest.main(verbosity=2)