from pages.seach_form_main_p import CarSearchForm


def test_search_form_accepts_a_city_and_opens_calendar(driver):
    search_form = CarSearchForm(driver)
    search_form.open()

    search_form.fill_city("Tel Aviv")
    assert search_form.selected_city() == "Tel Aviv"

    calendar = search_form.open_date_picker()
    assert calendar.is_displayed()
    assert not search_form.is_submit_enabled()
