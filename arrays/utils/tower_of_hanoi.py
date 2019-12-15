# Problem Statement
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/


def shift_n_disks(disk_num, aux_pillar, from_pillar, to_pillar):
    if disk_num == 1:
        print('moving disk=1 from {} to {}'.format(from_pillar, to_pillar))
        return

    shift_n_disks(disk_num-1, to_pillar, from_pillar, aux_pillar)
    print('move disk={} from {} to {}'.format(disk_num, from_pillar, to_pillar))
    shift_n_disks(disk_num-1, from_pillar, aux_pillar, to_pillar)


# driver code
def run():
    #                |                   |                   |
    #                |                   |                   |
    #                -                   |                   |
    #               ---                  |                   |
    #              -----                 |                   |
    #            _________           _________           _________
    #         A (Source pillar)    B (Aux pillar)    C (Destination pillar)

    from_pillar = 'A'
    aux_pillar = 'B'
    to_pillar = 'C'
    num_of_disks = 64

    print('Main pillar={}, Aux pillar={}, To pillar={}\n'.format(from_pillar, aux_pillar, to_pillar))
    shift_n_disks(num_of_disks, aux_pillar, from_pillar, to_pillar)


if __name__ == '__main__':
    run()
