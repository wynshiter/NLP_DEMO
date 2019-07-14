        :param input_vocab_size: 输入词表大小
        :param target_vocab_size: 输出词表大小
        :param batch_size: batch大小
        :param embedding_size: 输入输出词表嵌入维度
        :param mode: 取之为train,表示训练模式，取之为decode，代表预训练模式
        :param hidden_size: RNN模型中间层大小，Encoder和Decoder层相同
        :param depth: rnn层数
        :param beam_width: beansearch超参数，用于解码
        :param cell_type: rnn神经元类型，lstm， gru等
        :param dropout: 随机丢弃比例， 0到1之间取值
        :param use_dropout: 是否用dropout
        :param use_residual: 是否使用residual
        :param optimizer: 使用哪一个优化器
        :param learning_rate: 学习率
        :param min_learning_rate: 最小学习率
        :param decay_step: 衰减步骤
        :param max_gradient_norm: 梯度正则裁剪系数
        :param max_decode_step: 最大decode长度，可以非常大
        :param attention_type: 使用attention类型
        :param bidirection:是否双向encoder
        :param time_major: 是否在计算过程中使用时间作为主要大批量数据
        :param seed: 一些层间操作大随机数
        :param parallel_iterations: 并行执行RNN循环的个数
        :param share_embedding:是否让encoder和decoder共用embedding
        :param pretrained_embedding: 是否使用预训练的embedding