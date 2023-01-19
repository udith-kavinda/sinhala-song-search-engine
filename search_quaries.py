import json


#best_filds
def multi_match_best(query, fields=['title','lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
	}

	q = json.dumps(q)
	return q

def multi_match_best_with_fields(query, fields=['title','lyrics']):
	print ("QUERY FIELDS")
	print (fields)
	q = {
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "best_fields"
			}
		},
	}

	q = json.dumps(q)
	return q

def multi_match_year_without_query(year, fields=['year']):
	q = {
		"query": {
            "bool": {
            "filter": [
                {
                "range": {
                    "year": {
                    "gte": str(year[0]),
                    "lte": str(year[1])
                    }
                }
                }
            ]
            }
        },
	}
	q = json.dumps(q)
	return q


def multi_match_year_with_query(query, year, fields=['year']):
	q = {
		"query": {
            "bool": {
            "filter": [
                {
                "range": {
                    "year": {
                    "gte": str(year[0]),
                    "lte": str(year[1])
                    }
                }
                },
                {
                "multi_match": {
                    "query": query,
                    "fields": fields,
					"type": "best_fields"
                }
                }
            ]
            }
        },
	}
	q = json.dumps(q)
	return q


def multi_match_single_year_without_query(year, fields=['year']):
	q = {
		"query": {
			"match": {
				"year": {"query": str(year)}
			}
		},
	}
	q = json.dumps(q)
	return q

def multi_match_single_year_with_query(query, year, fields=['year']):
	q = {
		"query": {
            "bool": {
            "filter": [
                {
                "match": {
				    "year": {"query": str(year)}
			    }
                },
                {
                "multi_match": {
                    "query": query,
                    "fields": fields,
					"type": "best_fields"
                }
                }
            ]
            }
        }
	}
	q = json.dumps(q)
	return q

