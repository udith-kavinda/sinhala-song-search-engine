from elasticsearch import Elasticsearch
import search_quaries
client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'lyrics2'

synonym_artist = ['ගායකයා','ගයනවා','ගායනා','ගායනා','ගැයු','ගයන','ගයපු']
synonym_lyricist = ['ගත්කරු','රචකයා','ලියන්නා','ලියන','රචිත','ලියපු','ලියව්‌ව','රචනා','රචක','ලියන්','ලියූ']
synonym_title = ['ගීතය']
synonym_list = [ synonym_artist, synonym_lyricist, synonym_title]


def search(search_query):
    processed_query = ""
    tokens = search_query.split()
    processed_tokens = search_query.split()
    search_fields = []
    year = 0
    field_list = ["artist", "lyricist", "title"]
    all_fields = ["title","artist", "lyricist", "album", "lyrics", "metaphors"]
    year_array = []

    if (search_query.strip() != ""):
        for word in tokens:
            print (word)

            if word.isdigit():
                temp_word = word
                if(len(str(word.lstrip('0'))) == 1):
                    temp_word+="000"
                elif((len(str(word.lstrip('0'))) == 2)):
                    temp_word+="00"
                elif((len(str(word.lstrip('0'))) == 3)):
                    temp_word+="0"
                elif((len(str(word.lstrip('0'))) > 4)):
                    temp_word = word[0:4]
                print(temp_word)
                year = int(temp_word)
                year_array.append(year)
                search_query = year
                processed_tokens.remove(word)
                print ('Identified year ',year)

            for i in range(0, 3):
                if word in synonym_list[i]:
                    print('Adding field', field_list[i], 'for ', word, 'search field list')
                    search_fields.append(field_list[i])
                    processed_tokens.remove(word)

        if (len(processed_tokens)==0 and year != 0):
            processed_query = []
        elif (len(processed_tokens) ==0 and year ==0):
            processed_query = search_query
        else:
            processed_query = " ".join(processed_tokens)

        final_fields = search_fields

        if (year==0):
            print('Faceted Query')
            if(len(search_fields)==0):
                query_es = search_quaries.multi_match_best(processed_query, all_fields)
            else:
                query_es = search_quaries.multi_match_best_with_fields(processed_query, final_fields)

        else:
            print('Range Query')
            if(len(year_array) > 1):
                years = sorted(year_array)
                years = [year_array[0] ,year_array[-1]]
                if (len(processed_query) == 0):
                    query_es = search_quaries.multi_match_year_without_query(years, all_fields)
                else:
                    if(len(search_fields)==0):
                        query_es = search_quaries.multi_match_year_with_query(processed_query, years, all_fields)
                    else:
                        query_es = search_quaries.multi_match_year_with_query(processed_query, years, final_fields)
            else:
                if (len(processed_query) == 0):
                    query_es = search_quaries.multi_match_single_year_without_query(year, ["year"])
                else:
                    if(len(search_fields)==0):
                        query_es = search_quaries.multi_match_single_year_with_query(processed_query, year, all_fields)
                    else:
                        query_es = search_quaries.multi_match_single_year_with_query(processed_query, year, final_fields)


        print("QUERY BODY")
        print(query_es)
        search_result = client.search(index=INDEX, body=query_es)
        print(search_result)
        return search_result

    else:
        return {"hits": {"hits": []}}





