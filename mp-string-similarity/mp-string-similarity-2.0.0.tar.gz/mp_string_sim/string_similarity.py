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
  jarowinkler = JaroWinkler()
  counted = {}
  for event_name in names:
    counted[event_name] = 1
    for compared_event in names:
      if event_name == compared_event:
        continue
      if counted.get(compared_event, 0):
        continue
      if jarowinkler.similarity(event_name, compared_event) > limit:
        similar_events[compared_event].append(event_name)
        similar_events[event_name].append(compared_event)
        similar_event_count += 2
  similarity = similar_event_count  / len(names) ** 2
  response = {
    "similar_events" : similar_events,
    "similarity_percentage" : similarity,
    "similar_event_count": similar_event_count,
    "total_event_count": len(names),
    "similarity_threshold" : limit
  }
  return response 