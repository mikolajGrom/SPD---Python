from operator import itemgetter


def johnsons_algorithm(tasks, machines):
    virtual_tasks, optimal_begining, optimal_ending = []

    if machines == 3:
        for item in tasks:
            virtual_tasks[0] = item[0] + item[1]
            virtual_tasks[1] = item[1] + item[2]
    elif machines == 2:
        virtual_tasks = tasks

    while len(virtual_tasks) != 0:
        p1 = min(virtual_tasks, key=itemgetter(0))
        p2 = min(virtual_tasks, key=itemgetter(1))
        if p1 <= p2:
            optimal_begining.append(p1)
            virtual_tasks.remove(p1)
        else:
            optimal_ending.insert(0, p2)
            virtual_tasks.remove(p2)
    optimal_order = optimal_begining + optimal_ending
    return optimal_order
