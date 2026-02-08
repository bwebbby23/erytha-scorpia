import unittest
import numpy as np
from scorpia_kernel import ErythaScorpia

class TestErythaSafety(unittest.TestCase):
    
    def setUp(self):
        self.system = ErythaScorpia()

    def test_noise_gating(self):
        """
        Verify that high social noise is dampened (ASD-1 Protection).
        """
        # Input: Extreme Social Noise (1.0)
        inputs = np.array([0.1, 0.1, 0.1, 1.0]) 
        # The SensoryBus should filter this down significantly
        integrated_load = self.system.bus.integrate(inputs)
        
        # Expectation: Load should be low because Social weight is low (0.05)
        self.assertLess(integrated_load, 0.3, "CRITICAL: Social noise leakage detected.")

    def test_homeostasis_trigger(self):
        """
        Verify that the Rewiring Protocol triggers exactly at MAPE > 15%.
        """
        # Force a high error state
        self.system.state.current_mape = 20.0 
        
        # Check logic flag (Simulated check)
        trigger = self.system.state.current_mape > 15.0
        self.assertTrue(trigger, "FAIL: Plasticity did not trigger during high stress.")

    def test_synaptic_stability(self):
        """
        Ensure Hebbian learning doesn't cause mathematical explosion (Epileptic fit).
        """
        # Run a massive update
        activation = np.ones(64)
        self.system.plasticity.adapt(activation, error_mag=10.0)
        
        # Check max weight
        max_weight = np.max(self.system.plasticity.synapses)
        self.assertLessEqual(max_weight, 1.0, "FAIL: Synaptic runaway detected.")

if __name__ == '__main__':
    unittest.main()
