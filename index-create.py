from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json
import datetime

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'lyrics2'

def createIndex():
    settings = {
        "settings": {
            "index":{
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis" :{
                "analyzer":{
                    "sinhala-analyzer":{
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter":["edge_ngram_custom_filter"]
                    }
                },
                "filter" : {
                    "edge_ngram_custom_filter":{
                        "type": "edge_ngram",
                        "min_gram" : 2,
                        "max_gram" : 50,
                        "side" : "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                    "title": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "lyrics": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "artist": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "lyricist": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "album": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "year": {
                        "type": "date",
                        "format": "yyyy",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "metaphors": {
                        "type": "nested",
                        "properties": {
                            "songPart": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "interpretation": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "type": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "sourceDomain": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            },
                            "targetDomain": {
                                "type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword",
                                        "ignore_above": 256
                                    }
                                },
                                "analyzer" : "sinhala-analyzer",
                                "search_analyzer": "standard"
                            }
                        }
                    }
            }
        }
    }
    result = client.indices.create(index=INDEX , body =settings)
    print (result)

def read_all_songs():
    with open('./data/sinhala-songs.json', 'r', encoding='utf8') as f:
        tra_songs = json.loads(f.read())
        results_list = [a for num, a in enumerate(tra_songs) if a not in tra_songs[num + 1:]]
        return results_list

def genData(song_array):
    for song in song_array:

        title = song["title"]
        artist = song["artist"]
        lyricist = song["lyricist"]
        album = song["album"]
        year = datetime.datetime(int(song["year"]), 1, 1).year
        lyrics = song["lyrics"]
        metaphors = song["metaphors"]
        
        yield {
            "_index": INDEX,
            "_source": {
                "title": title,
                "artist": artist,
                "lyricist": lyricist,
                "album": album,
                "year": year,
                "lyrics": lyrics,
                "metaphors": metaphors
            },
        }



createIndex()
all_songs = read_all_songs()
# print(all_songs[0]['metaphors'][0])
# print(len(all_songs))
# genData(all_songs)
#print(genData)
helpers.bulk(client,genData(all_songs))