import numpy as np
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class OperatorProfile:
    id: str
    # Metric Category 1: Identity & Culture (Normalized 0.0 - 1.0)
    cultural_homogamy: float
    value_congruence: float
    attachment_style: float # 0=Avoidant, 0.5=Anxious, 1.0=Secure
    
    # Metric Category 2: Practical
    financial_mindset: float # 0=Saver, 1=Spender
    sleep_chronotype: float  # 0=Lark, 1=Owl

class AlignmentEngine:
    """
    Implementation of the 100-Metric Relationship Compatibility Framework.
    Predicts stability based on Gottman's 'Four Horsemen' and Value Congruence.
    """
    def __init__(self):
        self.divorce_threshold = 0.85 # >90% accuracy per research
        
    def assess_compatibility(self, p1: OperatorProfile, p2: OperatorProfile) -> Dict:
        # 1. Calculate Core Congruence (Euclidean Distance)
        # Lower distance = Higher compatibility
        vec1 = np.array([p1.cultural_homogamy, p1.value_congruence, p1.financial_mindset])
        vec2 = np.array([p2.cultural_homogamy, p2.value_congruence, p2.financial_mindset])
        
        # Weighted distance (Values matter more than Sleep)
        weights = np.array([0.5, 0.3, 0.2])
        raw_distance = np.linalg.norm((vec1 - vec2) * weights)
        compatibility_score = 1.0 - np.tanh(raw_distance)
        
        return {
            "raw_compatibility": compatibility_score,
            "risk_flag": compatibility_score < 0.6
        }

    def detect_cascade_failure(self, interaction_log: List[str]) -> bool:
        """
        Scans for 'The Four Horsemen': Criticism, Contempt, Defensiveness, Stonewalling.
        """
        triggers = ["you always", "worthless", "whatever", "not my fault"]
        risk_counter = 0
        
        for phrase in interaction_log:
            if any(trigger in phrase.lower() for trigger in triggers):
                risk_counter += 1
                
        # Gottman Ratio: 5:1 Positive to Negative. 
        # If negative density is high, predict failure.
        return risk_counter >= 3
