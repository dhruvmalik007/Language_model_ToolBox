"""
This module provides configuration utilities for datasets.

Imports:
    logging: Provides a way to configure and use loggers.
    re: Provides regular expression matching operations.
    dataclasses: Provides a decorator and functions for creating data classes.

Credits:
    This code is inspired by the Meta FAIR library.
    License: This source code is licensed under the MIT license found in the
    LICENSE file in the root directory of this source tree.
"""

import logging
import re
from dataclasses import dataclass, asdict, fields

## importing various dataset types for the loading purporses (parquet, csv, multimodal data) 
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

## TODO: implement the functionality similar to the fairseq library for assets loading as that of ""from fairseq2.assets import default_asset_store""

class ParquetFormat():
    pyarrow = 0
    huggingface = 1

