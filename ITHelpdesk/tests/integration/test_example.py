import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    # Go to http://127.0.0.1:8000/
    page.goto("http://127.0.0.1:8000/")
    # Click text=Log In
    page.locator("text=Log In").click()
    expect(page).to_have_url("http://127.0.0.1:8000/login")
    # Click text=Create an account
    page.locator("text=Create an account").click()
    expect(page).to_have_url("http://127.0.0.1:8000/register")
    # Fill input[name="username"]
    page.locator("input[name=\"username\"]").fill("Khan")
    # Fill input[name="first_name"]
    page.locator("input[name=\"first_name\"]").fill("KhanFname")
    # Fill input[name="last_name"]
    page.locator("input[name=\"last_name\"]").fill("KhanLname")
    # Fill input[name="email"]
    page.locator("input[name=\"email\"]").fill("Khanemail@live.com")
    # Fill input[name="password1"]
    page.locator("input[name=\"password1\"]").fill("gskdfhjl20345897")
    # Fill input[name="password2"]
    page.locator("input[name=\"password2\"]").fill("gskdfhjl20345897")
    # Click button:has-text("Register")
    page.locator("button:has-text(\"Register\")").click()
    expect(page).to_have_url("http://127.0.0.1:8000/")
    # Click text=Create Ticket
    page.locator("text=Create Ticket").click()
    expect(page).to_have_url("http://127.0.0.1:8000/tickets")
    # Fill input[name="title"]
    page.locator("input[name=\"title\"]").fill("TEST")
    # Fill input[name="subject"]
    page.locator("input[name=\"subject\"]").fill("TEST")
    # Select HIGH
    page.locator("select[name=\"priority\"]").select_option("HIGH")
    # Fill textarea[name="description"]
    page.locator("textarea[name=\"description\"]").fill("TEST")
    # Click text=Submit
    page.locator("text=Submit").click()
    expect(page).to_have_url("http://127.0.0.1:8000/")
    # Click text=edit
    page.locator("text=edit").click()
    expect(page).to_have_url(re.compile("http://127.0.0.1:8000/update/.*"))
    # Click html
    page.locator("html").click()
    # Fill input[name="title"]
    page.locator("input[name=\"title\"]").fill("NOTATEST")
    # Click text=Submit
    page.locator("text=Submit").click()
    page.wait_for_url("http://127.0.0.1:8000/")
    # Click text=delete
    page.locator("text=delete").click()
    expect(page).to_have_url("http://127.0.0.1:8000/")
    # Click text=Account Details
    page.locator("text=Account Details").click()
    expect(page).to_have_url("http://127.0.0.1:8000/profile")
    expect(page.locator("text=Username:Khan"))
    # Click text=Edit
    page.locator("text=Edit").click()
    expect(page).to_have_url(re.compile("http://127.0.0.1:8000/profile/edit/.*"))
    # Fill input[name="username"]
    page.locator("input[name=\"username\"]").fill("NotKhan")
    # Click text=Submit
    page.locator("text=Submit").click()
    expect(page).to_have_url("http://127.0.0.1:8000/")
    # Click text=Account Details
    page.locator("text=Account Details").click()
    expect(page).to_have_url("http://127.0.0.1:8000/profile")
    expect(page.locator("text=Username:NotKhan"))
    # Click text=Return
    page.locator("text=Return").click()
    expect(page).to_have_url("http://127.0.0.1:8000/")
    # Click text=Log Out
    page.locator("text=Log Out").click()
    expect(page).to_have_url("http://127.0.0.1:8000/login")
    # Fill input[name="username"]
    page.locator("input[name=\"username\"]").fill("NotKhan")
    # Fill input[name="password"]
    page.locator("input[name=\"password\"]").fill("gskdfhjl20345897")
    # Click button:has-text("Login")
    page.locator("button:has-text(\"Login\")").click()
    expect(page).to_have_url("http://127.0.0.1:8000/")
    # Click text=Account Details
    page.locator("text=Account Details").click()
    expect(page).to_have_url("http://127.0.0.1:8000/profile")
    page.locator("text=DELETE ACCOUNT").click()