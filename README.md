# Erytha Scorpia: Neuro-Symbolic Cognitive Architecture

![Status](https://img.shields.io/badge/System-Active-success) ![Architecture](https://img.shields.io/badge/Architecture-Hybrid%20Neuro--Symbolic-purple) ![Profile](https://img.shields.io/badge/Optimization-ASD--1-blue) ![License](https://img.shields.io/badge/License-MIT-green)

> **System Axiom:** "Suffering is not a moral failing; it is an architectural error." — *Benjamin Webb, 2026*

## 1. Executive Summary

**Erytha Scorpia** is the kernel implementation of the *Project Benjamin* cognitive architecture. It functions as a **Universal Optimization Engine**, translating the **Free Energy Principle** (Friston) and **Spike-Timing Dependent Plasticity** (STDP) into executable Python logic.

Unlike traditional AI agents that optimize for "task completion," Scorpia optimizes for **Homeostasis**. It treats high-entropy states (Cognitive Overload, Relational Conflict, Abstract Confusion) as "Prediction Errors" and resolves them via Bayesian inference and structural rewiring.

---

## 2. The Core Kernel (Neuro-Cognitive Layer)

The system's "Brain" (`scorpia_kernel.py`) manages energy expenditure via three biological layers designed to protect neurodivergent (ASD-1) hardware.

### Layer 1: The Sensory Bus (Noise Cancellation)
* **Objective:** Mitigate sensory overload and signal degradation.
* **Mechanism:** Non-linear gating of high-entropy signals (Social/Auditory) to protect low-entropy processing channels (Pattern Recognition).
* **Math:** $$S_{perceived} = \tanh\left(\frac{\sum w_i s_i}{\sum w_i}\right)$$

### Layer 2: Predictive Cortex (The Oracle)
* **Objective:** Minimize surprise (Free Energy) via Hierarchical Predictive Coding.
* **Mechanism:** Generates probabilistic forecasts of metabolic cost.
* **Optimization:** $\theta_{t+1} = \theta_t - \eta \nabla \mathcal{L}$ (Gradient descent on prediction error).
* **Target:** Mean Absolute Percentage Error (MAPE) ≤ 15%.

### Layer 3: Plasticity Engine (The Rewire)
* **Objective:** Prevent systemic burnout via structural adaptation.
* **Mechanism:** Implements **Spike-Timing Dependent Plasticity (STDP)**.
* **Trigger:** When MAPE > 15%, the system initiates aggressive Hebbian updates ("Fire together, wire together") to encode the stressor as a new reflex.

---

## 3. Universal Domain Modules

Scorpia demonstrates that **Optimization Logic is Domain-Agnostic**. The same kernel used for neural regulation is applied to social dynamics and pedagogy.

### A. Alignment Engine (`alignment.py`)
* **Domain:** Social Dynamics / Relationship Science.
* **Source:** *The 100-Metric Relationship Compatibility Framework*.
* **Logic:** Uses vector space modeling to calculate dyadic compatibility (`Euclidean Distance`).
* **Feature:** Natural Language Processing (NLP) that scans interaction logs for **"The Four Horsemen"** (Criticism, Contempt, Defensiveness, Stonewalling) to predict cascade failure.

### B. Codex Mapper (`codex_mapper.py`)
* **Domain:** Pedagogy / Information Theory.
* **Source:** *The Codex Method* (RCT Protocol).
* **Logic:** A NetworkX Knowledge Graph that maps **High-Entropy Inputs** (Abstract Formalisms) to **Low-Entropy Outputs** (Narrative Schemas).
* **Application:** Dynamically anchors abstract concepts (e.g., *Big-O Notation*) to somatic metaphors (e.g., *Traffic Jam*) to optimize retention and reduce cognitive load.

---

## 4. Installation & Usage

### Prerequisites
* Python 3.9+
* `numpy` (Tensor operations)
* `fastapi` (API Gateway)
* `networkx` (Graph Theory)

### Quick Start

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/erytha-scorpia.git](https://github.com/YOUR_USERNAME/erytha-scorpia.git)
cd erytha-scorpia

# 2. Install dependencies
pip install numpy fastapi uvicorn networkx

# 3. Run the Cognitive Kernel (Simulation)
python scorpia_kernel.py

# 4. Launch the API Server
uvicorn api:app --reload

5. API Documentation
The system exposes a RESTful interface via api.py for integration with wearables (Oura/Apple Watch) and external agents.
| Endpoint | Method | Description |
|---|---|---|
| /ingest | POST | Pushes environmental biometric data (Auditory, Visual, Proprioceptive, Social) to the Sensory Bus. |
| /diagnostic | GET | Returns real-time synaptic weight matrices and neuroplasticity heatmaps. |
| /status | GET | Returns current Homeostasis Index and Prediction Error (MAPE). |
6. Testing & Safety Protocols
Safety is architectural. The test_safety.py suite ensures the system adheres to biological limits.
python -m unittest test_safety.py

 * Social Damping Test: Verifies that social noise is filtered to protect ASD-1 cognitive resources.
 * Plasticity Trigger Test: Confirms structural rewiring only occurs when error exceeds the 15% threshold.
 * Epilepsy Guard: Prevents synaptic weight explosion during high-learning phases.
7. Theoretical Basis
This architecture is the synthesis of four distinct fields:
 * Computational Neuroscience: Hebbian Learning, STDP, and Friston's Free Energy Principle.
 * Systems Theory: The Project Benjamin Master Blueprint (Closed-loop recalibration).
 * Relationship Science: Gottman's Cascade Model of Dissolution.
 * Pedagogy: The Codex Method (Narrative-based Schema Mapping).
8. License
MIT License
Copyright (c) 2026 Benjamin Webb (Erytha Systems)
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

***
