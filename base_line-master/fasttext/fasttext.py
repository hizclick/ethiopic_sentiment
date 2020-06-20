import fasttext
import datetime

hyper_params = {"lr": 0.01,
                "epoch": 50,
                "wordNgrams": 4,
                "dim": 20}     
                               
print(str(datetime.datetime.now()) + ' START=>' + str(hyper_params) )
# Train the model.
model = fasttext.train_supervised(input='base_train.csv', **hyper_params)
print("Model trained with the hyperparameter \n {}".format(hyper_params))

model_acc_training_set = model.test(train_file_path)
model_acc_validation_set = model.test('validation_path')
        
# DISPLAY ACCURACY OF TRAINED MODEL
text_line = str(hyper_params) + ",accuracy:" + str(model_acc_training_set[1])  + ",validation:" + str(model_acc_validation_set[1]) + '\n' 
print(text_line)
