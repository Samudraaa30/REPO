def search_repository(index, query):

    query = query.lower()

    results = []

    for file in index:

        if query in file["name"].lower():

            results.append(file)

    return results