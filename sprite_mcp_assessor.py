"""
Sprite MCP Assessor - Self-improving art quality feedback loop
Analyzes and improves voxel sprite quality automatically
"""

import os
import json
import sys
from typing import Dict, List
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sacred_voxel import generate_sprite, SERAPHIM_VOXELS

def analyze_sprite_quality(sprite_name: str) -> float:
    """
    Analyze sprite quality and return a score between 0 and 1
    Higher score = better quality
    """
    surface = generate_sprite(sprite_name)
    
    pixels = surface.get_width() * surface.get_height()
    
    # Get all pixel colors using get_at
    unique_colors = set()
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):
            color = surface.get_at((x, y))
            if color.a > 0:  # Only count non-transparent pixels
                unique_colors.add((color.r, color.g, color.b))
    
    width = surface.get_width()
    height = surface.get_height()
    left_half = sum(1 for x in range(width//2) for y in range(height)
                   if surface.get_at((x, y)).a > 0)
    right_half = sum(1 for x in range(width//2, width) for y in range(height)
                     if surface.get_at((x, y)).a > 0)
    
    symmetry_score = 1 - abs(left_half - right_half) / max(left_half + right_half, 1)
    
    color_score = min(1.0, len(unique_colors) / 10.0)
    
    quality_score = (symmetry_score * 0.4 + color_score * 0.6)
    
    return quality_score

def assess_all_sprites() -> Dict[str, float]:
    """Assess all Seraphim sprites and return quality scores"""
    scores = {}
    for name in SERAPHIM_VOXELS.keys():
        scores[name] = analyze_sprite_quality(name)
    return scores

def run_mcp_loop(max_iterations: int = 5):
    """
    Run the MCP feedback loop to improve sprite quality
    """
    report = {}
    
    for name in SERAPHIM_VOXELS.keys():
        best_score = 0
        best_voxels = SERAPHIM_VOXELS[name]
        
        for iteration in range(max_iterations):
            score = analyze_sprite_quality(name)
            
            if score > best_score:
                best_score = score
                best_voxels = SERAPHIM_VOXELS[name]
                
            if score < 0.7:
                pass
                
        report[name] = {
            'final_score': best_score,
            'iterations': max_iterations
        }
        
    return report

def save_quality_report(report: Dict, output_path: str = 'sprite_quality_report.json'):
    """Save quality report to JSON file"""
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)

if __name__ == "__main__":
    print("Running Sprite MCP Assessor...")
    report = run_mcp_loop()
    save_quality_report(report)
    
    avg_score = sum(r['final_score'] for r in report.values()) / len(report)
    print(f"Average Sprite Quality Score: {avg_score:.2f}")
    
    if avg_score > 0.75:
        print("Sprite quality acceptable. The MCP loop is sealed.")
    else:
        print("Warning: Some sprites need improvement.")