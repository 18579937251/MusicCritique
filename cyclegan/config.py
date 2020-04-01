import os


class Config(object):
    def __init__(self):
        self.name = 'steely_gan'
        self.dataset_name = 'free_midi_library'
        self.genreA = 'rock'
        self.genreB = 'jazz'

        self.phase = 'train'
        self.continue_train = True

        self.direction = 'AtoB'

        self.model = 'full' # three different models, base, partial, full
        self.gaussian_std = 1
        self.use_image_pool = True
        self.image_pool_info = 'pooled' if self.use_image_pool else 'not_pooled'

        self.save_path = 'd:/checkpoints/' + '{}2{}_{}_{}_gn{}'.format(self.genreA, self.genreB, self.model, self.image_pool_info, self.gaussian_std)
        self.model_path = self.save_path + '/models'
        self.checkpoint_path = self.save_path + '/checkpoints'

        self.log_path = self.save_path + '/info.log'
        self.loss_save_path = self.save_path + '/losses.json'

        self.test_path = self.save_path + '/test_results'
        self.test_save_path = self.test_path + '/' + self.direction

        self.G_A2B_save_path = self.model_path + '/G_A2B/'
        self.G_B2A_save_path = self.model_path + '/G_B2A/'
        self.D_A_save_path = self.model_path + '/D_A/'
        self.D_B_save_path = self.model_path + '/D_B/'

        self.D_A_all_save_path = self.model_path + '/D_A_all/'
        self.D_B_all_save_path = self.model_path + '/D_B_all/'

        self.image_pool_max_size = 20

        self.max_dataset_size = 10000
        self.dataset_mode = 'unaligned'

        self.track_merged = False
        self.sigma_c = 1.0
        self.sigma_d = 1.0

        self.time_step = 120
        self.bar_length = 4
        self.note_valid_range = (24, 108)
        self.note_valid_length = 84
        self.instr_num = 5

        self.gpu = True

        self.beta1 = 0.5                     # Adam optimizer beta1 & 2
        self.beta2 = 0.999

        self.lr = 0.00005
        self.weight_decay = 0.1

        self.g_lr = 2e-4                     # generator learning rate
        self.d_lr = 2e-4                     # discriminator learning rate

        self.no_flip = True
        self.num_threads = 1
        self.batch_size = 16
        self.max_epoch = 30
        self.epoch_step = 5

        self.data_shape = (self.batch_size, 1, 64, 84)
        self.input_shape = (1, 64, 84)

        self.plot_every = 100  # iterations
        self.save_every = 5  # epochs

        self.start_epoch = 0


if __name__ == '__main__':
    config = Config()
    print(config.save_path)

