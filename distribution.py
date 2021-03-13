import pandas as pd
import plotnine as plot


def plot_vs_discrete(data_table,
                     discrete_metric_name,
                     metric_name,
                     segment_name,
                     title,
                     ylim,
                     aggregate="mean"
                     ):
    data_filtered = \
        data_table.loc[((pd.notnull(data_table[metric_name])) & (pd.notnull(data_table[discrete_metric_name])))][
            [discrete_metric_name, metric_name, segment_name]]

    data_filtered[[metric_name]] = data_filtered[[metric_name]].astype(float)
    result = data_filtered.groupby([discrete_metric_name, segment_name]).agg({metric_name: aggregate}).reset_index()
    result[metric_name] = round(result[metric_name], 3)

    gg_result = plot.ggplot(result) + plot.aes(x=discrete_metric_name,
                                               y=metric_name,
                                               fill=segment_name,
                                               label=metric_name
                                               ) + \
                plot.geom_bar(stat="identity", position="dodge") + \
                plot.geom_text(position=plot.position_dodge(width=.9), size=8) + \
                plot.labs(x=discrete_metric_name, y=aggregate + "(" + metric_name + ")", title=title)

    if pd.notnull(ylim):
        gg_result = gg_result + plot.ylim(ylim)

    return gg_result
