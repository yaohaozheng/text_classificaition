class CONFIG():
    update_w2v = True           # 是否在训练中更新w2v
    #vocab_size = 59290          # 词汇量，与word2id中的词汇量一致,训练时候大小，59290
    vocab_size=58954             #预测时候大小根据实际报错来定
    n_class = 2                 # 分类数：分别为pos和neg
    max_sen_len = 75            # 句子最大长度
    embedding_dim = 50          # 词向量维度
    batch_size = 100            # 批处理尺寸
    n_hidden = 256              # 隐藏层节点数
    n_epoch = 10                # 训练迭代周期，即遍历整个训练样本的次数
    opt = 'adam'                # 训练优化器：adam或者adadelta
    learning_rate = 0.001       # 学习率；若opt=‘adadelta'，则不需要定义学习率
    drop_keep_prob = 0.5        # dropout层，参数keep的比例
    num_filters = 256           # 卷积层filter的数量
    kernel_size = 3             # 卷积核的尺寸；nlp任务中通常选择2,3,4,5
    print_per_batch = 100       # 训练过程中,每100词batch迭代，打印训练信息
    save_dir = './checkpoints/' # 训练模型保存的地址
    train_path = './data/train.txt'
    dev_path = './data/validation.txt'
    test_path = './data/test.txt'
    word2id_path = './data/word_to_id.txt'
    pre_word2vec_path = './data/wiki_word2vec_50.bin'
    corpus_word2vec_path = './data/corpus_word2vec.txt'

