
MASTER_INBOX = "info@parkshark.com"
RECRUITMENT_INBOX = "recruitment@parkshark.com"
SPAM_INBOX = "spam@parkshark.com"
SALES_INBOX = "sales@parkshark.com"
RECEPTION_INBOX = "reception@parkshark.com"

# In minutes
TIME_ELAPSED = 0

GLOBAL_EMAIL_COUNTER, GLOBAL_RECRUITMENT_EMAIL_COUNTER, GLOBAL_SPAM_EMAIL_COUNTER, GLOBAL_SALES_EMAIL_COUNTER, GLOBAL_RECEPTION_EMAIL_COUNTER = 0, 0, 0, 0, 0
while True:
    TIME_START = time.current_time_in_minutes()

    if TIME_ELAPSED % 60 == 0:    
        BATCH_EMAIL_COUNTER, BATCH_RECRUITMENT_EMAIL_COUNTER, BATCH_SPAM_EMAIL_COUNTER, BATCH_SALES_EMAIL_COUNTER, BATCH_RECEPTION_EMAIL_COUNTER = 0, 0, 0, 0, 0
        
        new_emails_list = download_inbox(MASTER_INBOX)

        for new_email in new_emails_list:
            if new_email.contains("CV"):
                forward_email_to(RECRUITMENT_INBOX, new_email)
                BATCH_RECRUITMENT_EMAIL_COUNTER += 1
            elif new_email.contains("Promo") or new_email.contains("advertising"):
                forward_email_to(SPAM_INBOX, new_email)
                BATCH_SPAM_EMAIL_COUNTER += 1
            elif new_email.contains("proposal"):
                forward_email_to(SALES_INBOX, new_email)
                BATCH_SALES_EMAIL_COUNTER += 1
            else:
                forward_email_to(RECEPTION_INBOX, new_email)
                BATCH_RECEPTION_EMAIL_COUNTER += 1

            delete_email_from(MASTER_INBOX, new_email)

            BATCH_EMAIL_COUNTER += len(new_emails_list)

            GLOBAL_EMAIL_COUNTER += BATCH_EMAIL_COUNTER
            GLOBAL_RECRUITMENT_EMAIL_COUNTER += BATCH_RECRUITMENT_EMAIL_COUNTER
            GLOBAL_SPAM_EMAIL_COUNTER += BATCH_SPAM_EMAIL_COUNTER
            GLOBAL_SALES_EMAIL_COUNTER += BATCH_SALES_EMAIL_COUNTER
            GLOBAL_RECEPTION_EMAIL_COUNTER += BATCH_RECEPTION_EMAIL_COUNTER

            print(f"We have sorted {BATCH_EMAIL_COUNTER} emails")
            print(f"\t{BATCH_RECRUITMENT_EMAIL_COUNTER} to recruitment")
            print(f"\t{BATCH_SPAM_EMAIL_COUNTER} to spam")
            print(f"\t{BATCH_SALES_EMAIL_COUNTER} to sales")
            print(f"\t{BATCH_RECEPTION_EMAIL_COUNTER} to reception")


    if time.current_time() == "1700":
        print(f"We have sorted {GLOBAL_EMAIL_COUNTER} emails")
        print(f"\t{GLOBAL_RECRUITMENT_EMAIL_COUNTER} to recruitment")
        print(f"\t{GLOBAL_SPAM_EMAIL_COUNTER} to spam")
        print(f"\t{GLOBAL_SALES_EMAIL_COUNTER} to sales")
        print(f"\t{GLOBAL_RECEPTION_EMAIL_COUNTER} to reception")

    TIME_ELAPSED += time.current_time_in_minutes() - TIME_START