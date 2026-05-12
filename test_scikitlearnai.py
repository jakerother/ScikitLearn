# test_scikitlearnai.py
"""
Tests for ScikitLearnAI module.
"""

import unittest
from scikitlearnai import ScikitLearnAI

class TestScikitLearnAI(unittest.TestCase):
    """Test cases for ScikitLearnAI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ScikitLearnAI()
        self.assertIsInstance(instance, ScikitLearnAI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ScikitLearnAI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
