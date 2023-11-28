import logging
import os
import pytest
from datetime import datetime
from pytest import Cache
from configs.env_dev import EnvDev
from configs.env_qa import EnvQA


LOG = logging.getLogger(__name__)

# Loads free form configs on start and caches globally
def pytest_sessionstart(session):
    load_env()

def load_env():
    env = os.environ.get("TEST_ENV", "DEV").upper()
    
    valid_envs: dict = { "DEV": EnvDev, "QA": EnvQA }
        
    # Set Default env if not valid
    if env not in valid_envs:
        LOG.warning(f"Selected env {env} was not a valid choice {list(valid_envs.keys())}! Loading default DEV")
        env = EnvDev
    else:
        env = valid_envs[env]

    Cache._config = env().model_dump()
    return Cache._config

def pytest_sessionfinish(session, exitstatus):
    """ whole test run finishes. """
    return exitstatus


def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Description</th>")
    cells.insert(1, '<th class="sortable time" data-column-type="time">Time</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f"<td>{report.description}</td>")
    cells.insert(1, f'<td class="col-time">{datetime.now()}</td>')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)

    
    

    

        
    
    
    
    

    