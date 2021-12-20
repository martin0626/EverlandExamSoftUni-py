class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        rooms_expenses = 0
        for room in self.rooms:
            rooms_expenses += room.expenses + room.room_cost
        return f'Monthly consumptions: {rooms_expenses}$.'

    def pay(self):
        result_string = ''

        for room in self.rooms:
            room_price = room.expenses + room.room_cost

            if room_price <= room.budget:
                result_string += f'{room.family_name} paid {room_price:.2f}$ and have {room.budget - room_price:.2f}$ left.'
                room.budget -= room_price
            else:
                result_string += f'{room.family_name} does not have enough budget and must leave the hotel.'
                self.rooms.remove(room)
        return result_string

    def status(self):
        total_population = sum([r.members_count for r in self.rooms])
        result_string = f'Total population: {total_population}'

        for room in self.rooms:
            room_name = room.family_name
            room_members = room.members_count
            room_budget = room.budget
            room_expenses = room.expenses
            result_string += f'\n{room_name} with {room_members} members. Budget: {room_budget:.2f}$, Expenses: {room_expenses:.2f}$'
            if len(room.children) > 0:
                child_str = ''

                for child in room.children:
                    num = room.children.index(child) + 1
                    child_str += f'\n--- Child {num} monthly cost: {child.get_monthly_expense():.2f}$'
                result_string += child_str
            if hasattr(room, 'appliances'):
                appliances_cost = sum([ap.get_monthly_expense() for ap in room.appliances])
                result_string += f'\n--- Appliances monthly cost: {appliances_cost:.2f}$'

        return result_string
