# Time complexity: O((V+E)^2)
# Space complexity: O(V+E)
def find_itinerary(tickets: list) -> list:
    sorted_tickets = sorted(tickets)

    adj_list = dict()
    for dep, arr in sorted_tickets:
        if dep not in adj_list:
            adj_list[dep] = []
        adj_list[dep].append(arr)

    ans = ['JFK']

    def dfs(airport: str):
        if len(ans) == len(tickets)+1: return True
        if airport not in adj_list: return False

        destinations = adj_list[airport].copy()
        for i, destination in enumerate(destinations):
            adj_list[airport].pop(i)
            ans.append(destination)
            if dfs(destination):
                return True
            adj_list[airport].insert(i, destination)
            ans.pop()

        return False

    dfs('JFK')

    return ans
