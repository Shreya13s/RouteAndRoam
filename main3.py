from module3 import PlacesModule
pm= PlacesModule(r"C:\Users\mgpre\Documents\python\places.csv")
mod = PlacesModule(r"C:\Users\mgpre\Documents\python\places.csv")


# Step 1: enter country
country = input("Enter a country name: ")

places = mod.list_places_by_country(country)

if not places:
    print("No places found for this country.")
    exit()

print("\nPlaces available in", country.title())
for p in places:
    print("-", p.title())

# Step 2: enter place
place = input("\nEnter a place from the list: ")

info = mod.get_place_info(country, place)

if info is None:
    print("Place not found under this country.")
else:
    print("\n--- DETAILS ---")
    print("Country:", info["COUNTRY"].title())
    print("Place:", info["PLACE"].title())
    print("Language:", info["LANGUAGE"])
    print("Timezone:", info["TIMEZONE"])
    print("Specialities:", info["SPECIALITIES"])

    print("\nOpening image...")
    mod.show_image(info["IMAGES"])
