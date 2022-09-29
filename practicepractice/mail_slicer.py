def mail_slice():
    print("Welcome to the mail slicer")
    print("")

    email_input  = input("Enter your email")
    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")