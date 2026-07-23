import matplotlib.pyplot as plt
import pandas as pd

class FitnessAnalytics:
    @staticmethod
    def plot_calorie_progress(df_logs, target_daily_calories=500):
        """Generates a Matplotlib visual analytics chart for calorie burning progress."""
        if df_logs.empty:
            print("[INFO] No data available for visual analytics.")
            return

        df_logs['date_only'] = pd.to_datetime(df_logs['date']).dt.date
        daily_summary = df_logs.groupby('date_only')['calories_burned'].sum().reset_index()

        plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
        fig, ax = plt.subplots(figsize=(8, 4))

        ax.bar(daily_summary['date_only'].astype(str), daily_summary['calories_burned'], color='#2b6cb0', label='Calories Burned')
        ax.axhline(y=target_daily_calories, color='#e53e3e', linestyle='--', label=f'Target ({target_daily_calories} kcal)')

        ax.set_title("Daily Calorie Burn Progress Dashboard", fontsize=12, fontweight='bold', pad=10)
        ax.set_xlabel("Date", fontsize=10)
        ax.set_ylabel("Calories (kcal)", fontsize=10)
        ax.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        plt.savefig("assets/dashboard_preview.png", dpi=300)
        plt.show()
