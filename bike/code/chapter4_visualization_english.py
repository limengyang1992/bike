#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 4: Analysis and Insights Visualization Generator (English Version)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')

# Set academic style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'font.size': 26,
    'font.family': 'serif',
    'axes.labelsize': 28,
    'axes.titlesize': 30,
    'xtick.labelsize': 26,
    'ytick.labelsize': 26,
    'legend.fontsize': 26,
    'figure.titlesize': 32,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3
})

# Dopamine color scheme
DOPAMINE_COLORS = {
    'primary': '#FF6B6B',      # Coral Red
    'secondary': '#4ECDC4',    # Teal
    'accent': '#45B7D1',       # Sky Blue
    'warning': '#FFA07A',      # Light Salmon
    'success': '#98D8C8',      # Mint Green
    'info': '#F7DC6F',         # Golden Yellow
    'purple': '#BB8FCE',       # Light Purple
    'orange': '#F8C471',       # Orange
    'pink': '#F1948A',         # Pink
    'teal': '#85C1E9'          # Light Blue
}

class Chapter4VisualizerEnglish:
    """Chapter 4 Visualization Generator (English)"""
    
    def __init__(self, data_path):
        self.data_path = data_path
        self.df = None
        
    def load_and_prepare_data(self):
        """Load and prepare data"""
        print("Loading data...")
        self.df = pd.read_csv(self.data_path)
        
        # Basic feature engineering
        self.df['start_time'] = pd.to_datetime(self.df['start_time'])
        self.df['end_time'] = pd.to_datetime(self.df['end_time'])
        self.df['duration_minutes'] = (self.df['end_time'] - self.df['start_time']).dt.total_seconds() / 60
        self.df['hour'] = self.df['start_time'].dt.hour
        self.df['day_of_week'] = self.df['start_time'].dt.dayofweek
        self.df['is_weekend'] = self.df['day_of_week'].isin([5, 6]).astype(int)
        
        # Spatial features
        self.df['distance_km'] = np.sqrt(
            (self.df['end_location_x'] - self.df['start_location_x'])**2 + 
            (self.df['end_location_y'] - self.df['start_location_y'])**2
        ) * 111
        
        # Create grid
        self.df['grid_x'] = np.round(self.df['start_location_x'], 2)
        self.df['grid_y'] = np.round(self.df['start_location_y'], 2)
        
        # Define economic level groups
        self.df['economic_level'] = pd.cut(self.df['house_price'], 
                                          bins=3, labels=['Low Economic Level', 'Medium Economic Level', 'High Economic Level'])
        
        print(f"Data loaded successfully, {len(self.df)} records")
        
    def create_figure_4_1(self):
        """Figure 4.1: "Club Effect" - Spatial Aggregation of Resources"""
        print("Creating Figure 4.1: Club Effect - Spatial Aggregation of Resources...")
        
        # Calculate grid activity
        grid_activity = self.df.groupby(['grid_x', 'grid_y']).agg({
            'orderid': 'count',
            'house_price': 'mean'
        }).reset_index()
        grid_activity.columns = ['grid_x', 'grid_y', 'activity_count', 'avg_price']
        
        # Define high activity and high price areas
        high_activity_threshold = grid_activity['activity_count'].quantile(0.7)
        high_price_threshold = grid_activity['avg_price'].quantile(0.7)
        
        grid_activity['is_high_activity'] = grid_activity['activity_count'] > high_activity_threshold
        grid_activity['is_high_price'] = grid_activity['avg_price'] > high_price_threshold
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # Overlay: High activity and high price
        overlap = grid_activity[grid_activity['is_high_activity'] & grid_activity['is_high_price']]
        ax.scatter(grid_activity['grid_x'], grid_activity['grid_y'], 
                  c='lightgray', alpha=0.3, s=20, label='Normal Areas')
        ax.scatter(overlap['grid_x'], overlap['grid_y'], 
                  c=DOPAMINE_COLORS['warning'], alpha=0.8, s=60, label='High Activity + High Price')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.legend()
        
        plt.tight_layout()
        plt.savefig('Figure_4_1_Club_Effect.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_figure_4_2(self):
        """Figure 4.2: "Two Patterns" - Functional Differentiation of Travel"""
        print("Creating Figure 4.2: Two Patterns - Functional Differentiation of Travel...")
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # Weekday vs Weekend overall comparison
        weekday_data = self.df[self.df['is_weekend'] == 0]
        weekend_data = self.df[self.df['is_weekend'] == 1]
        
        weekday_hourly = weekday_data.groupby('hour').size()
        weekend_hourly = weekend_data.groupby('hour').size()
        
        ax.plot(weekday_hourly.index, weekday_hourly.values, 
               marker='o', linewidth=2, label='Weekday', color=DOPAMINE_COLORS['primary'])
        ax.plot(weekend_hourly.index, weekend_hourly.values, 
               marker='s', linewidth=2, label='Weekend', color=DOPAMINE_COLORS['secondary'])
        ax.set_xlabel('Hour')
        ax.set_ylabel('Usage Count')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('Figure_4_2_Two_Patterns.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_figure_4_3(self):
        """Figure 4.3: "Tidal Commute" - Internal Urban Flow Direction"""
        print("Creating Figure 4.3: Tidal Commute - Internal Urban Flow Direction...")
        
        # Define low price and high price areas
        low_price_threshold = self.df['house_price'].quantile(0.3)
        high_price_threshold = self.df['house_price'].quantile(0.7)
        
        low_price_data = self.df[self.df['house_price'] <= low_price_threshold]
        high_price_data = self.df[self.df['house_price'] >= high_price_threshold]
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # Commute flow analysis
        weekday_morning = self.df[(self.df['is_weekend'] == 0) & (self.df['hour'].between(7, 9))]
        weekday_evening = self.df[(self.df['is_weekend'] == 0) & (self.df['hour'].between(17, 19))]
        
        ax.scatter(weekday_morning['start_location_x'], weekday_morning['start_location_y'], 
                  alpha=0.6, s=20, color=DOPAMINE_COLORS['accent'], label='Morning Peak (7-9h)')
        ax.scatter(weekday_evening['start_location_x'], weekday_evening['start_location_y'], 
                  alpha=0.6, s=20, color=DOPAMINE_COLORS['info'], label='Evening Peak (17-19h)')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        ax.legend()
        
        plt.tight_layout()
        plt.savefig('Figure_4_3_Tidal_Commute.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_figure_4_4(self):
        """Figure 4.4: Economic Level and Usage Pattern Relationship"""
        print("Creating Figure 4.4: Economic Level and Usage Pattern Relationship...")
        
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        
        # Economic level and usage frequency relationship
        economic_usage = self.df.groupby('economic_level').agg({
            'orderid': 'count',
            'house_price': 'mean',
            'distance_km': 'mean',
            'duration_minutes': 'mean'
        }).reset_index()
        
        bars = ax.bar(economic_usage['economic_level'], economic_usage['orderid'], 
                     color=[DOPAMINE_COLORS['primary'], DOPAMINE_COLORS['secondary'], DOPAMINE_COLORS['accent']],
                     alpha=0.8)
        ax.set_xlabel('Economic Level')
        ax.set_ylabel('Usage Count')
        
        # Set x-axis tick labels font size to prevent overlap
        ax.tick_params(axis='x', labelsize=18)
        
        # Add value labels
        for i, v in enumerate(economic_usage['orderid']):
            ax.text(i, v + 10, f'{v}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig('Figure_4_4_Economic_Patterns.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_all_chapter4_figures(self):
        """Create all Chapter 4 figures"""
        print("Starting to create all Chapter 4 figures...")
        
        # Load data
        self.load_and_prepare_data()
        
        # Create figures
        self.create_figure_4_1()
        self.create_figure_4_2()
        self.create_figure_4_3()
        self.create_figure_4_4()
        
        print("All Chapter 4 figures created successfully!")

def main():
    """Main function"""
    visualizer = Chapter4VisualizerEnglish('mobike_shanghai_with_house_price.csv')
    visualizer.create_all_chapter4_figures()

if __name__ == "__main__":
    main()
