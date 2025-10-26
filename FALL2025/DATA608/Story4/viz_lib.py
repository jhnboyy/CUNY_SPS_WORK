import pandas as pd
import geopandas as gpd
import matplotlib.patches as mpatches
from shapely import affinity   
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from typing import Optional, Tuple

def make_span_chart(
    df: pd.DataFrame,
    category: str,                 # categorical column for y-axis labels
    x_min: str,                    # column with min values
    x_max: str,                    # column with max values
    title: str = "Title",
    subtitle: Optional[str] = None,
    color: str = "#43AA8B",
    annotate: bool = True,
    xfmt: str = '${x:,.0f}',
    x_labels_show: bool = True,     # show/hide x-axis label text
    y_labels_show: bool = True,     # show/hide y-axis label text
    x_axis_show: bool = True,       # show/hide entire x-axis
    y_axis_show: bool = True,       # show/hide entire y-axis
    x_ticks_show: bool = True,      # show/hide tick marks (x)
    y_ticks_show: bool = True,      # show/hide tick marks (y)
    x_lab: str = '',
    y_lab: str = '',
    grid: bool = True,
    figsize: Tuple[float, float] = (9, 5),
    sort_by=None,
    annotated_labels_placement_pad: float = 0.15,

    # ---- New, configurable title/subtitle controls ----
    use_suptitle: bool = True,          # use fig.suptitle for the main title
    subtitle_on_axes: bool = True,      # True: ax.set_title; False: fig.text
    title_x: Optional[float] = None,    # override horizontal position (None => default centering)
    title_y: Optional[float] = None,    # override vertical position for title
    subtitle_x: Optional[float] = None, # used only if subtitle_on_axes=False
    subtitle_y: Optional[float] = None, # used only if subtitle_on_axes=False
    top_adjust: Optional[float] = None, # fig.subplots_adjust(top=?)
    tight_rect: Optional[Tuple[float, float, float, float]] = None  # plt.tight_layout(rect=?)
) -> plt.Axes:
    """Draw a clean span (range) chart with flexible axis/tick visibility and fully
    configurable title/subtitle placement.
    """

    # --- Validate columns
    for col in [category, x_min, x_max]:
        if col not in df.columns:
            raise KeyError(f"Column '{col}' not found in DataFrame")

    # --- Clean and sort data
    data = df.copy()
    data[x_min] = pd.to_numeric(data[x_min], errors="coerce")
    data[x_max] = pd.to_numeric(data[x_max], errors="coerce")
    data = data.dropna(subset=[x_min, x_max])
    if sort_by:
        data = data.sort_values(sort_by, ascending=True).reset_index(drop=True)
    else:
        data = data.sort_values(x_max, ascending=True).reset_index(drop=True)

    # --- Create figure
    fig, ax = plt.subplots(figsize=figsize)
    y = np.arange(len(data))

    # --- Horizontal lines
    ax.hlines(y, xmin=data[x_min], xmax=data[x_max],
              color=color, linewidth=10, alpha=0.6)

    # --- Y labels
    ax.set_yticks(y)
    ax.set_yticklabels(data[category])

    # --- Titles (configurable, no hard-coded defaults)
    if subtitle:
        # Main title
        if use_suptitle:
            suptitle_kwargs = {"fontsize": 14, "fontweight": "bold"}
            if title_x is not None: suptitle_kwargs["x"] = title_x
            if title_y is not None: suptitle_kwargs["y"] = title_y
            fig.suptitle(title, **suptitle_kwargs)
        else:
            ax.set_title(
                title,
                fontsize=14, fontweight="bold", loc="center",
                x=(title_x if title_x is not None else 0.5),
                y=(title_y if title_y is not None else None)
            )

        # Subtitle
        if subtitle_on_axes:
            ax.set_title(subtitle, fontsize=10, fontweight="normal",
                         color="dimgray", loc="center", pad=10)
        else:
            fig.text(
                0.5 if subtitle_x is None else subtitle_x,
                0.94 if subtitle_y is None else subtitle_y,
                subtitle, ha="center", va="top", fontsize=10, color="dimgray", wrap=True
            )

        fig.subplots_adjust(top=0.84 if top_adjust is None else top_adjust)

    else:
        if use_suptitle:
            suptitle_kwargs = {"fontsize": 14, "fontweight": "bold"}
            if title_x is not None: suptitle_kwargs["x"] = title_x
            if title_y is not None: suptitle_kwargs["y"] = title_y
            fig.suptitle(title, **suptitle_kwargs)
        else:
            ax.set_title(
                title,
                fontsize=14, fontweight="bold", loc="center",
                x=(title_x if title_x is not None else 0.5),
                y=(title_y if title_y is not None else None)
            )

        fig.subplots_adjust(top=0.88 if top_adjust is None else top_adjust)

    # --- Axis labels
    if x_labels_show:
        ax.set_xlabel(x_lab)
        ax.xaxis.set_major_formatter(StrMethodFormatter(xfmt))
    if y_labels_show:
        ax.set_ylabel(y_lab)

    # --- Grid control
    ax.grid(grid)

    # --- Remove chart frame
    for spine in ax.spines.values():
        spine.set_visible(False)

    # --- Axis visibility toggles
    if not x_axis_show:
        ax.get_xaxis().set_visible(False)
    if not y_axis_show:
        ax.get_yaxis().set_visible(False)

    # --- Tick mark visibility
    if not x_ticks_show:
        ax.tick_params(axis='x', which='both', length=0)
    if not y_ticks_show:
        ax.tick_params(axis='y', which='both', length=0)

    # --- Add vertical margin for readability
    ax.margins(y=0.15)

    # --- Optional annotations for min/max values
    if annotate:
        for i, row in data.iterrows():
            ax.text(row[x_min], i + annotated_labels_placement_pad, f"${row[x_min]:,.0f}",
                    ha="left", va="bottom", fontsize=10, color="dimgray")
            ax.text(row[x_max], i + annotated_labels_placement_pad, f"${row[x_max]:,.0f}",
                    ha="right", va="bottom", fontsize=10, color="dimgray")

    # --- Respect optional tight layout rect (preserves title/subtitle headroom)
    plt.tight_layout(rect=tight_rect if tight_rect is not None else [0, 0, 1, 0.95])

    return ax

def make_state_map_insets(
    df_states: pd.DataFrame,
    state_col: str = "state",
    category_col: str = "best_paying_role",
    colors: dict | None = None,
    missing_color: str = "#E6E6E6",
    title: str = "",
    subtitle: str | None = None,
    legend_title: str = "",
    title_y: float = 0.965,
    subtitle_pad: int = 12,
    figsize=(10, 7),
    ak_rotate_deg: float = 28.0,  
    hi_rotate_deg: float = 50.0,     # <-- NEW: Hawaii rotation (CCW)
):
    url = "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_state_20m.zip"
    states = gpd.read_file(url)

    data = df_states.copy()
    data[state_col] = data[state_col].str.strip().str.title()
    states["NAME"] = states["NAME"].str.strip().str.title()
    g = states.merge(data, how="left", left_on="NAME", right_on=state_col)
    g = g.to_crs(epsg=5070)

    conus  = g[~g["STUSPS"].isin(["AK", "HI", "PR", "GU", "VI", "AS", "MP"])].copy()
    alaska = g[g["STUSPS"] == "AK"].copy()
    hawaii = g[g["STUSPS"] == "HI"].copy()

    if colors is None:
        colors = {
            "Data Analyst":"#802392",
            "Data Scientist":"#2E6171",
            "Data Engineer":"#43AA8B",
            "Lead Data Architect":"#938BA1",
            "Data Manager":"#000000",
            "Data Editor":"#2E6171"
        }
    for part in (conus, alaska, hawaii):
        part["_color"] = part[category_col].map(colors).fillna(missing_color)

    # --- Rotate AK & HI in their projected CRS (EPSG:5070)
    # Positive angle = counter-clockwise
    alaska_plot = alaska.copy()
    if not alaska_plot.empty and ak_rotate_deg:
        alaska_plot["geometry"] = alaska_plot.geometry.apply(
            lambda g: affinity.rotate(g, ak_rotate_deg, origin="center", use_radians=False)
        )

    hawaii_plot = hawaii.copy()
    if not hawaii_plot.empty and hi_rotate_deg:
        hawaii_plot["geometry"] = hawaii_plot.geometry.apply(
            lambda g: affinity.rotate(g, hi_rotate_deg, origin="center", use_radians=False)
        )

    fig = plt.figure(figsize=figsize)
    ax_main = fig.add_axes([0.08, 0.20, 0.72, 0.70])
    ax_ak   = fig.add_axes([0.08, 0.05, 0.25, 0.25])
    ax_hi   = fig.add_axes([0.36, 0.08, 0.15, 0.15])

    conus.plot(color=conus["_color"], edgecolor="white", linewidth=0.6, ax=ax_main)
    # plot rotated versions in the insets
    (alaska_plot if not alaska_plot.empty else alaska).plot(
        color=alaska["_color"], edgecolor="white", linewidth=0.45, ax=ax_ak
    )
    (hawaii_plot if not hawaii_plot.empty else hawaii).plot(
        color=hawaii["_color"], edgecolor="white", linewidth=0.45, ax=ax_hi
    )

    for ax in (ax_main, ax_ak, ax_hi):
        ax.set_aspect("equal"); ax.axis("off")

    # Titles centered on the figure
    if title:
        fig.text(0.5, title_y, title, ha="center", va="top",
                 fontsize=16, fontweight="bold", color="black")
    if subtitle:
        top = ax_main.get_position().y1
        fig.text(0.5, top + 0.02, subtitle, ha="center", va="bottom",
                 fontsize=11, color="dimgray")

    patches = [mpatches.Patch(color=v, label=k) for k, v in colors.items()]
    # if g[category_col].isna().any():
    #     patches.append(mpatches.Patch(color=missing_color, label="No Data"))
    ax_main.legend(handles=patches, title=legend_title or category_col.replace("_"," ").title(),
                   loc="center left", bbox_to_anchor=(1.02, 0.5), ncol=1,
                   frameon=False, borderaxespad=0.)

    plt.tight_layout(rect=[0.0, 0.0, 0.86, title_y - 0.01])
    fig.patch.set_facecolor("white")
    plt.show()
    return fig, (ax_main, ax_ak, ax_hi)

