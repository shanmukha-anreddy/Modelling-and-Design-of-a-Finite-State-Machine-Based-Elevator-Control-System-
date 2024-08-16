import time

class Elevator:
    def __init__(self):
        self.current_floor = 0
        self.direction = None
        self.door_open = False
        self.requested_floor = None  # Add this line to define the attribute

    def move_up(self):
        self.direction = "up"
        self.current_floor += 1
        print(f"\n╔══════════════════╗")
        print(f"║ Moving Up ║ Floor {self.current_floor} ▲")
        print(f"╚══════════════════╝")
        if self.current_floor == self.requested_floor:
            self.open_doors()
            time.sleep(2)  # Wait for 2 seconds while doors are open
            self.close_doors()
        else:
            print("              ", end="\r")  # Clear previous line
        print(f"Floor {self.current_floor} ◄► ")

    def move_down(self):
        self.direction = "down"
        self.current_floor -= 1
        print(f"\n╔════════════════════╗")
        print(f"║ Moving Down ║ Floor {self.current_floor} ▼")
        print(f"╚════════════════════╝")
        if self.current_floor == self.requested_floor:
            self.open_doors()
            time.sleep(2)  # Wait for 2 seconds while doors are open
            self.close_doors()
        else:
            print("               ", end="\r")  # Clear previous line
        print(f"Floor {self.current_floor} ▲")

    def stop(self):
        self.direction = None
        print("\n╔═════════════╗")
        print("║   Stopping  ║")
        print("╚═════════════╝")

    def open_doors(self):
        self.door_open = True
        print("\n╔═══════════════╗")
        print("║ Opening Doors ║")
        print("╚═══════════════╝")

    def close_doors(self):
        self.door_open = False
        print("\n╔════════════════╗")
        print("║ Closing Doors ║")
        print("╚════════════════╝")


class ElevatorControlSystem:
    def __init__(self):
        self.elevator = Elevator()

    def request_floor(self, floor):
        self.elevator.requested_floor = floor  # Store requested floor in elevator object
        if floor > self.elevator.current_floor:
            while self.elevator.current_floor < floor:
                self.elevator.move_up()
        elif floor < self.elevator.current_floor:
            while self.elevator.current_floor > floor:
                self.elevator.move_down()
        else:
            self.elevator.open_doors()
            time.sleep(2)  # Wait for 2 seconds while doors are open
            self.elevator.close_doors()
            print(f"\nElevator Arrived at Floor {floor}")


def main():
    ecs = ElevatorControlSystem()
    print("----------Welcome to the Elevator Control System--------------")
    while True:
        try:
            floor = input("\nEnter the Floor Number (0 to 10) or 'Exit' to quit: ")
            if floor.lower() == 'exit':
                print("\nExiting...")
                break
            floor = int(floor)
            if floor < 0 or floor > 10:
                print("\nInvalid Floor Number.")
            else:
                ecs.request_floor(floor)
        except ValueError:
            print("\nInvalid Input. Please Enter a valid integer Floor Number.")


if __name__ == "__main__":
    main()
