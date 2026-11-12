"""
MUET Cyber Learning Portal - Data Science and Analytics Lab IV
Topic: Matplotlib Foundations: Figures, Axes and Basic Plots

SHORT THEORY NOTES:
1. Figure vs. Axes:
   - Figure (fig): The whole top-level canvas/window holding everything.
   - Axes (ax): The individual plot/graph box containing coordinate systems, data points, labels, and ticks.
   - Using 'fig, ax = plt.subplots()' provides an explicit handle for every panel, making multi-plot grids simple and reliable.
2. The Four Basic Plot Types:
   - Line (ax.plot): Best for continuous changes or trends across ordered dimensions like time.
   - Bar (ax.bar): Compares discrete values across categorical groups.
   - Scatter (ax.scatter): Reveals associations and correlations between two numeric variables.
   - Histogram (ax.hist): Illustrates the frequency distribution of a single numeric feature.
3. Exporting Figures (fig.savefig):
   - dpi: Dots per inch; controls export resolution (e.g., 300 for reports, 72 for web/preview).
   - bbox_inches='tight': Fits the outer boundary strictly around all labels, preventing them from being cut off.
4. Headless Execution:
   - 'matplotlib.use("Agg")' lets scripts build and save figures in memory without needing a GUI display.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

print("=" * 65)
print("LAB IV: MATPLOTLIB FOUNDATIONS - FIGURES, AXES & BASIC PLOTS")
print("=" * 65)

# ==========================================
# Task 1: Create a Basic Line Plot
# Theory: ax.plot() captures trends over an ordered axis.
# ==========================================
x1 = [1, 2, 3, 4]
y1 = [10, 20, 15, 25]

fig1, ax1 = plt.subplots()
ax1.plot(x1, y1, marker='o')
ax1.set_title('Trend of Y over X')
ax1.set_xlabel('X values')
ax1.set_ylabel('Y values')

fig1.savefig('task1_line.png', dpi=150, bbox_inches='tight')
plt.close(fig1)

print("\n--- TASK 1 OUTPUT ---")
print(f"Plot successfully rendered and saved using axes object: {type(ax1).__name__}")


# ==========================================
# Task 2: Compare Categories with Bar Charts
# Theory: ax.bar() compares distinct categorical quantities.
# ==========================================
categories = ['A', 'B']
values = [50, 80]

fig2, ax2 = plt.subplots()
ax2.bar(categories, values)
ax2.set_title('Category Comparison')
ax2.set_xlabel('Category')
ax2.set_ylabel('Value')

fig2.savefig('task2_bar.png', dpi=150, bbox_inches='tight')
plt.close(fig2)

print("\n--- TASK 2 OUTPUT ---")
print("Bar plot successfully generated and saved for categories ['A', 'B'] with values [50, 80].")


# ==========================================
# Task 3: Analyze Distribution with Histograms
# Theory: ax.hist() bins continuous data to display frequency.
# ==========================================
data_vals = [1, 2, 2, 3, 3, 3, 4, 4, 5]

fig3, ax3 = plt.subplots()
counts, bin_edges, _ = ax3.hist(data_vals, bins=3, edgecolor='black')
ax3.set_title('Distribution of Data (3 Bins)')
ax3.set_xlabel('Value Range')
ax3.set_ylabel('Frequency')

fig3.savefig('task3_hist.png', dpi=150, bbox_inches='tight')
plt.close(fig3)

print("\n--- TASK 3 OUTPUT ---")
print(f"Bin counts: {counts.astype(int).tolist()}")
print(f"Bin edges: {np.round(bin_edges, 2).tolist()}")


# ==========================================
# Task 4: Exporting High-Resolution Figures
# Theory: dpi=300 sets print quality; bbox_inches='tight' stops clipping.
# ==========================================
fig4, ax4 = plt.subplots()
ax4.plot([1, 2, 3], [4, 5, 6])
ax4.set_title('Sample High-Res Plot')

# Submission line for Task 4
fig4.savefig('report_chart.png', dpi=300, bbox_inches='tight')
plt.close(fig4)

print("\n--- TASK 4 OUTPUT ---")
print("Saved report_chart.png at 300 DPI with tight bounding box.")

print("\n" + "=" * 65)
print("ALL TASKS EXECUTED SUCCESSFULLY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab IV
Topic: Customising Plots for Clarity

SHORT THEORY NOTES:
1. Self-Explanatory Plots:
   - A stand-alone chart must convey its key takeaway directly in the title.
   - Axes require precise units (e.g., 'Time (s)', 'Temperature (°C)') to prevent ambiguity.
   - Any multi-series visualization requires a legend mapping styles to data batches.
2. Accessible Encoding (Data-Ink & Accessibility):
   - Never rely on color alone; roughly 1 in 12 men have color-vision deficiencies.
   - Redundantly encode data by varying line style (solid vs dashed) and markers (circle vs square).
   - This ensures full legibility in monochrome, greyscale, or black-and-white printouts.
3. Axis Honesty (Zero Baseline):
   - Bar charts encode values by total column length/area from a baseline.
   - Starting a bar chart's y-axis above zero (truncated axis) exaggerates small differences.
   - Use 'ax.set_ylim(bottom=0)' to maintain true mathematical proportions.
4. In-Chart Annotations:
   - Annotating key points directly (peaks, valleys, anomalies) with arrows guides the reader's eye
     faster than an external caption or footnote.
================================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 65)
print("RUNNING LAB IV: CUSTOMISING PLOTS FOR CLARITY")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Creating a Self-Explanatory Plot
# Theory: Self-contained charts state takeaways in the title and include units.
# -------------------------------------------------------------
print("\n[Executing Task 1...]")
time_sec = [0, 5, 10, 15, 20, 25]
temp_c = [22.0, 31.5, 45.0, 62.3, 78.1, 91.4]

fig1, ax1 = plt.subplots()
ax1.plot(time_sec, temp_c, marker='o', color='tab:blue')

t1_title = 'Core temperature rises steadily under continuous load'
t1_xlabel = 'Time (s)'
t1_ylabel = 'Temperature (°C)'

ax1.set_title(t1_title)
ax1.set_xlabel(t1_xlabel)
ax1.set_ylabel(t1_ylabel)

fig1.savefig('task1_plot.png', dpi=120, bbox_inches='tight')
plt.close(fig1)

print("--- TASK 1 OUTPUT ---")
print(f"Title: {t1_title}")
print(f"X-Axis Label: {t1_xlabel}")
print(f"Y-Axis Label: {t1_ylabel}")


# -------------------------------------------------------------
# TASK 2: Accessible Multi-Series Encoding
# Theory: Redundant encoding (color + line style + marker) supports greyscale and color blindness.
# -------------------------------------------------------------
print("\n[Executing Task 2...]")
epochs = [1, 2, 3, 4, 5, 6]
model_a_acc = [65.2, 74.0, 81.5, 87.1, 91.0, 93.4]
model_b_acc = [58.0, 64.5, 71.0, 76.2, 80.5, 83.0]

fig2, ax2 = plt.subplots()
line1, = ax2.plot(epochs, model_a_acc, color='tab:blue', linestyle='-', marker='o', label='Model A (CNN)')
line2, = ax2.plot(epochs, model_b_acc, color='tab:orange', linestyle='--', marker='s', label='Model B (MLP)')

ax2.set_title('Model A consistently outperforms Model B across all epochs')
ax2.set_xlabel('Epoch number')
ax2.set_ylabel('Validation accuracy (%)')
ax2.legend()

fig2.savefig('task2_plot.png', dpi=120, bbox_inches='tight')
plt.close(fig2)

print("\n--- TASK 2 OUTPUT ---")
print(f"Legend Labels: {[line1.get_label(), line2.get_label()]}")


# -------------------------------------------------------------
# TASK 3: Ensuring Bar Chart Honesty
# Theory: ax.set_ylim(bottom=0) stops truncated baselines from artificially exaggerating differences.
# -------------------------------------------------------------
print("\n[Executing Task 3...]")
servers = ['Node 01', 'Node 02', 'Node 03']
uptime_pct = [99.2, 99.8, 99.5]

fig3, ax3 = plt.subplots()
ax3.bar(servers, uptime_pct, color='tab:gray')

# Mandatory honest baseline
ax3.set_ylim(bottom=0)

ax3.set_title('Server uptime comparison across cluster nodes')
ax3.set_xlabel('Server identifier')
ax3.set_ylabel('Uptime percentage (%)')

fig3.savefig('task3_plot.png', dpi=120, bbox_inches='tight')
ymin, _ = ax3.get_ylim()
plt.close(fig3)

print("\n--- TASK 3 OUTPUT ---")
print(f"Observed y-axis minimum value: {ymin}")


# -------------------------------------------------------------
# TASK 4: Highlighting Points of Interest
# Theory: ax.annotate() points directly at anomalies so readers don't have to search for them.
# -------------------------------------------------------------
print("\n[Executing Task 4...]")
hours = list(range(0, 24))
traffic_gbps = [12, 10, 8, 7, 9, 14, 25, 42, 65, 78, 82, 85, 80, 83, 88, 94, 91, 148, 110, 95, 70, 50, 32, 18]

fig4, ax4 = plt.subplots()
ax4.plot(hours, traffic_gbps, color='tab:blue', marker='.')

peak_traffic = max(traffic_gbps)
peak_hour = hours[traffic_gbps.index(peak_traffic)]
annotation_text = 'DDoS attack traffic spike'

ax4.annotate(
    annotation_text,
    xy=(peak_hour, peak_traffic),
    xytext=(peak_hour - 7, peak_traffic - 15),
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2)
)

ax4.set_title('Network traffic volume reveals sudden late-afternoon surge')
ax4.set_xlabel('Time of day (hours)')
ax4.set_ylabel('Bandwidth utilization (Gbps)')

fig4.savefig('task4_plot.png', dpi=120, bbox_inches='tight')
plt.close(fig4)

print("\n--- TASK 4 OUTPUT ---")
print(f"Annotation Label: {annotation_text}")
print(f"Annotated Point Coordinates: ({peak_hour}, {peak_traffic})")

print("\n" + "=" * 65)
print("ALL TASKS EXECUTED AND SAVED TO CURRENT WORKING DIRECTORY.")
print("=" * 65)

"""
================================================================================
MUET Cyber Learning Portal - Data Science and Analytics Lab IV
Topic: Customising Plots for Clarity

SHORT THEORY NOTES:
1. Self-Explanatory Plots:
   - A stand-alone chart must convey its key takeaway directly in the title.
   - Axes require precise units (e.g., 'Time (s)', 'Temperature (°C)') to prevent ambiguity.
   - Any multi-series visualization requires a legend mapping styles to data batches.
2. Accessible Encoding (Data-Ink & Accessibility):
   - Never rely on color alone; roughly 1 in 12 men have color-vision deficiencies.
   - Redundantly encode data by varying line style (solid vs dashed) and markers (circle vs square).
   - This ensures full legibility in monochrome, greyscale, or black-and-white printouts.
3. Axis Honesty (Zero Baseline):
   - Bar charts encode values by total column length/area from a baseline.
   - Starting a bar chart's y-axis above zero (truncated axis) exaggerates small differences.
   - Use 'ax.set_ylim(bottom=0)' to maintain true mathematical proportions.
4. In-Chart Annotations:
   - Annotating key points directly (peaks, valleys, anomalies) with arrows guides the reader's eye
     faster than an external caption or footnote.
================================================================================
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 65)
print("RUNNING LAB IV: CUSTOMISING PLOTS FOR CLARITY")
print("=" * 65)


# -------------------------------------------------------------
# TASK 1: Creating a Self-Explanatory Plot
# Theory: Self-contained charts state takeaways in the title and include units.
# -------------------------------------------------------------
print("\n[Executing Task 1...]")
time_sec = [0, 5, 10, 15, 20, 25]
temp_c = [22.0, 31.5, 45.0, 62.3, 78.1, 91.4]

fig1, ax1 = plt.subplots()
ax1.plot(time_sec, temp_c, marker='o', color='tab:blue')

t1_title = 'Core temperature rises steadily under continuous load'
t1_xlabel = 'Time (s)'
t1_ylabel = 'Temperature (°C)'

ax1.set_title(t1_title)
ax1.set_xlabel(t1_xlabel)
ax1.set_ylabel(t1_ylabel)

fig1.savefig('task1_plot.png', dpi=120, bbox_inches='tight')
plt.close(fig1)

print("--- TASK 1 OUTPUT ---")
print(f"Title: {t1_title}")
print(f"X-Axis Label: {t1_xlabel}")
print(f"Y-Axis Label: {t1_ylabel}")


# -------------------------------------------------------------
# TASK 2: Accessible Multi-Series Encoding
# Theory: Redundant encoding (color + line style + marker) supports greyscale and color blindness.
# -------------------------------------------------------------
print("\n[Executing Task 2...]")
epochs = [1, 2, 3, 4, 5, 6]
model_a_acc = [65.2, 74.0, 81.5, 87.1, 91.0, 93.4]
model_b_acc = [58.0, 64.5, 71.0, 76.2, 80.5, 83.0]

fig2, ax2 = plt.subplots()
line1, = ax2.plot(epochs, model_a_acc, color='tab:blue', linestyle='-', marker='o', label='Model A (CNN)')
line2, = ax2.plot(epochs, model_b_acc, color='tab:orange', linestyle='--', marker='s', label='Model B (MLP)')

ax2.set_title('Model A consistently outperforms Model B across all epochs')
ax2.set_xlabel('Epoch number')
ax2.set_ylabel('Validation accuracy (%)')
ax2.legend()

fig2.savefig('task2_plot.png', dpi=120, bbox_inches='tight')
plt.close(fig2)

print("\n--- TASK 2 OUTPUT ---")
print(f"Legend Labels: {[line1.get_label(), line2.get_label()]}")


# -------------------------------------------------------------
# TASK 3: Ensuring Bar Chart Honesty
# Theory: ax.set_ylim(bottom=0) stops truncated baselines from artificially exaggerating differences.
# -------------------------------------------------------------
print("\n[Executing Task 3...]")
servers = ['Node 01', 'Node 02', 'Node 03']
uptime_pct = [99.2, 99.8, 99.5]

fig3, ax3 = plt.subplots()
ax3.bar(servers, uptime_pct, color='tab:gray')

# Mandatory honest baseline
ax3.set_ylim(bottom=0)

ax3.set_title('Server uptime comparison across cluster nodes')
ax3.set_xlabel('Server identifier')
ax3.set_ylabel('Uptime percentage (%)')

fig3.savefig('task3_plot.png', dpi=120, bbox_inches='tight')
ymin, _ = ax3.get_ylim()
plt.close(fig3)

print("\n--- TASK 3 OUTPUT ---")
print(f"Observed y-axis minimum value: {ymin}")


# -------------------------------------------------------------
# TASK 4: Highlighting Points of Interest
# Theory: ax.annotate() points directly at anomalies so readers don't have to search for them.
# -------------------------------------------------------------
print("\n[Executing Task 4...]")
hours = list(range(0, 24))
traffic_gbps = [12, 10, 8, 7, 9, 14, 25, 42, 65, 78, 82, 85, 80, 83, 88, 94, 91, 148, 110, 95, 70, 50, 32, 18]

fig4, ax4 = plt.subplots()
ax4.plot(hours, traffic_gbps, color='tab:blue', marker='.')

peak_traffic = max(traffic_gbps)
peak_hour = hours[traffic_gbps.index(peak_traffic)]
annotation_text = 'DDoS attack traffic spike'

ax4.annotate(
    annotation_text,
    xy=(peak_hour, peak_traffic),
    xytext=(peak_hour - 7, peak_traffic - 15),
    arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2)
)

ax4.set_title('Network traffic volume reveals sudden late-afternoon surge')
ax4.set_xlabel('Time of day (hours)')
ax4.set_ylabel('Bandwidth utilization (Gbps)')

fig4.savefig('task4_plot.png', dpi=120, bbox_inches='tight')
plt.close(fig4)

print("\n--- TASK 4 OUTPUT ---")
print(f"Annotation Label: {annotation_text}")
print(f"Annotated Point Coordinates: ({peak_hour}, {peak_traffic})")

print("\n" + "=" * 65)
print("ALL TASKS EXECUTED AND SAVED TO CURRENT WORKING DIRECTORY.")
print("=" * 65)