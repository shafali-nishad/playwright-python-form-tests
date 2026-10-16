from playwright.sync_api import sync_playwright, expect


#
def test_name_field_accepts_text(page):
    name_field = page.locator('#name')
    name_field.fill("Shafali")
    expect(name_field).to_have_value("Shafali")


def test_email_field_accepts_text(page):
    page.locator('#email').fill("shafali@example.com")
    expect(page.locator('#email')).to_have_value("shafali@example.com")


def test_phone_field_accepts_text(page):
    phone_number = page.locator("//input[@id='phone']")
    phone_number.fill("9876543210")
    expect(phone_number).to_have_value("9876543210")


def test_gender_radio_button_selection(page):
    gender_option = page.locator("//label[text()='Female']")
    gender_option.scroll_into_view_if_needed()
    gender_option.check()
    expect(gender_option).to_be_checked()


def test_day_checkbox_selection(page):
    day_checkbox = page.get_by_role("checkbox", name="Sunday", exact=True)
    day_checkbox.scroll_into_view_if_needed()
    day_checkbox.check()
    expect(day_checkbox).to_be_checked()
    day_checkbox.uncheck()
    expect(day_checkbox).not_to_be_checked()


def test_country_dropdown_selection(page):
    drop_down = page.locator("#country")
    drop_down.scroll_into_view_if_needed()
    drop_down.select_option(value="india")
    expect(drop_down).to_have_value("india")
