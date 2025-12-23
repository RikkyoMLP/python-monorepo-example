import numpy as np
from hsi_utils.core.plotting_utils import PlotInput, draw_plot

def main():
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    plot1 = PlotInput(
        data=y1,
        identifier="Sin(x)",
        line_color="red",
        show_max=True
    )
    
    plot2 = PlotInput(
        data=y2,
        identifier="Cos(x)",
        line_color="blue",
        show_min=True
    )

    output_filename = "monorepo_example.png"
    draw_plot(
        left_axis_plots=[plot1],
        left_axis_label="Sine Amplitude",
        right_axis_plots=[plot2],
        right_axis_label="Cosine Amplitude",
        x_axis_label="Step",
        title="Monorepo Example: Shared Plotting Utility",
        output_path=output_filename
    )

if __name__ == "__main__":
    main()

