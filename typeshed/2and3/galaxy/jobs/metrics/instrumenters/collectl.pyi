# Stubs for galaxy.jobs.metrics.instrumenters.collectl (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import formatting
from ..instrumenters import InstrumentPlugin

class CollectlFormatter(formatting.JobMetricFormatter):
    def format(self, key, value): ...

class CollectlPlugin(InstrumentPlugin):
    plugin_type = ...  # type: str
    formatter = ...  # type: Any
    saved_logs_path = ...  # type: Any
    summarize_process_data = ...  # type: Any
    log_collectl_program_output = ...  # type: Any
    process_statistics = ...  # type: Any
    def __init__(self, **kwargs) -> None: ...
    def pre_execute_instrument(self, job_directory): ...
    def post_execute_instrument(self, job_directory): ...
    def job_properties(self, job_id, job_directory): ...
