# test_modelsync.py
"""
Tests for ModelSync module.
"""

import unittest
from modelsync import ModelSync

class TestModelSync(unittest.TestCase):
    """Test cases for ModelSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModelSync()
        self.assertIsInstance(instance, ModelSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModelSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
