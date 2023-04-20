addresses = {
    "Pluralsight": "182 N. Union Ave, Farmington, UT 84025",
    "Apple": "One Infinite Loop. Cupertino, CA 95014",
    "Microsoft": "One Microsoft Way, Redmond, WA 98052-6399"
}

contact = input("Contact name?" )
if contact in addresses:
    print(contact, ":\n--------------")
    print(addresses[contact])

else:
    print("Unknown contact")
