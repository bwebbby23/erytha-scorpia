import numpy as np
import logging
from dataclasses import dataclass
from typing import List, Tuple

# ERYTHA SCORPIA: COGNITIVE OPTIMIZATION KERNEL v3.0
# "Suffering is Architectural." - System Axiom

logging.basicConfig(level=logging.INFO, format='[SCORPIA] %(message)s')
np.random.seed(42)

@dataclass
class ScorpiaState:
    homeostasis_index: float = 1.0
    plasticity_rate: float = 0.01
    current_mape: float = 0.0

class SensoryBus:
    """
    Layer 4: Multisensory Integration Bus
    Filters high-noise social signals for ASD-1 hardware optimization.
    """
    def __init__(self):
        # Weighting: [Auditory, Visual, Proprioceptive, Social]
        # Scorpia Logic: Aggressive dampening of Auditory/Social noise
        self.weights = np.array([0.05, 0.45, 0.45, 0.05]) 
        self.noise_gate = 0.2
        
    def integrate(self, signals: np.ndarray) -> float:
        # Signal Gating (Non-linear filter)
        gated = np.where(signals > self.noise_gate, signals, 0)
        # Weighted Integration
        integrated_load = np.dot(gated, self.weights)
        return np.tanh(integrated_load) # Normalize 0-1

class PredictiveCortex:
    """
    Layer 3: Hierarchical Predictive Coding
    Uses Bayesian priors to forecast sensory load.
    """
    def __init__(self, dim: int = 64):
        self.priors = np.random.normal(0, 0.1, dim)
        self.learning_rate = 0.05
        
    def forecast(self, context: np.ndarray) -> float:
        # Belief Projection
        prediction = np.dot(self.priors, context)
        return 1 / (1 + np.exp(-prediction)) # Sigmoid activation

    def update_priors(self, error: float, context: np.ndarray):
        # Gradient Descent on Free Energy (Prediction Error)
        grad = error * context
        self.priors -= self.learning_rate * grad

class PlasticityEngine:
    """
    Layer 2: STDP & Hebbian Rewiring
    Manages the 'Burnout Threshold' via synaptic weight adjustments.
    """
    def __init__(self, dim: int = 64):
        self.synapses = np.eye(dim)
        
    def adapt(self, activation: np.ndarray, error_mag: float):
        # Hebbian Rule: Fire together, wire together
        # Modulated by Error Magnitude (Frustration Signal)
        co_activation = np.outer(activation, activation)
        delta_w = 0.01 * co_activation * (1 + error_mag)
        
        self.synapses += delta_w
        # Normalization to prevent runaway excitation (Seizure/Panic prevention)
        self.synapses /= np.max(np.abs(self.synapses))

class ErythaScorpia:
    def __init__(self):
        self.bus = SensoryBus()
        self.cortex = PredictiveCortex()
        self.plasticity = PlasticityEngine()
        self.state = ScorpiaState()
        
    def process_frame(self, raw_inputs: List[float]):
        """
        Executes one 200ms cognitive frame.
        """
        # 1. Ingest
        inputs = np.array(raw_inputs)
        load = self.bus.integrate(inputs)
        
        # 2. Contextualize (Generate embedding)
        context = np.random.normal(load, 0.1, 64)
        
        # 3. Predict
        forecast = self.cortex.forecast(context)
        
        # 4. Error Calculation (MAPE)
        # Reality is simulated here as the raw integrated load
        reality = load
        error = np.abs(forecast - reality)
        self.state.current_mape = error * 100
        
        # 5. Homeostatic Check
        if self.state.current_mape > 15.0:
            logging.warning(f"MAPE CRITICAL ({self.state.current_mape:.2f}%). REWIRING ACTIVE.")
            self.cortex.update_priors(error, context)
            self.plasticity.adapt(context, error)
        else:
            logging.info(f"System Nominal. MAPE: {self.state.current_mape:.2f}%")

if __name__ == "__main__":
    # Simulate High-Stress Environment (Party/Crowd)
    # [Auditory (High), Visual (Med), Proprioceptive (Low), Social (High)]
    env_stress = [0.9, 0.5, 0.2, 0.95]
    
    scorpia = ErythaScorpia()
    
    for i in range(5):
        logging.info(f"--- FRAME {i} ---")
        scorpia.process_frame(env_stress)
