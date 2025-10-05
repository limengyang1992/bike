# Project Structure Guide

## 📁 Directory Organization

### Root Level
```
bike/
├── README.md                           # Main project documentation
├── requirements.txt                    # Python dependencies
├── mobike_shanghai_with_house_price.csv # Main dataset (2,000 records)
├── Feature_Engineering_Description.md  # Feature engineering details
├── Figure_Descriptions.md              # Figure explanations
└── PROJECT_STRUCTURE.md               # This file
```

### Code Directory (`code/`)
```
code/
├── academic_visualization_english.py   # Generates Chapter 2 & 3 figures
├── chapter4_visualization_english.py   # Generates Chapter 4 figures
└── run_all_english_figures.py         # Main execution script
```

**Key Scripts:**
- `run_all_english_figures.py`: **Main entry point** - generates all paper figures
- `academic_visualization_english.py`: Creates 4 figures for data and ML chapters
- `chapter4_visualization_english.py`: Creates 4 figures for analysis chapter

### Images Directory (`images/`)
```
images/
├── Figure_2_1_Data_Distribution.png    # Spatial data distribution
├── Figure_2_2_Grid_Activity.png        # Grid-based activity analysis
├── Figure_2_3_House_Price_Distribution.png # Economic distribution
├── Figure_2_4_Dataset_Structure.png    # Data architecture
├── Figure_3_1_Model_Performance.png    # ML model comparison
├── Figure_3_2_Feature_Importance.png   # Feature importance analysis
├── Figure_3_3_Prediction_Results.png   # Prediction accuracy
├── Figure_4_1_Club_Effect.png          # Spatial resource clustering
├── Figure_4_2_Two_Patterns.png         # Usage pattern differentiation
├── Figure_4_3_Tidal_Commute.png        # Urban flow patterns
└── Figure_4_4_Economic_Patterns.png    # Economic-usage relationships
```

**Figure Categories:**
- **Chapter 2** (Data): Figures 2.1-2.4 (4 figures)
- **Chapter 3** (ML): Figures 3.1-3.3 (3 figures)  
- **Chapter 4** (Analysis): Figures 4.1-4.4 (4 figures)
- **Total**: 11 publication-ready figures

### LaTeX Directory (`latex/`)
```
latex/
├── figure_2_4_advanced.tex             # Professional dataset structure
├── figure_2_4_simple.tex               # Standard LaTeX version
├── figure_2_4_minimal.tex              # Minimal dependencies
└── figure_2_4_dataset_structure.tex    # Full-featured version
```

**LaTeX Versions:**
- **Advanced**: Best for publications (shadows, modern styling)
- **Simple**: Standard LaTeX compatibility
- **Minimal**: Online compilation friendly
- **Full**: Custom fonts and advanced features

## 🚀 Usage Instructions

### Quick Start
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate all figures
python code/run_all_english_figures.py

# 3. View results in images/ folder
```

### Individual Figure Generation
```bash
# Generate specific chapters
python code/academic_visualization_english.py  # Chapters 2 & 3
python code/chapter4_visualization_english.py  # Chapter 4
```

### LaTeX Compilation
```bash
# For Overleaf or online LaTeX editors
# Copy content from latex/figure_2_4_advanced.tex
# Compile with pdfLaTeX
```

## 📊 Data Flow

```
Raw Data (CSV) 
    ↓
Feature Engineering (38 features)
    ↓
Machine Learning (Random Forest)
    ↓
Visualization (11 figures)
    ↓
LaTeX Integration (Professional figures)
```

## 🎯 Key Files to Know

### Essential Files
1. **`mobike_shanghai_with_house_price.csv`** - Main dataset
2. **`code/run_all_english_figures.py`** - Main execution script
3. **`README.md`** - Complete project documentation
4. **`requirements.txt`** - Python dependencies

### Documentation Files
1. **`Feature_Engineering_Description.md`** - Technical details
2. **`Figure_Descriptions.md`** - Figure explanations
3. **`PROJECT_STRUCTURE.md`** - This file

### Output Files
1. **`images/`** - All generated figures (11 files)
2. **`latex/`** - LaTeX source files (4 versions)

## 🔧 Technical Details

### Dependencies
- **Python**: 3.7+
- **Core Libraries**: pandas, numpy, scikit-learn
- **Visualization**: matplotlib, seaborn
- **LaTeX**: tikz, xcolor (for LaTeX figures)

### Performance
- **Dataset Size**: 2,000 records, 38 features
- **Processing Time**: ~30 seconds for all figures
- **Output Quality**: 300 DPI, publication-ready
- **File Sizes**: 1-3 MB per figure

### Compatibility
- **Operating Systems**: Windows, macOS, Linux
- **Python Versions**: 3.7, 3.8, 3.9, 3.10, 3.11
- **LaTeX**: pdfLaTeX, XeLaTeX compatible

## 📝 Notes

- All figures use **English labels only**
- **Dopamine color scheme** (Orange, Blue, Green)
- **26pt minimum font size** for readability
- **No titles** in figures (added in paper text)
- **Vector graphics** available in LaTeX format
