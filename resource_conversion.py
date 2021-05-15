def is_complete(required, current):
    ret = False

    z = zip(required.values(), current.values())
    ret = all([c >= r for r, c in z])

    return ret


def show_current_status(current_iteration, required, current):
    z = zip(required.values(), current.values())
    strings = [f"{c:.2f}/{r}" for r, c in z]

    # i starts from 0, so add 1
    compiled_string = " ".join([f"t{i+1}: {s}" for i, s in enumerate(strings)])

    print(f"Run {current_iteration}: {compiled_string}")


def add_resources_after_run(gain, current):
    for k, v in gain.items():
        current[k] += v


def convert_excess_resources(conversion, required, current):
    for i, v in enumerate(conversion.values()):
        tier_num = i+1  # i starts from 0, so add 1
        while can_convert(tier_num, v, required, current):
            convert_one_resource(tier_num, v, current)


def can_convert(tier, ratio, required, current):
    ret = False

    tier_key = f"t{tier}"
    if current[tier_key] - ratio >= required[tier_key]:
        ret = True

    return ret


def convert_one_resource(tier, ratio, current):
    lower_tier = f"t{tier}"
    higher_tier = f"t{tier+1}"

    old_lower_tier_value = current[lower_tier]
    old_higher_tier_value = current[higher_tier]

    current[lower_tier] -= ratio
    current[higher_tier] += 1.0

    print(f"Converting {lower_tier}: {old_lower_tier_value:.2f}->{current[lower_tier]:.2f} to {higher_tier}: {old_higher_tier_value:.2f}->{current[higher_tier]:.2f}")


if __name__ == "__main__":
    resource_gain_per_run = {
        "t1" : 2.19,
        "t2" : 2.00,
        "t3" : 0.24
    }

    required_resources = {
        "t1" : 9.0,
        "t2" : 63.0,
        "t3" : 100.0
    }

    conversion_ratio = {
        "t1" : 3.0,
        "t2" : 3.0
    }

    current_resources = {
        "t1" : 0.0,
        "t2" : 0.0,
        "t3" : 0.0
    }

    current_run = 0
    while not is_complete(required_resources, current_resources):
        current_run += 1
        add_resources_after_run(resource_gain_per_run, current_resources)
        convert_excess_resources(conversion_ratio, required_resources, current_resources)
        show_current_status(current_run, required_resources, current_resources)
