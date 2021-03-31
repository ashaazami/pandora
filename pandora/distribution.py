import pandas as pd
import plotnine as plot
import numpy as np


def plot_vs_discrete(data_table,
                     discrete_metric_name,
                     metric_name,
                     segment_name,
                     title,
                     ylim=None,
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


def plot_vs_continuous(data_table,
                       continuous_metric_name,
                       breaks,
                       metric_name,
                       segment_name,
                       title,
                       aggregate="mean"):
    result = _aggregate_vs_continuous(data_table, continuous_metric_name, breaks, metric_name, segment_name, aggregate)
    gg_result = plot.ggplot(result) + plot.aes(x="level_0",
                                               y=metric_name,
                                               fill=segment_name,
                                               label=metric_name
                                               ) + \
                plot.geom_bar(stat="identity", position="dodge") + \
                plot.geom_text(position=plot.position_dodge(width=.9), size=8) + \
                plot.labs(x=continuous_metric_name, y=aggregate + "(" + metric_name + ")", title=title)
    return gg_result


def plot_scatter_vs_continuous(data_table,
                               continuous_metric_name,

                               metric_name,
                               segment_name,
                               title,
                               aggregate="mean"):
    gg_result = plot.ggplot(data_table) + plot.aes(x=continuous_metric_name,
                                                   y=metric_name,
                                                   fill=segment_name,
                                                   label=metric_name
                                                   ) + \
                plot.geom_point(stat="identity") + \
                plot.labs(x=continuous_metric_name, y=aggregate + "(" + metric_name + ")", title=title)
    return gg_result


def plot_continuous_distribution(data_table,
                                 continuous_metric_name,
                                 segment_name,
                                 title,
                                 xlim=None):
    filtered_data = data_table[
        pd.notnull(data_table[continuous_metric_name]) & pd.notnull(data_table[continuous_metric_name])]
    result = plot.ggplot(data=filtered_data) + plot.aes(x=continuous_metric_name, color=segment_name) + \
             plot.geom_density() + plot.labs(x=continuous_metric_name, title=title, fill=segment_name)

    if pd.notnull(xlim):
        result = result + plot.xlim(xlim)
    return result


def bin_and_plot_vs_continuous(data_table,
                               continuous_metric_name,
                               breaks,
                               metric_name,
                               segment_name,
                               title,
                               aggregation="mean"):
    quantile = _quantile_bin(data_table, continuous_metric_name, breaks)

    result = plot_vs_continuous(data_table, continuous_metric_name, quantile, metric_name, segment_name, title,
                                aggregation)
    return result


def _quantile_bin(data_table, continuous_metric_name, number_of_bins):
    q = np.linspace(0, 1, num=number_of_bins)
    quantiles = np.unique(np.quantile(data_table[continuous_metric_name], q=q))
    return quantiles


def _factor_by_quantile(data_table, continuous_metric_name, number_of_bins):
    quantiles = _quantile_bin(data_table, continuous_metric_name, number_of_bins)
    factors = pd.Categorical(
        pd.cut(data_table[continuous_metric_name], right=False, include_lowest=True, bins=quantiles))
    return factors


def _aggregate_vs_continuous(data_table,
                             continuous_metric_name,
                             bins,
                             metric_name,
                             segment_name,
                             aggregate="mean"):
    data_filtered = \
        data_table.loc[((pd.notnull(data_table[metric_name])) & (pd.notnull(data_table[continuous_metric_name])))][
            [continuous_metric_name, metric_name, segment_name]]
    result = data_filtered.groupby(
        [pd.Categorical(pd.cut(data_filtered[continuous_metric_name], right=False, include_lowest=True, bins=bins)),
         segment_name]).agg({metric_name: aggregate}).reset_index()

    result[metric_name] = round(result[metric_name], 3)

    return result
