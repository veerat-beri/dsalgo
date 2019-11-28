# Problem Statement
# https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/


def shift_n_disks(no_of_disks):
    def _shift_n_disks(remaining_disks, aux_pillar, from_pillar, to_pillar):
        if remaining_disks == 1:
            print('moving disk=1 from pillar={} to second-pillar={}'.format(from_pillar, to_pillar))
            return

        _shift_n_disks(remaining_disks-1, to_pillar, from_pillar, aux_pillar)
        print('move disk={} from pillar={} to pillar={}'.format(remaining_disks, from_pillar, to_pillar))
        _shift_n_disks(remaining_disks-1, from_pillar, aux_pillar, to_pillar)
        print('move disk={} from pillar={} to pillar={}'.format(remaining_disks, from_pillar, to_pillar))

    _shift_n_disks(no_of_disks, 'A', 'B', 'C')


# driver code
def run():
    print('Main pillar={}, Aux pillar={}, To pillar={}'.format('A', 'B', 'C'))
    shift_n_disks(3)


if __name__ == '__main__':
    run()
