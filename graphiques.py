import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pathlib import Path
from collections import Counter
import matplotlib.ticker as ticker


def plot_multi_stacked_bar(ax, data, questions, title, font_size, pad,categories=None, colors=None, yticklabels=None):
        results = []
        for q in questions:
            valid_values = data[q].dropna()
            for val in valid_values:
                if pd.isna(val) or str(val).strip() == '':
                    continue
                choices = [c.strip() for c in str(val).split(';')]
                for cat in categories:
                    results.append({
                        'Question': q,
                        'Category': cat,
                        'Count': 1 if cat in choices else 0
                    })

        df = pd.DataFrame(results)
        pivot_df = df.pivot_table(index='Question', columns='Category',
                                values='Count', aggfunc='sum', fill_value=0)

        pivot_df = pivot_df.reindex(questions)

        # Normalize and reorder
        pivot_df = pivot_df.div(pivot_df.sum(axis=1), axis=0)
        pivot_df = pivot_df[[c for c in categories if c in pivot_df.columns]]
        # Plotting
        pivot_df.plot(kind='barh', stacked=True, ax=ax, color=colors,
                     edgecolor='white', linewidth=0.5)
        ax.invert_yaxis()

        # Labeling
        for i, (idx, row) in enumerate(pivot_df.iterrows()):
            cum_width = 0
            for j, (cat, value) in enumerate(row.items()):
                if value > 0.01:
                    ax.text(
                        cum_width + value / 2,
                        i,
                        f"{int(value * 100)}%",
                        va='center',
                        ha='center',
                        fontsize=font_size,
                        color='black'
                    )
                cum_width += value

        # Customisation
        ax.set_title(title, fontsize=font_size, pad=pad)
        ax.set_yticklabels(yticklabels, fontsize=font_size)
        ax.set_ylabel("")
        for spine in ['top', 'right', 'left']:
            ax.spines[spine].set_visible(False)
        ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left',
                 borderaxespad=0., prop={'size': font_size}, frameon=False)

def plot_score_distribution(ax, data, n_range, x_text, font_size, label_pad, title):
    data = data.copy()
    ne_sait_pas_count = (data == "-1").sum()
    numeric_data = data[data != "-1"].astype(int)
    moyenne_data=np.average(numeric_data)

    counts = numeric_data.value_counts().reindex(range(n_range), fill_value=0)
    colors = sns.diverging_palette(220, 280, s=70, l=85, n=n_range)

    # Préparer le graphique
    ax.set_title(title, fontsize=font_size, y=0.88)
    ax.set_xlim(0, n_range)
    ax.set_ylim(-0.7, 0.5)  # Extended ylim to accommodate "Ne sait pas" text

    # Plot each score
    left = 0
    for score in range(n_range):
        count = counts[score]
        color = colors[score]

        ax.barh(
            y=0,
            width=1,
            left=left,
            color=color,
            height=0.6,
            edgecolor='white',
            linewidth=1
        )

        if count > 0:
            ax.text(
                left + 0.5, 0,
                f"{count}",
                va='center',
                ha='center',
                color='black',
                fontsize=font_size,
                fontweight='bold'
            )

        if score == 10 and title=="Nombre de fiches actions rédigées concrétisant\nles priorités communes à court terme":
            label_text = "10 +"
        else:
            label_text = str(score)

        ax.text(
            left + 0.5, -0.4,
            label_text,
            ha='center',
            va='center',
            fontsize=font_size
        )
        left += 1

    ax.text(
        n_range/2, -0.8,
        x_text,
        ha='center',
        va='center',
        fontsize=font_size,
        )

    ax.text(
        n_range/2, -0.6,  # Centered position below the main plot
        f"Moyenne des réponses: {moyenne_data:.1f}",
        ha='center',
        va='center',
        fontsize=font_size,
    )


    # Add "Ne sait pas" count if any
    if ne_sait_pas_count > 0:
        ax.text(
            n_range/2, -0.8,  # Centered position below the main plot
            f"Nombre de répondant ayant répondu 'Ne sait pas': {ne_sait_pas_count}",
            ha='center',
            va='center',
            fontsize=font_size,
        )


    # Customize
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ['top', 'right', 'left', 'bottom']:
        ax.spines[spine].set_visible(False)

def plot_respondent_counts(ax, data, questions, categories, font_size, title):
    ax.axis('off')
    counts = {}

    for q in questions:
        for val in data[q].dropna():
            choices = [c.strip() for c in str(val).split(';')]
            for cat in categories:
                if cat in choices:
                    counts[cat] = counts.get(cat, 0) + 1

    # Add title
    ax.text(0.5, 1, title, fontsize=font_size, ha='center', va='top', transform=ax.transAxes, weight='bold')

    # Add respondent counts in one line
    response_text = " | ".join([f"{cat}: {counts.get(cat, 0)}" for cat in categories])
    ax.text(0.5, 0.5, response_text, fontsize=font_size, ha='center', va='center', transform=ax.transAxes)

def plot_side_graph(ax,data,font_size,column_presented,fixed_order,title,color_palette, column_used=None,exclude=None):

    xlabel="Nombre de réponses"

    bar_width = 0.6


    def count_mentions(column):
        mentions = []
        for value in column.dropna():
            mentions.extend(v.strip() for v in str(value).split(';'))
        counter = Counter(mentions)
        if exclude:
            for item in exclude:
                counter.pop(item, None)
        return counter

    # ---------- Count primary ----------
    counts_1 = count_mentions(data[column_presented])
    values_1 = [counts_1.get(tool, 0) for tool in fixed_order]

    # ---------- Optional second dataset ----------
    has_second = column_used is not None

    if has_second:
        counts_2 = count_mentions(data[column_used])
        values_2 = [counts_2.get(tool, 0) for tool in fixed_order]

    # ---------- Axis scaling ----------
    max_count = max(values_1) if not has_second else max(max(values_1), max(values_2))
    x_limit = max_count * 1.15 if max_count > 0 else 10

    y_pos = np.arange(len(fixed_order)) * 1.8
    colors = color_palette[:len(fixed_order)]

    # ---------- Plot ----------
    if has_second:
        ax.barh(
            y_pos + bar_width / 2,
            values_1,
            bar_width,
            color=colors,
            edgecolor='white',
            linewidth=0.2,
            label='Présentés'
        )
        ax.barh(
            y_pos - bar_width / 2,
            values_2,
            bar_width,
            color=colors,
            edgecolor='black',
            linewidth=0.2,
            alpha=0.5,
            hatch='/',
            label='Utilisés'
        )
    else:
        ax.barh(
            y_pos,
            values_1,
            bar_width,
            color=colors,
            edgecolor='white',
            linewidth=0.6,
            label='Nombre de réponses'
        )

    # ---------- Labels ----------
    ax.set_yticks(y_pos)
    ax.set_yticklabels(fixed_order, fontsize=font_size)
    ax.set_xlabel(xlabel, fontsize=font_size)
    ax.set_title(title, fontsize=font_size)
    ax.set_xlim(0, x_limit)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.tick_params(axis='x', labelsize=font_size)

    # ---------- Value annotations ----------
    for i, v in enumerate(values_1):
        if v > 0:
            ax.text(v * 1.05, y_pos[i] + bar_width / 2, f"{v}", va='center',
                    fontsize=font_size, fontweight='bold')

    if has_second:
        for i, v in enumerate(values_2):
            if v > 0:
                ax.text(v * 1.05, y_pos[i] - bar_width / 2,
                        f"{v}", va='center',
                        fontsize=font_size, fontweight='bold', alpha=0.8)

    # ---------- Style ----------
    ax.grid(True, axis='x', alpha=0.3, linestyle='--')

    if column_used is not None:
        ax.legend(
            bbox_to_anchor=(1.05, 1),
            loc='upper left',
            prop={'size': font_size},
            frameon=False
        )

    for spine in ['top', 'right', 'left']:
        ax.spines[spine].set_visible(False)
