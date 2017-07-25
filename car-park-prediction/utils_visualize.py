"""Plot target variable as time series."""

import get_data
from ggplot import aes, geom_line, facet_wrap, ggplot


if __name__ == "__main__":

    df = get_data.get_all_data()

    p = ggplot(df, aes('datetime', 'cap', group='date')) + \
        geom_line(alpha=0.2) + \
        facet_wrap('name')
    p.save('../output/time_series.pdf')
