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
from typing import Enum, Optional, List

## importing various dataset types for the loading purporses (parquet, csv, multimodal data) 
import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq

## TODO: implement the functionality similar to the fairseq library for assets loading as that of ""from fairseq2.assets import default_asset_store"
class ParquetFormat():
    pyarrow = 0
    huggingface = 1
    pandas = 2

class SonarEmbeddings:
    pass

class ColumnsNames(Enum):
    STANDARD_SOURCE_COLUMN = "_source_column"
    STANDARD_SOURCE_TEXT_COLUMN = "_source_text_column"
    STANDARD_TARGET_COLUMN = "_target_column"
    STANDARD_TARGET_TEXT_COLUMN = "_target_text_column"
    STANDARD_DATASET_NAME = "_dataset_name"

    HUGGINGFACE_SOURCE_COLUMN = "source"
    HUGGINGFACE_SOURCE_TEXT_COLUMN = "source_text"
    HUGGINGFACE_TARGET_COLUMN = "target"
    HUGGINGFACE_TARGET_TEXT_COLUMN = "target_text"
    HUGGINGFACE_DATASET_NAME = "dataset_name"

    @staticmethod
    def get_column_names(format_type: str):
        if format_type == "standard":
            return {
                "source_column": ColumnsNames.STANDARD_SOURCE_COLUMN.value,
                "source_text_column": ColumnsNames.STANDARD_SOURCE_TEXT_COLUMN.value,
                "target_column": ColumnsNames.STANDARD_TARGET_COLUMN.value,
                "target_text_column": ColumnsNames.STANDARD_TARGET_TEXT_COLUMN.value,
                "dataset_name": ColumnsNames.STANDARD_DATASET_NAME.value,
            }
        elif format_type == "huggingface":
            return {
                "source_column": ColumnsNames.HUGGINGFACE_SOURCE_COLUMN.value,
                "source_text_column": ColumnsNames.HUGGINGFACE_SOURCE_TEXT_COLUMN.value,
                "target_column": ColumnsNames.HUGGINGFACE_TARGET_COLUMN.value,
                "target_text_column": ColumnsNames.HUGGINGFACE_TARGET_TEXT_COLUMN.value,
                "dataset_name": ColumnsNames.HUGGINGFACE_DATASET_NAME.value,
            }
        else:
            raise ValueError(f"Unknown format type: {format_type}")








class DatasetConfig():
    """
    generic dataset configuration from original dataset
    but adapted to all of the datatypes. 
    """
    columns: Optional[List[str]] = None
    """The list of columns to load.
    Columns such as `source_column`, ..., will be added automatically.
    """

    source_text_column: Optional[str] = None
    """ Column to load as source raw text"""

    target_text_column: Optional[str] = None
    """ Column to load as target raw text for paired data"""

    source_prefix_text: Optional[str] = None
    """ Text to prepend to the content of the source_column"""

    source_suffix_text: Optional[str] = None
    """ Text to append to the content of the target_column"""

    target_prefix_text: Optional[str] = None
    """ Text to prepend to the content of the source_column"""

    target_suffix_text: Optional[str] = None
    """ Text to append to the content of the target_column"""

    source_sequences = Optional[List[SonarEmbeddings]] = None