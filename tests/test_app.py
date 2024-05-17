import os.path

from streamlit.testing.v1 import AppTest


def test_app_error():
    """tests any error occurs during testing the code of streamlit app"""
    test_dir=os.path.dirname(os.path.abspath(__file__))
    app_script_path=os.path.join(test_dir,"..","welcome_👋️.py")
    assert os.path.isfile(app_script_path),f"File not found at {app_script_path}"
    at = AppTest.from_file(app_script_path)
    # at.button[0].click().run()
    at.sidebar[0].success().run()
    at.run()
