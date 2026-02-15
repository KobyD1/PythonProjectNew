import pytest
import os
from playwright.sync_api import sync_playwright
import subprocess
import urllib
import json



@pytest.fixture(name="browser")
def playwright_browser():
    print(run_on)
    if run_on == 'local':
        with sync_playwright() as playwright:
          browser = playwright.chromium.launch(headless=True)
    yield browser

if run_on == 'cloud':
    with sync_playwright() as playwright:
        playwrightVersion = str(subprocess.getoutput('playwright --version')).strip().split(" ")[1]
        capabilities['LT:Options']['playwrightClientVersion'] = playwrightVersion
        lt_cdp_url = 'wss://cdp.lambdatest.com/playwright?capabilities=' + urllib.parse.quote(json.dumps(capabilities))
        browser = playwright.chromium.connect(lt_cdp_url)
    yield browser