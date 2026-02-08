# Erytha Scorpia: Neuro-Symbolic Cognitive Engine

![System](https://img.shields.io/badge/Architecture-Hybrid%20Neuro--Symbolic-purple) ![Profile](https://img.shields.io/badge/Optimization-ASD--1-blue)

**Erytha Scorpia** is the kernel implementation of the *Project Benjamin* cognitive architecture. It functions as a "digital prosthesis" for neurodivergent operators, translating the **Free Energy Principle** (Friston) into a Python-based executable for real-time decision support.

## 1. The Architecture
Scorpia does not "manage tasks." It manages **Cognitive Load** via three distinct layers:

### Layer 1: The Sensory Bus (Noise Cancellation)
* **Logic:** Non-linear gating of high-entropy signals (Social/Auditory) to protect low-entropy processing (Pattern Recognition).
* **Code:** `SensoryBus.integrate()` implements a custom weighted tanh function to normalize inputs.

### Layer 2: Predictive Cortex (The Oracle)
* **Logic:** Uses **Hierarchical Predictive Coding** to forecast energy expenditure.
* **Math:** $\theta_{t+1} = \theta_t - \eta \nabla \mathcal{L}$ (Gradient descent on prediction error).
* **Target:** Maintains Mean Absolute Percentage Error (MAPE) ≤ 15%.

### Layer 3: Plasticity Engine (The Rewire)
* **Logic:** Implements **Spike-Timing Dependent Plasticity (STDP)**.
* **Function:** When MAPE > 15%, the system triggers aggressive Hebbian updates to "learn" the stressor and adapt the predictive model.

## 2. Usage
Scorpia is designed to run as a background daemon, processing environmental metrics.

```bash
# Clone the Scorpia Kernel
git clone [https://github.com/your-username/erytha-scorpia](https://github.com/your-username/erytha-scorpia)

# Run the Simulation
python scorpia_kernel.py
3. Theoretical Basis
• Neuroscience: Hebbian Learning, STDP, Friston's Free Energy Principle.
• Systems Theory: The 100-Metric Relationship Framework (Interlinkage Logic).
• Philosophy: "Suffering is Architectural" (Webb, 2026).
4. License
Proprietary Research Preview.
(c) 2026 Benjamin Webb.
