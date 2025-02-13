import argparse

def init_parser(alg):

    if alg == 'A2C':

        parser = argparse.ArgumentParser(description='Thesis')
        parser.add_argument('--logger')
        parser.add_argument('--name')
        parser.add_argument('--gpu', default='0', type=str)
        parser.add_argument('--device')

        parser.add_argument('--gamma', type=float, default=1, metavar='G', help='discount factor for rewards (default: 0.99)')
        parser.add_argument('--epoch_num', type=int, default=40)
        parser.add_argument('--test_episode', type=int, default=50)
        parser.add_argument('--val_episode', type=int, default=50)
        parser.add_argument('--test_size', type=int, default=0.1, help='')
        parser.add_argument('--val_size', type=int, default=0.5, help='')
        parser.add_argument('--batch_size', default=1, type=int, help='')
        parser.add_argument('--train_batch_size', default=1, type=int, help='')
        parser.add_argument('--num_steps', default=10, type=int, help='')
        parser.add_argument('--h', default=1, type=int, help='hidden layer')
        parser.add_argument('--w', nargs='+', default=[120, 50], type=int)
        parser.add_argument('--nn_out', default=40, type=int)
        parser.add_argument('--share_lr', type=float, default=0.001, help='learning rate.')
        parser.add_argument('--actor_lr', type=float, default=0.0001, help='learning rate.')
        parser.add_argument('--critic_lr', type=float, default=0.0001, help='learning rate.')
        parser.add_argument('--step', type=float, default=100, help='learning rate decay step.')
        parser.add_argument('--lr_min', type=float, default=1e-4, help='learning rate minimum.')
        parser.add_argument('--e_rate', type=float, default=0.001, help='.')
        parser.add_argument('--a_rate', type=float, default=1, help='.')
        parser.add_argument('--c_rate', type=float, default=1, help='.')
        parser.add_argument('--lr_decay_lambda', type=float, default=0.999, help='.')#0.999999999

        parser.add_argument('--load', type=bool, default=False, help='')
        parser.add_argument('--duse_T', type=bool, default=True, help='')
        parser.add_argument('--est_T', type=bool, default=False, help='')
        parser.add_argument('--use_pref', type=bool, default=False, help='')
        parser.add_argument('--same_price', type=bool, default=False, help='')
        parser.add_argument('--use_price', type=bool, default=True, help='')
        parser.add_argument('--only_test', type=bool, default=False, help='')
        parser.add_argument('--change_T', type=bool, default=True, help='')

        parser.add_argument('--num', default='0', type=str, help='number of experiment')
        parser.add_argument('--print_grad', type=bool, default=False, help='')
        parser.add_argument('--max_norm', type=int, default=10, help='')
        parser.add_argument('--seed_range', default=20, type=int, help='')
        parser.add_argument('--net_seed', default=0, type=int, help='')
        parser.add_argument('--seed', default=0, type=int, help='')
        parser.add_argument('--info', type=bool, default=True, help='')
        parser.add_argument('--cardinality', default=4, type=int, help='size constraint')
        parser.add_argument('--ini_inv', default=10, type=int, help='initial inventory')
        parser.add_argument('--num_products', default=10, type=int, help='')
        parser.add_argument('--number_samples', default=10000, type=int, help='')
        parser.add_argument('--num_cus_types', default=4, type=int, help='')
        parser.add_argument('--cus_use_time', default=[20,25,30,35],help='usage time of corresponding customer type')

        parser.add_argument('--cus_type', help='array 4*100, four prob vectors of four customers, towards 100 extracted preference lists')
        parser.add_argument('--seg_prob')
        parser.add_argument('--rank_list', help='array 100*11, 100 extracted preference lists')
        parser.add_argument('--seqdata')
        parser.add_argument('--transdata')
        parser.add_argument('--test_opt', type=bool, default=False, help='')
        #parser.add_argument('--seg_prob')
        
        parser.add_argument('--detail', type=bool, default=False)
        
        parser.add_argument('--T', default=40, type=int, help='how long is history')
        return parser

    else:

        raise RuntimeError('undefined algorithm {}'.format(alg))