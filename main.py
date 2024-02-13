import random
from dataclasses import dataclass

from our_array import Array
from our_queue import IntQueue


@dataclass
class Stats:
    """Data class for collecting simulation statistics."""
    server_idle: int = 0
    customers_served: int = 0
    customers_turned_away: int = 0


def coffee_shop_simulator(line_capacity: int, serve_time: int, next_low: int, next_high: int) -> Stats:
    """
    Simulate the serving line at a coffee shop using a queue.
    :param line_capacity: The maximum number of people who can stand in line.
    :param serve_time: The time in seconds to serve a customer.
    :param next_low: The lowest amount of time for the arrival of the next customer.
    :param next_high: The maximum amount of time for the arrival of the next custmer.
    :return: The statistics accumulated during the simulation.
    """

    print(f"""
╔════════════════════════════════════╗
║     Sandy and Ian's Coffee         ║ 
╟────────────────────────────────────╢
║ Served in {serve_time} seconds or it's free! ║
╚════════════════════════════════════╝
""")

    # store customers in a queue data structure
    line_up: IntQueue = IntQueue(line_capacity)

    # track statistics throughout simulation
    stats: Stats = Stats()

    # information about the next customer
    next_customer_number: int = 1
    next_customer_arrival: int = random.randint(next_low, next_high)

    # countdown to next coffee served
    next_serve: int = serve_time

    time: int
    for time in range(10000):

        next_customer_arrival -= 1

        # next customer arrives and is either turned away or enters the line.
        if next_customer_arrival == 0:
            if line_up.is_full():
                stats.customers_turned_away += 1
                print(f"[{time}] Customer {next_customer_number} left: line too long...")
            else:
                line_up.enqueue(next_customer_number)

            # setup the arrival of the next customer.
            next_customer_arrival = random.randint(next_low, next_high)
            next_customer_number += 1

        # track if the server is "idle", that is not making coffee.
        if line_up.is_empty():
            stats.server_idle += 1

        # otherwise the server can make a coffee every "serve_time" seconds.
        else:
            next_serve -= 1
            if next_serve == 0:
                num: int = line_up.dequeue()
                print(f"[{time}] Customer {num} served.")
                stats.customers_served += 1
                next_serve = serve_time

    print(f"Served {stats.customers_served} customers.")
    print(f"Was idle for {stats.server_idle} seconds.")
    print(f"Turned away {stats.customers_turned_away} customers.")

    return stats


LINE_CAPACITY = 8
SERVE_TIME = 30
NEXT_CUSTOMER_LOW = 1
NEXT_CUSTOMER_HIGH = 60


def test_correctness(stats: Stats):
    assert stats.customers_served == 326, "Problem with queue implementation"
    assert stats.server_idle == 220, "Problem with queue implementation"
    assert stats.customers_turned_away == 4, "Problem with queue implementation"


def test_efficiency():
    assert Array.access_counter <= 2608, "Good start! but this could be optimized a bit more..."
    assert Array.access_counter <= 326, "Great! But we could do better..."


def main():
    random.seed(123)
    stats: Stats = coffee_shop_simulator(LINE_CAPACITY, SERVE_TIME, NEXT_CUSTOMER_LOW, NEXT_CUSTOMER_HIGH)
    test_correctness(stats)
    test_efficiency()


if __name__ == "__main__":
    main()
