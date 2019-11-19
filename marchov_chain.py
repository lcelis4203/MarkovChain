import sys
sys.path.insert(0, "/usr/local/lib/python3.6/dist-packages/")
import markovify

with open("trump_tweets.txt") as f:
    text = f.read()
model_a = markovify.Text(text, state_size=2)

with open("metamorphosis_franz_kafka.txt") as f:
    text = f.read()
model_b = markovify.Text(text, state_size=2)

model_combo = markovify.combine([model_a, model_b], [5.0, 20.0])

for i in range(300):
    with open("trump_and_kafka.txt", 'a') as out:
        out.write(model_combo.make_sentence() + '\n' +'\n')
