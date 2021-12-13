from random import randrange


def test_check_contact_phones(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_edit_page = app.contact.get_contact_from_edit_page(index)
    assert contacts[index].all_emails_from_home == app.merge_emails_like_on_home_page(contact_from_edit_page)
    assert contacts[index].all_phones_from_home == app.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contacts[index].address == contact_from_edit_page.address
    assert contacts[index].firstname == contact_from_edit_page.firstname
    assert contacts[index].lastname == contact_from_edit_page.lastname
