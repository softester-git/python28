def test_contact_home_page_eq_edit_page(app, db):
    contacts = db.get_contact_list()
    contacts_home = app.contact.get_contact_list()
    for home_record in contacts_home:
        db_record = list(filter(lambda x: x.id == home_record.id, contacts))[0]
        assert str(db_record.firstname).strip() == str(home_record.firstname).strip()
        assert str(db_record.lastname).strip() == str(home_record.lastname).strip()
        assert str(db_record.address).strip() == str(home_record.address).strip()
        home_phones = "".join(home_record.all_phones_from_home.split("\n"))
        db_phones = [str(db_record.phone_home), str(db_record.phone_mobile), str(db_record.phone_work), str(db_record.phone2)]
        assert "".join(app.contact.clear_all_phones(db_phones)) == home_phones
        db_emails = str(db_record.email) + str(db_record.email2) + str(db_record.email3)
        home_emails = home_record.all_emails_from_home.replace("\n", "")
        assert db_emails == home_emails