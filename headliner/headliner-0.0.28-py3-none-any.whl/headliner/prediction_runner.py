from sklearn.model_selection import train_test_split

from headliner.training_runner import read_data_json
from headliner.model.summarizer_bert import SummarizerBert

if __name__ == '__main__':

    train = read_data_json('/Users/cschaefe/datasets/welt_dedup.json', 400)[:1000]
    train_data, val_data = train_test_split(train, test_size=100, shuffle=True, random_state=32)
    path_to_model = '/Users/cschaefe/Downloads/transformer_check_3rd_training'
    summarizer = SummarizerBert.load(path_to_model)
    summarizer.max_prediction_len = 30
    for val_index in range(100):
        text = val_data[val_index][0]
        target = val_data[val_index][1]
        print('(target) {}'.format(target))
        pred = summarizer.predict(text)
        print('(pred) {}'.format(pred))

