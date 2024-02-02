def preprocess(data):
    # Drop recipes that have titles that are too short (less than 4 characters)
    data.drop(data[data['title'].str.len() < 4].index, inplace=True)

    # Drop recipes that have fewer than 2 ingredients
    data.drop(data[data['ingredients'].str.len() < 2].index, inplace=True)

    # Drop recipes that have fewer than 2 steps or are shorter than 30 characters
    data.drop(data[data.directions.map(lambda x: len(x) < 2 or len(''.join(x)) < 30)].index, inplace=True)
    
    # Drop recipes that contain "step" or "mix all" since this token is too frequent?
    data.drop(data[data.directions.map(lambda x: re.search('(step|mix all)', ''.join(str(x)), re.IGNORECASE)!=None)].index, inplace=True)

    return data