# vehicles w attributes: brand, model, km done so far, general service date
# user should be able to see a list of all vehicles, edit kilometers and change the general service date and add new vehicles
# data stored in a txt.-file

class vehicle():
    def __init__(self, brand, model, km_done_so_far, general_service_date):
        self.brand = brand
        self.model = model
        self.km_done_so_far = km_done_so_far
        self.general_service_date = general_service_date


def list_all_vehicles(vehicles):
    if not vehicles:
        print "Sorry, you don\'t have any vehicles in your list."
    else:
        for index, vehicle in enumerate(vehicles):
            print "%s / %s %s, %s km. Next service date: %s." % (index+1, vehicle.brand,
                                                                      vehicle.model, vehicle.km_done_so_far,
                                                                      vehicle.general_service_date)

def create_vehicle(brand, model, km_done_so_far, general_service_date, vehicles):
    new_vehicle = vehicle(brand=brand, model=model, km_done_so_far=km_done_so_far,
                          general_service_date=general_service_date)
    vehicles.append(new_vehicle)

    return True

def add_new_vehicle(vehicles):
    brand = raw_input("Please enter the brand of the vehicle: ")
    model = raw_input("Please enter the model of the vehicle: ")
    km_done_so_far = raw_input("Please enter the km of the vehicle: ")
    general_service_date = raw_input("Please enter the date of the next general service: ")

    result = create_vehicle(brand, model, km_done_so_far, general_service_date, vehicles)

    if result:
        print "You added the new vehicle %s %s to the list." % (brand, model)
        print ""
    else:
        return

def choose_vehicle(vehicles):
    print "Please select the ID of the vehicle you'd like to edit. "

    print ""
    print list_all_vehicles(vehicles)
    print "__________"

    selection = raw_input("Which vehicle do you want to edit? Please enter the ID: ")
    return vehicles[int(selection) -1]

def edit_vehicle_km(vehicles):
    selected_vehicle = choose_vehicle(vehicles)

    print "You selected the vehicle: %s %s with %s km." % (selected_vehicle.brand, selected_vehicle.model, selected_vehicle.km_done_so_far)
    print "_________"

    new_km_done_so_far = raw_input("Please enter the new amount of km done so far of the vehicle: ")
    selected_vehicle.km_done_so_far = new_km_done_so_far

    print ""
    print "The amount of km done so far got updated."
    print ""


def change_general_service_date(vehicles):
    selected_vehicle = choose_vehicle(vehicles)

    print "You selected the vehicle: %s %s with general service date %s." % (selected_vehicle.brand, selected_vehicle.model, selected_vehicle.general_service_date)

    new_general_service_date = raw_input("Please enter the new date of the next general service (DD/MM/YY: ")
    selected_vehicle.general_service_date = new_general_service_date

    print ""
    print "The new date of the general service got updated."
    print ""

def save_to_disk(vehicles):
    with open("vehicles.txt", "w+") as veh_file:
        for vehicle in vehicles:
            veh_file.write("%s, %s, %s, %s\n" % (vehicle.brand, vehicle.model, vehicle.km_done_so_far, vehicle.general_service_date))

def main():
    print "Welcome to the vehicle manager!"
    print "*" * 20

    vehicles = []

    with open("vehicles.txt", "r") as v_file:
        for line in v_file:
            try:
                brand, model, km_done_so_far, general_service_date = line.split(",")
                create_vehicle(brand, model, km_done_so_far, general_service_date, vehicles)
            except ValueError:
                continue

    while True:
        print "What do you want do? Please select one of these options:"
        print "a) See the list of all vehicles"
        print "b) Add a new vehicle"
        print "c) Edit the km done so far"
        print "d) Change the general service date"
        print "x) Quit the program"

        selection = raw_input("Please enter your selection (a, b, c or x): ")

        if selection.lower() == "a":
            list_all_vehicles(vehicles)

        elif selection.lower() == "b":
            add_new_vehicle(vehicles)

        elif selection.lower() == "c":
            edit_vehicle_km(vehicles)

        elif selection.lower() == "d":
            change_general_service_date(vehicles)

        elif selection.lower() == "x":
            print "Thank you for using the vehicles manager. Goodbye!"
            print "_________"

            save_to_disk(vehicles)
            break

        else:
            print 'Sorry, the program couldn\'t read your selection. Please select one option.'
            continue


if __name__ == "__main__":
    main()
