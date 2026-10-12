messages = [
    (("P0", 1), ("P1", 1)),
    (("P2", 3), ("P1", 2)),
    (("P1", 2), ("P0", 2)),
    (("P1", 2), ("P2", 4)),
    (("P1", 3), ("P2", 6)),
    (("P2", 5), ("P1", 4)),
    (("P1", 4), ("P0", 4)),
]

initial_cut = {
    "P0": 2,
    "P1": 2,
    "P2": 6
}

def is_consistent(cut, messages):
    for send, receive in messages:
        sender, send_event = send
        receiver, receive_event = receive

        send_included = send_event <= cut[sender]
        receive_included = receive_event <= cut[receiver]

        if receive_included and not send_included:
            return False

    return True


def compute_consistent_cut(initial_cut, messages):
    cut = initial_cut.copy()
    pass_number = 0

    while True:
        pass_number += 1
        changed = False

        print(f"Pass {pass_number}: {cut}")

        for send, receive in messages:
            sender, send_event = send
            receiver, receive_event = receive

            send_included = send_event <= cut[sender]
            receive_included = receive_event <= cut[receiver]

            if receive_included and not send_included:
                print(
                    f"  {receiver} event {receive_event} is included, "
                    f"but {sender} event {send_event} is missing."
                )

                cut[receiver] = receive_event - 1
                changed = True

                print(f"  Move {receiver} backwards: {cut}")

        if not changed:
            return cut

result = compute_consistent_cut(initial_cut, messages)

print("Final cut:", result)
print("Consistent:", is_consistent(result, messages))

assert is_consistent(result, messages)

assert is_consistent(result, messages)

assert all(
    result[process] <= initial_cut[process]
    for process in initial_cut
)