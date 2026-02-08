from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from scorpia_kernel import ErythaScorpia

# INITIALIZE THE API
app = FastAPI(title="Erytha Scorpia API", version="3.0.0")

# INITIALIZE THE BRAIN (Persistent State)
brain = ErythaScorpia()

# DATA MODELS (The Schema)
class SensoryInput(BaseModel):
    auditory: float  # 0.0 to 1.0
    visual: float
    proprioceptive: float
    social: float

class SystemStatus(BaseModel):
    homeostasis_index: float
    current_mape: float
    plasticity_active: bool

@app.get("/")
def health_check():
    return {"status": "ONLINE", "system": "Erytha Scorpia v3.0"}

@app.post("/ingest", response_model=SystemStatus)
def ingest_sensory_data(data: SensoryInput):
    """
    Endpoint for wearable devices to push environmental biometric data.
    """
    # Convert API model to list for the Kernel
    raw_vector = [data.auditory, data.visual, data.proprioceptive, data.social]
    
    # Process Frame
    try:
        brain.process_frame(raw_vector)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # Return Cognitive State
    return SystemStatus(
        homeostasis_index=brain.state.homeostasis_index,
        current_mape=brain.state.current_mape,
        plasticity_active=brain.state.current_mape > 15.0
    )

@app.get("/diagnostic")
def get_neuroplasticity_metrics():
    """
    Returns the current synaptic weight matrix (heatmap data).
    """
    return {
        "synaptic_weights": brain.plasticity.synapses.tolist(),
        "predictive_priors": brain.cortex.priors.tolist()
    }
