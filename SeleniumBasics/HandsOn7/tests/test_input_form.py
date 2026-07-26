from pages.input_form_page import InputFormPage


def test_input_form_submit(driver):

    page = InputFormPage(driver)

    page.open()

    page.fill_form(
        "Kishore",
        "kishore@gmail.com",
        "Password123",
        "Cognizant",
        "www.google.com",
        "Chennai",
        "Street 1",
        "Street 2",
        "Tamil Nadu",
        "600001"
    )

    page.submit_form()

    assert "Thanks" in page.get_success_message()