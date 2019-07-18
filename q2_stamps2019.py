import functools

import pandas as pd
import qiime2.plugin
import qiime2.sdk

from q2_types.feature_table import BIOMV100Format, BIOMV210Format


plugin = qiime2.plugin.Plugin(
    name='stamps2019',
    version='2019.4.0',
    website='',
    package='q2_stamps2019',
    description='',
    short_description='',
)


# This seems to handle a variety of R's write.table products robustly, and
# without error. YMMV.
read_csv = functools.partial(pd.read_csv, sep='\t', index_col=0)


class RWriteDotTableFormat(qiime2.plugin.model.TextFileFormat):
    def _validate_(self, level):
        try:
            read_csv(str(self))
        except Exception as exception:
            raise qiime2.plugin.ValidationError(exception) from exception


def transformer(ff: RWriteDotTableFormat) -> BIOMV210Format:
    df = read_csv(str(ff))

    pm = qiime2.sdk.PluginManager()
    xformer = pm.plugins['types'].transformers[pd.DataFrame, BIOMV210Format]

    return xformer.transformer(df)


plugin.register_transformer(transformer)
plugin.register_views(RWriteDotTableFormat)
