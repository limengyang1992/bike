#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Run All Academic Figures Generator (English Version)
Generate individual academic charts with English labels
"""

from academic_visualization_english import AcademicVisualizerEnglish
from chapter4_visualization_english import Chapter4VisualizerEnglish

def main():
    """Main function"""
    print("=" * 80)
    print("Academic Paper Figures Generator (English Version)")
    print("Decoding Shanghai's Socio-economic Divide through Shared Bike Data")
    print("=" * 80)
    
    try:
        # Chapter 2-3 figures
        print("\n" + "=" * 60)
        print("Chapter 2-3: Data Universe Construction & Machine Learning")
        print("=" * 60)
        
        visualizer_23 = AcademicVisualizerEnglish('mobike_shanghai_with_house_price.csv')
        visualizer_23.create_all_figures()
        
        # Chapter 4 figures
        print("\n" + "=" * 60)
        print("Chapter 4: Analysis and Insights")
        print("=" * 60)
        
        visualizer_4 = Chapter4VisualizerEnglish('mobike_shanghai_with_house_price.csv')
        visualizer_4.create_all_chapter4_figures()
        
        print("\n" + "=" * 80)
        print("All Academic Figures Generated Successfully!")
        print("=" * 80)
        
        print("\nGenerated Figure Files:")
        print("Chapter 2 - Data Universe Construction:")
        print("  - Figure_2_1_Data_Distribution.png")
        print("  - Figure_2_2_Grid_Activity.png")
        print("  - Figure_2_3_House_Price_Distribution.png")
        print("  - Figure_2_4_Dataset_Structure.png")
        
        print("\nChapter 3 - Machine Learning:")
        print("  - Figure_3_1_Model_Performance.png")
        print("  - Figure_3_2_Feature_Importance.png")
        print("  - Figure_3_3_Prediction_Results.png")
        
        print("\nChapter 4 - Analysis and Insights:")
        print("  - Figure_4_1_Club_Effect.png")
        print("  - Figure_4_2_Two_Patterns.png")
        print("  - Figure_4_3_Tidal_Commute.png")
        print("  - Figure_4_4_Economic_Patterns.png")
        
        print("\nFigure Characteristics:")
        print("✅ Academic style design")
        print("✅ Dopamine color scheme")
        print("✅ High resolution output (300 DPI)")
        print("✅ Individual figure files")
        print("✅ English labels only")
        print("✅ Random Forest as primary model")
        print("✅ Highlighting core findings")
        
    except Exception as e:
        print(f"Error occurred during figure generation: {e}")
        print("Please check if the data file exists and required Python packages are installed")

if __name__ == "__main__":
    main()
