import pytest

# Dash provides a test fixture `dash_duo` when using dash[testing]
def test_header_present(dash_duo):
    from app import dash_app
    dash_duo.start_server(dash_app)

    # Wait for the header element to be visible
    dash_duo.wait_for_text_to_equal("#header", "Pink Morsel Visualizer")

    assert dash_duo.find_element("#header") is not None


def test_visualization_present(dash_duo):
    from app import dash_app
    dash_duo.start_server(dash_app)

    # Check the graph exists
    assert dash_duo.find_element("#visualization") is not None


def test_region_picker_present(dash_duo):
    from app import dash_app
    dash_duo.start_server(dash_app)

    # Check the radio items are rendered
    assert dash_duo.find_element("#region_picker") is not None
