class Resource:
    def __init__(self, name, gain_per_run, required_amount, count=0.00):
        self.count = count

        self.name = name
        self.gain_per_run = gain_per_run
        self.required_amount = required_amount

    def convert(self, other_resource, ratio):
        old_self_value = self.count
        old_other_resource_value = other_resource.count

        self.count -= ratio
        other_resource.count += 1

        print(f"Converting {self.name}: {old_self_value:.2f}->{self.count:.2f} to {other_resource.name}: {old_other_resource_value:.2f}->{other_resource.count:.2f}")

    def can_convert(self, ratio):
        return self.count - ratio >= self.required_amount

    def add_resources_after_run(self):
        self.count += self.gain_per_run

    def has_required_amount(self):
        return self.count >= self.required_amount


class Inventory:
    def __init__(self, resource_list):
        self.current_run = 0
        self.resource_list = resource_list

    def show_current_status(self):
        strings = [f"{resource.name}: {resource.count:.2f}/{resource.required_amount:.2f}" for resource in self.resource_list]
        compiled_string = " ".join(strings)
        print(f"Run {self.current_run}: {compiled_string}")

    def is_farming_complete(self):
        return all([resource.has_required_amount() for resource in self.resource_list])

    def complete_one_run(self):
        self.current_run += 1
        for resource in self.resource_list:
            resource.add_resources_after_run()


def convert_excess_resources(r1, r2, ratio):
    while r1.can_convert(ratio):
        r1.convert(r2, ratio)


if __name__ == "__main__":
    tier1 = Resource("t1", 2.19, 9.00, count=0.00)
    tier2 = Resource("t2", 2.00, 63.00, count=0.00)
    tier3 = Resource("t3", 0.24, 100.00, count=0.00)

    my_inventory = Inventory([tier1, tier2, tier3])

    while not my_inventory.is_farming_complete():
        my_inventory.complete_one_run()

        # modify conversion logic as needed
        convert_excess_resources(tier1, tier2, 3.00)
        convert_excess_resources(tier2, tier3, 3.00)

        # sample of different conversion logic:
        # if tier2.has_required_amount():
        #     convert_excess_resources(tier1, tier2, 3.00)
        # else:
        #     convert_excess_resources(tier1, tier3, 3.00)

        my_inventory.show_current_status()
