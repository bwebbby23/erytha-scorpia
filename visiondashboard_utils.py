import matplotlib.pyplot as plt
import numpy as np

def plot_cognitive_state(mape_history, plasticity_events):
    """
    Generates a clinical-grade visualization of the operator's cognitive stability.
    """
    plt.figure(figsize=(10, 6))
    
    # Plot Prediction Error (Stress)
    plt.plot(mape_history, label='Prediction Error (MAPE)', color='#FF4B4B', linewidth=2)
    
    # Plot Threshold
    plt.axhline(y=15.0, color='gray', linestyle='--', alpha=0.5, label='Burnout Threshold (15%)')
    
    # Highlight Plasticity Events (Rewiring)
    for event_time in plasticity_events:
        plt.axvline(x=event_time, color='#4BFF4B', alpha=0.3, label='STDP Event' if event_time == plasticity_events[0] else "")

    plt.title('Erytha Scorpia: Real-Time Cognitive Load Monitoring')
    plt.xlabel('Time (Frames)')
    plt.ylabel('Error Magnitude (%)')
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.savefig('cognitive_readout.png')
    print("[VISUAL] Saved cognitive_readout.png")
