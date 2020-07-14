"""
GloVe Word Embedding
"""
import numpy as np
import os, pickle
from OpenAttack.utils import WordVector, make_zip_downloader

NAME = "Glove"

URL = "https://thunlp.oss-cn-qingdao.aliyuncs.com/TAADToolbox/glove.zip"
DOWNLOAD = make_zip_downloader(URL)


def LOAD(path):
    word2id = pickle.load( open( os.path.join(path, "word2id.pkl"), "rb") )
    wordvec = np.load( os.path.join(path, "wordvec.npy") )
    return WordVector(word2id, wordvec)
