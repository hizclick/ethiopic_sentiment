data_folder = 'content_folder'
from flair.data import Corpus
from flair.datasets import ClassificationCorpus

corpus: Corpus = ClassificationCorpus(data_folder)

from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentRNNEmbeddings
from flair.trainers import ModelTrainer
from flair.models import TextClassifier


label_dict = corpus.make_label_dictionary()
word_embeddings = [WordEmbeddings('glove')]
document_embeddings = DocumentRNNEmbeddings(word_embeddings, hidden_size=256)
classifier = TextClassifier(document_embeddings, label_dictionary=label_dict)
trainer = ModelTrainer(classifier, corpus)
trainer.train('/content/data',
              learning_rate=0.1,
              mini_batch_size=32,
              anneal_factor=0.5,
              patience=5,
              max_epochs=150)
