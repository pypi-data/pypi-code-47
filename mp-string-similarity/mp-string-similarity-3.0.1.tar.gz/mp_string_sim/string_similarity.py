from multiprocessing import Process
import re
from strsimpy.jaro_winkler import JaroWinkler
from collections import defaultdict, Counter

def word_cloud(names, top=5, delimiters=[' ']):
  # Word Cloud will take a list of names and return a count of words
  # this is intended to find common words used multiple times in a given
  # implementation.
  word_counts = defaultdict(int) 
  total_words = 0
  for name in names:
    for word in split(name, delimiters):
      word_counts[word] += 1 
      total_words += 1
    top_words = Counter(word_counts).most_common(top)
  response = {
    "common_words": top_words,
    "total_words": total_words
  }
  return (top_words, total_words)

def split(name, delimiters, maxsplit=0):
    regexpattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexpattern, name, maxsplit)

def similarity(names, limit = .6):
  ## Given a list of events return the events that have a similarity > .6
  ## Should this return a metric?
  ## What happens when an event is similar to > 1 event

  similar_events = defaultdict(list)
  similar_event_count = 0
  similarity = 0
  compared = {}
  if len(names):
    for event_name in names:
      compared[event_name] = 1

      response = compare_words(event_name, names, compared, limit)
      similar_event_count += response["similar_event_count"]
      for event, similar in dict.items(response["similar_events"]):
        similar_events[event] = similar 
    similarity = similar_event_count  / len(names) ** 2
  response = {
    "similar_events" : similar_events,
    "similarity_percentage" : similarity,
    "similar_event_count": similar_event_count,
    "total_event_count": len(names),
    "similarity_threshold" : limit
  }
  return response 

def compare_words(word, words, compared, limit):
  jarowinkler = JaroWinkler()
  similar_event_count = 0
  similar_events = defaultdict(list)
  for compared_word in words:
    if word == compared_word:
      continue
    if compared.get(compared_word, 0):
      continue
    if jarowinkler.similarity(word, compared_word) > limit:
      similar_events[compared_word].append(word)
      similar_events[word].append(compared_word)
      similar_event_count += 2
  response = {
    "similar_events" : similar_events,
    "similar_event_count": similar_event_count,
  }
  return response 