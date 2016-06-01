```
def get_kNN_result(name):
    # Analyze start
    new_list = []
    new_vector = []
    cos_list = []
    result = []
    # Chinese participle
    new_cut = jieba.cut_for_search(name)
    # Generate new words list
    for cut in new_cut:
        if not (cut.strip() in stop_list):
            new_list.append(cut)
    # Generate vector by mapping
    for c_name in corpus_names:
        if not (c_name[0].strip() in new_list):
            new_vector.append(0)
        else:
            new_vector.append(1)
    # Get the list of Cosine Similarity
    for fid, vector in failure_names:
        cos = get_cos_similar(new_vector, list(eval(vector)))
        cos_list.append((cos, fid))
    # Sort the list of last step and get top5
    k_nn5 = sorted(cos_list)[-5:]
    k_nn5.reverse()  # big to small
    # Get id and similarity of top5
    case_collect5 = []
    for cos, fid in k_nn5:
        case_collect5.append(fid)
    print(case_collect5)
    # Query the top5 cases
    cursor.execute('select id,name,industry,mode from failurecase where id in ' + str(tuple(case_collect5)))
    value_cases = cursor.fetchall()
    print(value_cases)
    # Sort the list(value_cases)
    case_dict = {}
    for item2 in value_cases:
        case_dict[item2[0]] = {'name': item2[1], 'industry': item2[2], 'mode': item2[3]}
    for item1 in case_collect5:
        dict_item = case_dict[item1]
        dict_item['id'] = item1
        result.append(dict_item)
    return result
```
